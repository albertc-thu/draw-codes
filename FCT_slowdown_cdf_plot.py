from matplotlib import pyplot as plt
import numpy as np
import os
import sys
from matplotlib.ticker import FuncFormatter, MaxNLocator

os.chdir(sys.path[0])
os.chdir('../')

my_figsize = [11, 8]
my_fontsize = 26

NUM_BINS = 1000000

if len(sys.argv) >= 3:
    WORKLOAD = sys.argv[1]
    TYPE = sys.argv[2]
else:
    WORKLOAD = 'W4'
    PIAS = 'NO-PIAS'
    # TYPE = 'inpod'

SHORT = 100000 # 100KB
LONG = 10000000

# LOADS = ['0.1']
# LOADS = ['0.1', '0.25', '0.5', '0.75', '1']

# SCHEMES = ['ideal', 'fastpod', 'fastpass', 'dctcp']
SCHEMES = ['PIM', 'NegotiaToR']
LOADS = ['0.1', '0.25', '0.5', '0.75', '1']

GOSSIP =[300]

SCHEDULED = [30]

METRICS = ['FCT']

DATA_DIR_TEMP = './{pias}/{scheme}/DATA_vote_{workload}_{load}_gossip_{gossip}_scheduled_{scheduled}/'

FIGURE_DIR = './FIGURE/{workload}/FCT_slowdown/'.format(workload=WORKLOAD)
if not os.path.exists(FIGURE_DIR):
    os.makedirs(FIGURE_DIR)

# load data ----------------------------------------------------------------
data = {}
for scheme in SCHEMES:
    data[scheme] = {}
    for load in LOADS:
        data[scheme][load] = {}
        for gossip in GOSSIP:
            data[scheme][load][gossip] = {}
            for scheduled in SCHEDULED:
                data[scheme][load][gossip][scheduled] = {}

for scheme in SCHEMES:
    for load in LOADS:
        for gossip in GOSSIP:
            for scheduled in SCHEDULED:
                dir_path = DATA_DIR_TEMP.format(pias=PIAS, scheme=scheme, workload=WORKLOAD, load=load, gossip=gossip, scheduled=scheduled)
                data[scheme][load][gossip][scheduled]['PATH'] = dir_path
                for metric in METRICS:
                    data_path = dir_path + metric + '.txt'
                    data[scheme][load][gossip][scheduled][metric] = np.loadtxt(data_path)

                data[scheme][load][gossip][scheduled]['SHORT_IDX'] = data[scheme][load][gossip][scheduled]['FCT'][:, 4] < SHORT
                data[scheme][load][gossip][scheduled]['LONG_IDX'] = data[scheme][load][gossip][scheduled]['FCT'][:, 4] > LONG
                data[scheme][load][gossip][scheduled]['MIDDLE_IDX'] = (data[scheme][load][gossip][scheduled]['FCT'][:, 4] >= SHORT) * (data[scheme][load][gossip][scheduled]['FCT'][:, 4] <= LONG)


print("DATA LOADED!")

# linestyles = ['dotted', 'solid', 'dashed', (0, (3, 1, 1, 1))]
# labels = ['Ideal', 'Zeropod', 'Fastpass', 'DCTCP']
linestyles = ['dotted', 'solid', (0, (3, 1, 1, 1))]
# labels = ['Ideal', 'Zeropod', 'DCTCP']
labels = ['PIM', 'NegotiaToR']


def slowdown_cdf_plot(ax, load, flow_range='all'):
    counter = 0
    for scheme in SCHEMES:
        if flow_range == 'short':
            idx = data[scheme][load][gossip][scheduled]['SHORT_IDX']
        elif flow_range == 'long':
            idx = data[scheme][load][gossip][scheduled]['LONG_IDX']
        elif flow_range == 'middle':
            idx = data[scheme][load][gossip][scheduled]['MIDDLE_IDX']
        elif flow_range == 'all':
            idx = np.arange(len(data[scheme][load][gossip][scheduled]['FCT']))

        available_idx = data[scheme][load][gossip][scheduled]['FCT'][:, 7] > 0 # 过滤未完成的流
        idx = idx * available_idx

        slowdown = data[scheme][load][gossip][scheduled]['FCT'][idx, 5] # slowdown
        slowdown = np.insert(slowdown, 0, 0.999, axis=0)

        counts, bin_edges = np.histogram(slowdown, bins=NUM_BINS)
        cdf = np.cumsum(counts)
        ax.plot(bin_edges[:-1], cdf/len(slowdown), label=labels[counter], linewidth=5, linestyle=linestyles[counter], color = 'black')
        counter += 1

    ax.legend(loc='lower right', fontsize=my_fontsize-2, handlelength=4)

    # plot_vals = [10e-7, 10e-6, 10e-5, 10e-4]
    # label_vals = [1, 10, 100, 1000]

    ax.set_xscale('log')
    # ax.set_xticks(plot_vals) 
    # ax.set_xticklabels(label_vals) # relabeling the ticklabels

    ax.set_xlim(left=0.99)

    plt.xticks(fontsize=my_fontsize)
    plt.yticks(fontsize=my_fontsize)

    ax.set_xlabel('FCT Slowdown', fontsize=my_fontsize)
    ax.set_ylabel('CDF', fontsize=my_fontsize)
    ax.grid()


    figure_path = FIGURE_DIR + 'CDF_FCT_slowdown_{0}_{1}_flows.pdf'.format(load, flow_range)
    plt.savefig(figure_path, dpi=300, bbox_inches='tight')


for load in LOADS:
    fig, ax = plt.subplots(figsize=my_figsize)
    slowdown_cdf_plot(ax, load, 'short')

for load in LOADS:
    fig, ax = plt.subplots(figsize=my_figsize)
    slowdown_cdf_plot(ax, load, 'long')

for load in LOADS:
    fig, ax = plt.subplots(figsize=my_figsize)
    slowdown_cdf_plot(ax, load, 'middle')

for load in LOADS:
    fig, ax = plt.subplots(figsize=my_figsize)
    slowdown_cdf_plot(ax, load, 'all')