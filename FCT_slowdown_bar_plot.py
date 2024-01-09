from matplotlib import pyplot as plt
import numpy as np
import os
import sys

os.chdir(sys.path[0])
os.chdir('../')

my_figsize = [16, 8]
my_fontsize = 26

WIDTH = 0.05  # the width of the bars

WORKLOAD = 'W5'
TYPE = 'inpod'

SHORT = 100000 # 100KB
LONG = 10000000


# LOADS = ['0.1', '0.25', '0.5', '0.75', '1']
# labels = ['10', '25', '50', '75', '100'] # LOADS

LOADS = ['0.1', '0.25', '0.5', '0.75']
labels = ['10', '25', '50', '75'] # LOADS

# SCHEMES = ['ideal', 'fastpod', 'fastpass', 'dctcp']
SCHEMES = ['ideal', 'fastpod', 'dctcp']

METRICS = ['FCT']

DATA_DIR_TEMP = './DATA_{scheme}/DATA_{scheme}_{workload}_{load}/'

FIGURE_DIR = './FIGURE/{workload}/FCT_slowdown/'.format(workload=WORKLOAD)
if not os.path.exists(FIGURE_DIR):
    os.makedirs(FIGURE_DIR)

# load data ----------------------------------------------------------------
data = {}
for scheme in SCHEMES:
    data[scheme] = {}
    for load in LOADS:
        data[scheme][load] = {}

for scheme in SCHEMES:
    for load in LOADS:
        dir_path = DATA_DIR_TEMP.format(scheme=scheme, workload=WORKLOAD, type=TYPE, load=load)
        data[scheme][load]['PATH'] = dir_path
        for metric in METRICS:
            data_path = dir_path + metric + '.txt'
            data[scheme][load][metric] = np.loadtxt(data_path)

        data[scheme][load]['SHORT_IDX'] = data[scheme][load]['FCT'][:, 4] < SHORT
        data[scheme][load]['LONG_IDX'] = data[scheme][load]['FCT'][:, 4] > LONG
        data[scheme][load]['MIDDLE_IDX'] = (data[scheme][load]['FCT'][:, 4] >= SHORT) * (data[scheme][load]['FCT'][:, 4] <= LONG)


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
                idx = data[scheme][load]['SHORT_IDX']
            elif flow_range == 'long':
                idx = data[scheme][load]['LONG_IDX']
            elif flow_range == 'middle':
                idx = data[scheme][load]['MIDDLE_IDX']
            elif flow_range == 'all':
                idx = np.arange(len(data[scheme][load]['FCT']))

            available_idx = data[scheme][load]['FCT'][:, 7] > 0 # 过滤未完成的流
            idx = idx * available_idx

            slowdown = data[scheme][load]['FCT'][idx, 5] # slowdown
            if mode == 'Mean':
                results[scheme][mode].append(np.mean(slowdown))
            elif mode == 'Median':
                results[scheme][mode].append(np.percentile(slowdown, 50))
            elif mode == '99p':
                results[scheme][mode].append(np.percentile(slowdown, 99))

    x_tick = np.arange(len(labels))*0.3 # the label locations
    x = x_tick - (len(SCHEMES)-1)*WIDTH/2

    # hatches = ["xxxx", "", "", "////"]
    # colors = ["white", "black", "white", "white"]

    # schemes = ['Ideal', 'Zeropod', 'Fastpass', 'DCTCP']


    hatches = ["xxxx", "", "////"]
    colors = ["white", "black", "white"]

    schemes = ['Ideal', 'Zeropod', 'DCTCP']
    fig, ax = plt.subplots(figsize=my_figsize)
    ax.grid()
    for i, scheme in enumerate(SCHEMES):
        # ax.bar(x + WIDTH*i, results[scheme][mode], WIDTH, label=scheme)
        # 一次画一个scheme的所有load的bar
        ax.bar(x + WIDTH*i, results[scheme][mode], WIDTH, edgecolor="black", color=[colors[i]], label=schemes[i], hatch=hatches[i], linewidth = 3)

    ax.set_ylabel(mode + ' FCT Slowdown', fontsize=my_fontsize)
    ax.set_xlabel("Load (%)", fontsize=my_fontsize)
    ax.set_xticks(x_tick)

    plt.xticks(fontsize=my_fontsize)
    plt.yticks(fontsize=my_fontsize)

    ax.set_xticklabels(labels, fontsize=my_fontsize)
    # ax.set_ylim([0,3.0])
    # ax.legend(ncol=4, loc = "upper left", fontsize=20)
    ax.legend(ncol=2, loc = "upper left", fontsize=my_fontsize-2)

    figure_path = FIGURE_DIR + "BAR_" + mode + '_FCT_slowdown_' + flow_range + '.pdf'
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