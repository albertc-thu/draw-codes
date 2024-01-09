from matplotlib import pyplot as plt
import numpy as np
import os
import sys

os.chdir(sys.path[0])
os.chdir('../')

my_figsize = [15, 10]
my_fontsize = 40

WIDTH = 0.07  # the width of the bars


PIAS = ['NO-PIAS']
SCHEMES = ['benes', 'NegotiaToR']
# WORKLOAD = ['W4']
WORKLOAD = ['W4']
LOADS = ['0.1', '0.25', '0.5', '0.75', '1']
labels = ['10', '25', '50', '75', '100'] # LOADS

METRICS = ['FCT']

# for scheme in SCHEMES:
#     file_path = '../DATA/' + PIAS + '/' + scheme +'/'
#     for load in LOADS:
#         file_name = 'DATA_vote_' + WORKLOAD + '_' + load + '_gossip_300_scheduled_20.txt'


SHORT = 100000 # 100KB
LONG = 10000000



# SCHEMES = ['ideal', 'fastpod', 'fastpass', 'dctcp']



GOSSIP = [300]
SCHEDULED = [20]

DATA_DIR_TEMP  = './DATA/{pias}/{scheme}/DATA_vote_{workload}_{load}_gossip_{gossip}_scheduled_{scheduled}/'

FIGURE_DIR = './FIGS/' + WORKLOAD[0] + '/FCT'
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


# mode = ['mean', 'meadian', '99p']
def slowdown_bar_plot(mode, labels, flow_range='all'):
    results = {}
    for scheme in SCHEMES:
        results[scheme] = {}
        results[scheme][mode] = []
        for load in LOADS:
            if flow_range == 'short':
                idx = data[scheme][pias][workload][load][gossip][scheduled]['SHORT_IDX']
            elif flow_range == 'long':
                idx = data[scheme][pias][workload][load][gossip][scheduled]['LONG_IDX']
            elif flow_range == 'middle':
                idx = data[scheme][pias][workload][load][gossip][scheduled]['MIDDLE_IDX']
            elif flow_range == 'all':
                idx = np.arange(len(data[scheme][pias][workload][load][gossip][scheduled]['FCT']))

            available_idx = data[scheme][pias][workload][load][gossip][scheduled]['FCT'][:, 7] > 0 # 过滤未完成的流
            idx = idx * available_idx

            fct = data[scheme][pias][workload][load][gossip][scheduled]['FCT'][idx, 7] # fct
            if mode == 'Mean':
                results[scheme][mode].append(1000 * np.mean(fct))
            elif mode == 'Median':
                results[scheme][mode].append(1000 * np.percentile(fct, 50))
            elif mode == '99p':
                results[scheme][mode].append(1000 * np.percentile(fct, 99))

    x_tick = np.arange(len(labels))*0.3 # the label locations
    x = x_tick - (len(SCHEMES)-1)*WIDTH/2

    # hatches = ["xxxx", "", "", "////"]
    # colors = ["white", "black", "white", "white"]

    hatches = ["", "", "\\\\"]
    colors = ["white", "black", "white"]

    # schemes = ['Ideal', 'Zeropod', 'Fastpass', 'DCTCP']

    schemes = SCHEMES

    fig, ax = plt.subplots(figsize=my_figsize)
    ax.grid(axis='y')
    for i, scheme in enumerate(SCHEMES):
        # ax.bar(x + WIDTH*i, results[scheme][mode], WIDTH, label=scheme)
        # 一次画一个scheme的所有load的bar
        ax.bar(x + WIDTH*i, results[scheme][mode], WIDTH, edgecolor="black", color=[colors[i]], label=schemes[i], hatch=hatches[i], linewidth = 3)

    if mode == "Mean":
        ax.set_ylabel('Avg. FCT (ms)', fontsize=my_fontsize)
    else:
        ax.set_ylabel(mode + ' FCT (ms)', fontsize=my_fontsize)
    ax.set_xlabel("Load (%)", fontsize=my_fontsize)
    ax.set_xticks(x_tick)

    plt.xticks(fontsize=my_fontsize)
    plt.yticks(fontsize=my_fontsize)

    ax.set_xticklabels(labels, fontsize=my_fontsize)
    # ax.set_ylim([0,3.0])
    # ax.legend(ncol=4, loc = "upper left", fontsize=20)
    ax.legend(ncol=2, loc = "upper left", fontsize=my_fontsize-2, handlelength=1.5, borderpad = 0.2, labelspacing = 0.3, columnspacing = 1.0)

    figure_path = FIGURE_DIR + "inpod_256_" + mode.lower() + '_fct_' + flow_range + '.pdf'
    plt.savefig(figure_path, dpi=300, bbox_inches='tight')


slowdown_bar_plot('Mean', labels)
slowdown_bar_plot('Median', labels)
slowdown_bar_plot('99p', labels)

slowdown_bar_plot('Mean', labels, 'short')
slowdown_bar_plot('Median', labels, 'short')
slowdown_bar_plot('99p', labels, 'short')

slowdown_bar_plot('Mean', labels, 'long')
slowdown_bar_plot('Median', labels, 'long')
slowdown_bar_plot('99p', labels, 'long')

slowdown_bar_plot('Mean', labels, 'middle')
slowdown_bar_plot('Median', labels, 'middle')
slowdown_bar_plot('99p', labels, 'middle')