from matplotlib import pyplot as plt
import numpy as np
import os
import sys

os.chdir(sys.path[0])
os.chdir('./')

my_figsize = [16, 10]
my_fontsize = 40

WIDTH = 0.07  # the width of the bars


SHORT = 100000 # 100KB
LONG = 10000000


METRICS = ['GOODPUT']

PIAS = ['NO-PIAS']
# SCHEMES = ['NegotiaToR', 'benes']
SCHEMES = ['NegotiaToR-8uplinks', 'benes']
# SCHEMES = ['NegotiaToR', 'PIM']

# WORKLOAD = ['foindegree']
# FIG_FILE_NAME = 'incast'

WORKLOAD = ['incast']
FIG_FILE_NAME = 'incast'


# LOADS = ['0.1', '0.25', '0.5', '0.75', '1']
# labels = ['10', '25', '50', '75', '100'] # LOADS
LOADS = [2, 4, 6, 8, 10, 12, 14, 16]
labels = [2, 4, 6, 8, 10, 12, 14, 16]

GOSSIP = [300]

SCHEDULED = [20]

DATA_DIR_TEMP  = '../DATA/{pias}/{scheme}/DATA_vote_{workload}_{load}_gossip_{gossip}_scheduled_{scheduled}/'

FIGURE_DIR = '../FIGS/'+ FIG_FILE_NAME +'/GOODPUT/'
if not os.path.exists(FIGURE_DIR):
    os.makedirs(FIGURE_DIR)

# load data ----------------------------------------------------------------
data = {}
for scheme in SCHEMES:
    data[scheme] = {}
    for pias in PIAS:
        data[scheme][pias] = {}
        for workload in WORKLOAD:
            data[scheme][pias][workload] = {}
            for load in LOADS:
                data[scheme][pias][workload][load] = {}
                for gossip in GOSSIP:
                    data[scheme][pias][workload][load][gossip] = {}
                    for scheduled in SCHEDULED:
                        data[scheme][pias][workload][load][gossip][scheduled] = {}
                   
                

for scheme in SCHEMES:
    for pias in PIAS:
        for workload in WORKLOAD:
            for load in LOADS:
                for gossip in GOSSIP:
                    for scheduled in SCHEDULED:
                        dir_path = DATA_DIR_TEMP.format(pias=pias, scheme=scheme, workload=workload, load=load, gossip=gossip, scheduled=scheduled)
                        data[scheme][pias][workload][load]['PATH'] = dir_path
                        for metric in METRICS:
                            data_path = dir_path + metric + '.txt'
                            data[scheme][pias][workload][load][gossip][scheduled][metric] = np.loadtxt(data_path)
                            print("LOADED: ", scheme, pias, workload, load, gossip, scheduled, metric)


print("DATA LOADED!")

# 0  << f->id << " "
# 1 << f->start_time << " "
# 2 << f->src->id << " "
# 3 << f->dst->id << " "
# 4 << f->size << " "
# 5 << slow << " "
# 6 << f->finish_time << " "
# 7 << f->flow_completion_time << "\n";

# GOODPUT(host标号，goodput，收到的总bytes，收到第一个包的时间，收完最后一个包的时间)
def goodput_bar_plot(labels):
    results = {}
    for scheme in SCHEMES:
        results[scheme] = []
        for load in LOADS:
            idx = data[scheme][pias][workload][load][gossip][scheduled]['GOODPUT'][:, 2] > 0
            goodput = data[scheme][pias][workload][load][gossip][scheduled]['GOODPUT'][idx, 1] # goodput
            results[scheme].append(np.mean(goodput))


    x_tick = np.arange(len(labels))*0.3 # the label locations
    x = x_tick - (len(SCHEMES)-1)*WIDTH/2

    # hatches = ["xxxx", "", "\\\\", "", "////"]
    # colors = ["white", "black", "white", "white", "white"]

    # schemes = ['Ideal', 'Zeropod', 'Fastpass', 'DCTCP']

    hatches = ["", ".", "\\\\"]
    colors = ["white", "white", "white"]

    # SCHEMES_label = SCHEMES
    SCHEMES_label = ['NegotiaToR', 'benes']

    fig, ax = plt.subplots(figsize=my_figsize)
    ax.grid(axis="y")
    for i, scheme in enumerate(SCHEMES):
        ax.bar(x + WIDTH*i, results[scheme], WIDTH, edgecolor="black", color=[colors[i]], label=SCHEMES_label[i], hatch=hatches[i], linewidth = 3)

    ax.set_ylabel('Goodput (Gbps)', fontsize=my_fontsize)
    ax.set_xticks(x_tick)
    ax.set_xlabel("incast degree", fontsize=my_fontsize)
    ax.set_xticklabels(labels, fontsize=my_fontsize)
    ax.legend(ncol=1, loc = "upper left", fontsize=my_fontsize-2, handlelength = 1.5, borderpad = 0.2,  labelspacing = 0.3, columnspacing = 1.0)
    plt.xticks(fontsize=my_fontsize)
    plt.yticks(fontsize=my_fontsize)

    figure_path = FIGURE_DIR + 'goodput.pdf'
    plt.savefig(figure_path, dpi=300, bbox_inches='tight')

goodput_bar_plot(labels)