from matplotlib import pyplot as plt
# from brokenaxes import brokenaxes
import numpy as np
import os
import sys
import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter

my_figsize = [15, 10]
my_fontsize = 30
WIDTH = 0.05  # the width of the bars
SHORT = 10000 # 1KB
LONG = 100000 # 100KB
# LOADS = ['0.1', '0.25', '0.5', '0.75', '1']
# labels = ['10', '25', '50', '75', '100'] # LOADS

# LOADS = [2, 4, 6, 8, 10, 12, 14, 16]
# labels = [2, 4, 6, 8, 10, 12, 14, 16]
# LOADS = [2, 4, 6, 8, 10, 15, 20, 30, 40, 50]
# labels = [2, 4, 6, 8, 10, 15, 20, 30, 40, 50]

LOADS = ['0.25']
labels = ['2', '3', '4', '5', '6']
# WORKLOADS = ['W1', 'W2', 'W3', 'W4']
WORKLOADS = ['W4']
# WORKLOADS = ['incast']
# WORKLOADS = ['uniformincast']

GOSSIP = [300]

SCHEDULED = [30]

# PIAS = ['PIAS', 'NO-PIAS']
PIAS = ['PIAS']


METRICS = ['FCT', 'GOODPUT']


os.chdir(sys.path[0])
os.chdir('./')

# SCHEMES = ['NegotiaToR', 'PIM']
# SCHEMES = ['NegotiaToR-8uplinks', 'benes-vlb1', 'benes-vlb1.5', 'benes-vlb2']
# SCHEMES = ['1', 'single_dst_grant']
# SCHEMES = ['100G', '200G', '300G', 'benes-vlb1']
# SCHEMES = ['1', '2', '3', '4', '5']
# SCHEMES = ['1', '2p', '3p', '4p', '5p']
# SCHEMES = ['benes/1_new', 'benes-vlb/1', 'benes/2_new', 'benes-vlb/2']
# SCHEMES = ['ITER_1', 'ITER_2', 'ITER_3', 'ITER_4', 'ITER_5', 'ITER_6', 'ITER_7']
# SCHEMES = ['50', '100', '150', '200', '250']
# SCHEMES = ['ITER_1', 'ITER_3', 'ITER_5', 'ITER_7']
# SCHEMES = ['NegotiaToR-iterative/tmp/1', 'NegotiaToR-iterative/tmp/2', 'NegotiaToR-iterative/tmp/3', 'NegotiaToR-iterative/tmp/4','NegotiaToR-iterative/tmp/5']
# SCHEMES = ['NegotiaToR/tmp/1', 'NegotiaToR/tmp/2', 'NegotiaToR/tmp/3', 'NegotiaToR/tmp/4','NegotiaToR/tmp/5']
# Pias = ['PIAS', 'No-PIAS']
Pias = ['PIAS']
# Topo = ['Benes', 'Big-Switch']
Topo = ['Benes']
Algo = ['NegotiaToR', 'VLB']
# Algo = ['VLB']
# Iter = ['ITER_1', 'ITER_2', 'ITER_3', 'ITER_4', 'ITER_5', 'ITER_6', 'ITER_7']
Iter = ['ITER_1']
Acc =  ['ACC_1', 'ACC_2', 'ACC_3', 'ACC_4', 'ACC_5']
# Acc =  ['ACC_5']
SCHEMES = Algo
# DATA_DIR_TEMP = '../DATA/NegotiaToR/{pias}/{scheme}/ACC_3/DATA_vote_{workload}_{load}_scheduled_{scheduled}/'
DATA_DIR_TEMP = '../DATA/PIAS/Big-Switch/{scheme}/ITER_1/ACC_2/DATA_vote_W4_{load}/'


FIG_FILE_NAME = WORKLOADS[0]
FIGURE_DIR = '../FIGS/'+ FIG_FILE_NAME +'/GOODPUT/'
if not os.path.exists(FIGURE_DIR):
    os.makedirs(FIGURE_DIR)

data = {}
for scheme in SCHEMES:
    data[scheme] = {}
    for pias in PIAS:
        data[scheme][pias] = {}
        for workload in WORKLOADS:
            data[scheme][pias][workload] = {}
            for load in LOADS:
                data[scheme][pias][workload][load] = {}
                for gossip in GOSSIP:
                    data[scheme][pias][workload][load][gossip] = {}
                    for scheduled in SCHEDULED:
                        data[scheme][pias][workload][load][gossip][scheduled] = {}
                    
                
for scheme in SCHEMES:
    for pias in PIAS:
        for workload in WORKLOADS:
            for load in LOADS:
                for gossip in GOSSIP:
                    for scheduled in SCHEDULED:
                        dir_path = DATA_DIR_TEMP.format(pias=pias, scheme=scheme, workload=workload, load=load, gossip=gossip, scheduled=scheduled)
                        data[scheme][pias][workload][load]['PATH'] = dir_path
                        for metric in METRICS:
                            data_path = dir_path + metric + '.txt'
                            data[scheme][pias][workload][load][gossip][scheduled][metric] = np.loadtxt(data_path)
                            print("LOADED: ", scheme, pias, workload, load, gossip, scheduled, metric)

for scheme in SCHEMES:
    for pias in PIAS:
        for workload in WORKLOADS:
            for load in LOADS:
                for gossip in GOSSIP:
                    for scheduled in SCHEDULED:
                        data[scheme][pias][workload][load][gossip][scheduled]['SHORT_IDX'] = data[scheme][pias][workload][load][gossip][scheduled]['FCT'][:, 4] < SHORT
                        data[scheme][pias][workload][load][gossip][scheduled]['LONG_IDX'] = data[scheme][pias][workload][load][gossip][scheduled]['FCT'][:, 4] > LONG
                        data[scheme][pias][workload][load][gossip][scheduled]['MIDDLE_IDX'] = (data[scheme][pias][workload][load][gossip][scheduled]['FCT'][:, 4] >= SHORT) * (data[scheme][pias][workload][load][gossip][scheduled]['FCT'][:, 4] <= LONG)

# WIDTH = 0.05  # the width of the bars


def slowdown_bar_plot(mode, labels, workload, flow_range='all'):

    results = {}
    for scheme in SCHEMES:
        results[scheme] = {}
        for pias in PIAS:
            results[scheme][pias] = []
            for load in LOADS:

                if flow_range == 'Mice':
                    idx = data[scheme][pias][workload][load][gossip][scheduled]['SHORT_IDX']
                elif flow_range == 'Elephant':
                    idx = data[scheme][pias][workload][load][gossip][scheduled]['LONG_IDX']
                elif flow_range == 'middle':
                    idx = data[scheme][pias][workload][load][gossip][scheduled]['MIDDLE_IDX']
                elif flow_range == 'all':
                    idx = np.arange(len(data[scheme][pias][workload][load][gossip][scheduled]['FCT']))

                available_idx = data[scheme][pias][workload][load][gossip][scheduled]['FCT'][:, 7] > 0 # 过滤未完成的流
                idx = idx * available_idx

                fct = data[scheme][pias][workload][load][gossip][scheduled]['FCT'][idx, 7] # fct

                if mode == 'Mean':
                    results[scheme][pias].append(np.mean(fct) * 1e3)
                elif mode == 'Median':
                    results[scheme][pias].append(np.percentile(fct, 50) * 1e3)
                elif mode == '99p':
                    results[scheme][pias].append(np.percentile(fct, 99) * 1e3)



    print(results)


    # SCHEMES_label = SCHEMES
    # SCHEMES_label = ['NegotiaToR(1x)', 'Benes-VLB(1x)', 'Benes-VLB(1.5x)', 'Benes-VLB(2x)']
    # SCHEMES_label = ['NegotiaToR', 'PIM']
    # SCHEMES_label = ['multi_dst_grant', 'single_dst_grant']
    # SCHEMES_label = ['100G', '200G', '300G', '400G']
    # SCHEMES_label = ['NegotiaToR(1x)', 'NegotiaToR(2x)', 'NegotiaToR(3x)', 'NegotiaToR(4x)', 'NegotiaToR(5x)']
    # SCHEMES_label = ['Sirius(1x)', 'Sirius(2x)', 'Sirius(3x)', 'Sirius(4x)', 'Sirius(5x)']
    SCHEMES_label = ['NegotiaToR(2x)', 'Traffic Oblivious(2x)']
    # SCHEMES_label = ['NegotiaToR(old)', 'NegotiaToR(new)', 'NegotiaToR(2x)', 'VLB(2x)']
    # SCHEMES_label = ['1-iterative', '3-iterative', '5-iterative', '7-iterative']
    # SCHEMES_label = ['ITER_1', 'ITER_2', 'ITER_3', 'ITER_4', 'ITER_5', 'ITER_6', 'ITER_7']
    # SCHEMES_label = ['VLB(1x)', 'VLB(2x)', 'VLB(3x)', 'VLB(4x)', 'VLB(5x)']


    for pias in PIAS:
        x_tick = np.arange(len(labels))*0.3 # the label locations
        x = x_tick - (len(SCHEMES)-1)*WIDTH/2

        # fig, ax = plt.subplots(figsize=my_figsize)
        fig, ax = plt.subplots(figsize=my_figsize)
        ax.grid(axis='y')
        hatches = ["", ".", "\\", "x", "*", "|", "o"]
        colors = ["white", "white", "white", "white", "white", "white", "white"]
        for i, scheme in enumerate(SCHEMES):
            # ax.bar(x + WIDTH*i, results[scheme][mode], WIDTH, label=scheme)
            # 一次画一个scheme的所有load的bar
            ax.bar(x + WIDTH*i, results[scheme][pias], WIDTH, edgecolor="black", label=SCHEMES_label[i], linewidth = 3, color=[colors[i]], hatch=hatches[i])


        

        if mode == "Mean":
            ax.set_ylabel('Avg. FCT of ' + flow_range + " (ms)", fontsize=my_fontsize)
        elif mode == "99p":
            ax.set_ylabel('99p FCT of ' + flow_range + " (ms)", fontsize=my_fontsize)
        else:
            ax.set_ylabel('FCT of ' + flow_range + " (ms)", fontsize=my_fontsize)
        # ax.set_xlabel("Incast Degree", fontsize=my_fontsize)
        # ax.set_title('Accelerate by adding line rate', fontsize=my_fontsize)
        ax.set_xlabel("Load (%)", fontsize=my_fontsize)
        ax.set_xticks(x_tick)

        plt.xticks(fontsize=my_fontsize)
        plt.yticks(fontsize=my_fontsize)


        ax.set_xticklabels(labels, fontsize=my_fontsize)

        # scientific_formatter = FuncFormatter(scientific)
        # ax.yaxis.set_major_formatter(scientific_formatter)
        # ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())

        # ax.set_yscale('log')
        ax.ticklabel_format( style='plain', axis='y')

        # ax.set_yscale('log')

        # ax.set_ylim([0.0001,1000])
        ax.legend(ncol=1, loc = "upper left", fontsize=30)
        # ax.set_yscale('log')
        # ax.legend(ncol=2, loc = "upper left", fontsize=my_fontsize-2, handlelength=1.5, borderpad = 0.2, labelspacing = 0.3, columnspacing = 1.0)

        figure_path = '../FIGS/'+ WORKLOADS[0] + '/comparison_fct_' + flow_range + '.pdf'
        plt.savefig(figure_path, dpi=300, bbox_inches='tight')

slowdown_bar_plot("Mean", labels, WORKLOADS[0], flow_range='Elephant')
# slowdown_bar_plot("Mean", labels, WORKLOADS[0], flow_range='all')
slowdown_bar_plot("99p", labels, WORKLOADS[0], flow_range='Mice')

def goodput_bar_plot(labels):
    results = {}
    i = 0
    for scheme in SCHEMES:
        results[scheme] = []
        i = i + 100
        for load in LOADS:
            idx = data[scheme][pias][workload][load][gossip][scheduled]['GOODPUT'][:, 2] > 0
            goodput = data[scheme][pias][workload][load][gossip][scheduled]['GOODPUT'][idx, 1] # goodput
            results[scheme].append(np.mean(goodput)/400)


    x_tick = np.arange(len(labels))*0.3 # the label locations
    x = x_tick - (len(SCHEMES)-1)*WIDTH/2

    # hatches = ["xxxx", "", "\\\\", "", "////"]
    # colors = ["white", "black", "white", "white", "white"]

    # schemes = ['Ideal', 'Zeropod', 'Fastpass', 'DCTCP']

    hatches = ["", ".", "\\", "x", "*", "|", "o"]
    colors = ["white", "white", "white", "white", "white", "white", "white"]

    # SCHEMES_label = SCHEMES
    # SCHEMES_label = ['NegotiaToR', 'Benes-VLB']
    # SCHEMES_label = ['NegotiaToR(1x)', 'Benes-VLB(1x)', 'Benes-VLB(1.5x)', 'Benes-VLB(2x)']
    # SCHEMES_label = ['multi_dst_grant', 'single_dst_grant']
    # SCHEMES_label = ['100G', '200G', '300G', '400G']
    # SCHEMES_label = ['NegotiaToR(1x)', 'NegotiaToR(2x)', 'NegotiaToR(3x)', 'NegotiaToR(4x)', 'NegotiaToR(5x)']
    # SCHEMES_label = ['Sirius(1x)', 'Sirius(2x)', 'Sirius(3x)', 'Sirius(4x)', 'Sirius(5x)']
    # SCHEMES_label = ['VLB(1x)', 'VLB(2x)', 'VLB(3x)', 'VLB(4x)', 'VLB(5x)']
    SCHEMES_label = ['NegotiaToR(2x)', 'VLB(2x)']
    # SCHEMES_label = ['NegotiaToR(old)', 'NegotiaToR(new)', 'NegotiaToR(2x)', 'VLB(2x)']
    # SCHEMES_label = ['1-iterative', '3-iterative', '5-iterative', '7-iterative']
    # SCHEMES_label = ['ITER_1', 'ITER_2', 'ITER_3', 'ITER_4', 'ITER_5', 'ITER_6', 'ITER_7']




    fig, ax = plt.subplots(figsize=my_figsize)
    
    for i, scheme in enumerate(SCHEMES):
        ax.bar(x + WIDTH*i, results[scheme], WIDTH, edgecolor="black", color=[colors[i]], label=SCHEMES_label[i], hatch=hatches[i], linewidth = 3)

    # ax.set_title('Accelerate by adding line rate', fontsize=my_fontsize)
    ax.set_ylabel('Normalized Goodput', fontsize=my_fontsize)
    # ax.set_ylabel('Goodput (Gbps)', fontsize=my_fontsize)
    ax.set_xticks(x_tick)
    # ax.set_xlabel("Incast Degree", fontsize=my_fontsize)
    ax.set_xlabel("Load (%)", fontsize=my_fontsize)
    ax.set_xticklabels(labels, fontsize=my_fontsize)
    ax.legend(ncol=1, loc = "upper left", fontsize=my_fontsize-2, handlelength = 1.5, borderpad = 0.2,  labelspacing = 0.3, columnspacing = 1.0)

    

    plt.xticks(fontsize=my_fontsize)
    plt.ylim((0, 1))
    plt.yticks(np.arange(0,1.01,0.1))
    ax.grid(axis="y")
    plt.yticks(fontsize=my_fontsize)

    figure_path = '../FIGS/'+ WORKLOADS[0] + '/goodput.pdf'
    plt.savefig(figure_path, dpi=300, bbox_inches='tight')

goodput_bar_plot(labels)