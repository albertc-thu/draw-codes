import numpy as np
from matplotlib import pyplot as plt

schemes = ['ost_2', 'ost_3', 'ost_4', 'ost_5', 'ost_6']
workloads = ["W5_0.1", "W5_0.25", "W5_0.5", "W5_0.75", "W5_1"]
metrics = ['FCT', 'GOODPUT']

labels = ['10', '25', '50', '75', '100']
my_figsize = [15, 10]
my_fontsize = 30
WIDTH = 0.05  # the width of the bars
SHORT = 10000 # 100KB
LONG = 10000000 # 1MB

data = {}
for scheme in schemes:
    data[scheme] = {}
    for workload in workloads:
        data[scheme][workload] = {}

for scheme in schemes:
    for workload in workloads:
        for metric in metrics:
            file_name = "../DATA/Zeropod/ost/{scheme}/DATA_zeropod_{workload}/{metric}.txt".format(scheme=scheme, workload=workload, metric=metric)
            data[scheme][workload][metric] = np.loadtxt(file_name)

for scheme in schemes:
        for workload in workloads:
            data[scheme][workload]['SHORT_IDX'] = data[scheme][workload]['FCT'][:, 4] < SHORT
            data[scheme][workload]['LONG_IDX'] = data[scheme][workload]['FCT'][:, 4] > LONG
            data[scheme][workload]['MIDDLE_IDX'] = (data[scheme][workload]['FCT'][:, 4] >= SHORT) * (data[scheme][workload]['FCT'][:, 4] <= LONG)


def fct_bar_plot(mode, labels, workload, flow_range='all'):

    results = {}
    for scheme in schemes:
        results[scheme] = []
        for workload in workloads:

            if flow_range == 'Mice':
                idx = data[scheme][workload]['SHORT_IDX']
            elif flow_range == 'Elephant':
                idx = data[scheme][workload]['LONG_IDX']
            elif flow_range == 'middle':
                idx = data[scheme][workload]['MIDDLE_IDX']
            elif flow_range == 'all':
                idx = np.arange(len(data[scheme][workload]['FCT']))

            available_idx = data[scheme][workload]['FCT'][:, 7] > 0 # 过滤未完成的流
            idx = idx * available_idx

            fct = data[scheme][workload]['FCT'][idx, 7] # fct

            if mode == 'Mean':
                results[scheme].append(np.mean(fct) * 1e3)
            elif mode == 'Median':
                results[scheme].append(np.percentile(fct, 50) * 1e3)
            elif mode == '99p':
                results[scheme].append(np.percentile(fct, 99) * 1e3)



    print(results)


    schemes_label = ['OST_2', 'OST_3', 'OST_4', 'OST_5', 'OST_6']



    x_tick = np.arange(len(labels))*0.3 # the label locations
    x = x_tick - (len(schemes)-1)*WIDTH/2

    # fig, ax = plt.subplots(figsize=my_figsize)
    fig, ax = plt.subplots(figsize=my_figsize)
    ax.grid(axis='y')
    hatches = ["", ".", "\\", "x", "*", "|", "o"]
    colors = ["white", "white", "white", "white", "white", "white", "white"]
    for i, scheme in enumerate(schemes):
        # ax.bar(x + WIDTH*i, results[scheme][mode], WIDTH, label=scheme)
        # 一次画一个scheme的所有load的bar
        ax.bar(x + WIDTH*i, results[scheme], WIDTH, edgecolor="black", label=schemes_label[i], linewidth = 3, color=[colors[i]], hatch=hatches[i])


        

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

        figure_path = '../FIGS/Zeropod/comparison_fct_' + flow_range + '.pdf'
        plt.savefig(figure_path, dpi=300, bbox_inches='tight')

fct_bar_plot("Mean", labels, workloads[0], flow_range='Elephant')
# slowdown_bar_plot("Mean", labels, WORKLOADS[0], flow_range='all')
fct_bar_plot("99p", labels, workloads[0], flow_range='Mice')

def goodput_bar_plot(labels):
    results = {}
    i = 0
    for scheme in schemes:
        results[scheme] = []
        i = i + 100
        for workload in workloads:
            idx = data[scheme][workload]['GOODPUT'][:, 2] > 0
            goodput = data[scheme][workload]['GOODPUT'][idx, 1] # goodput
            results[scheme].append(np.mean(goodput))


    x_tick = np.arange(len(labels))*0.3 # the label locations
    x = x_tick - (len(schemes)-1)*WIDTH/2

    # hatches = ["xxxx", "", "\\\\", "", "////"]
    # colors = ["white", "black", "white", "white", "white"]

    # schemes = ['Ideal', 'Zeropod', 'Fastpass', 'DCTCP']

    hatches = ["", ".", "\\", "x", "*", "|", "o"]
    colors = ["white", "white", "white", "white", "white", "white", "white"]

    schemes_label = ['OST_2', 'OST_3', 'OST_4', 'OST_5', 'OST_6']





    fig, ax = plt.subplots(figsize=my_figsize)
    
    for i, scheme in enumerate(schemes):
        ax.bar(x + WIDTH*i, results[scheme], WIDTH, edgecolor="black", color=[colors[i]], label=schemes_label[i], hatch=hatches[i], linewidth = 3)

    # ax.set_title('Accelerate by adding line rate', fontsize=my_fontsize)
    ax.set_ylabel('Normalized Goodput', fontsize=my_fontsize)
    # ax.set_ylabel('Goodput (Gbps)', fontsize=my_fontsize)
    ax.set_xticks(x_tick)
    # ax.set_xlabel("Incast Degree", fontsize=my_fontsize)
    ax.set_xlabel("Load (%)", fontsize=my_fontsize)
    ax.set_xticklabels(labels, fontsize=my_fontsize)
    ax.legend(ncol=1, loc = "upper left", fontsize=my_fontsize-2, handlelength = 1.5, borderpad = 0.2,  labelspacing = 0.3, columnspacing = 1.0)

    

    plt.xticks(fontsize=my_fontsize)
    # plt.ylim((0, 1))
    # plt.yticks(np.arange(0,1.01,0.1))
    ax.grid(axis="y")
    plt.yticks(fontsize=my_fontsize)

    figure_path = '../FIGS/Zeropod/goodput.pdf'
    plt.savefig(figure_path, dpi=300, bbox_inches='tight')

goodput_bar_plot(labels)

