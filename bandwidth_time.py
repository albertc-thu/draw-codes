import numpy as np
from matplotlib import pyplot as plt


workloads = ['W4_0.1', 'W4_0.25', 'W4_0.5', 'W4_0.75', 'W4_1']
workloads = ['W4_1']
host_to_observe = 73
sample_interval = 45
show_interval = 45
show_time = 30000
start_time = 100000
start_index = int(start_time/show_interval)
merge = int(show_interval/sample_interval)
for w in workloads:
    dir_name = "../DATA/Count_BW/DATA_vote_" + w
    Dst_filename = dir_name + '/RECEIVER_BANDWIDTH.txt'
    Trans_filename = dir_name + '/TRANSFER_BANDWIDTH.txt'

    Dst_bandwidth = np.loadtxt(Dst_filename, delimiter=" ", usecols=(host_to_observe-1,))
    Trans_bandwidth = np.loadtxt(Trans_filename, delimiter=" ", usecols=(host_to_observe-1,))
    Dst_bandwidth_new = np.zeros(int(len(Dst_bandwidth)/merge))
    Trans_bandwidth_new = np.zeros(int(len(Trans_bandwidth)/merge))
    # print(len(Trans_bandwidth))
    # print(int(len(Trans_bandwidth)/merge))
    # print(len(Dst_bandwidth))
    # print(int(len(Dst_bandwidth)/merge))
    for i in range(len(Dst_bandwidth_new)):
        Dst_bandwidth_new[i] = np.sum(Dst_bandwidth[i*merge : (i+1)*merge]) 
    for i in range(len(Trans_bandwidth_new)):
        Trans_bandwidth_new[i] = np.sum(Trans_bandwidth[i*merge : (i+1)*merge]) 
    Dst_bandwidth_new = Dst_bandwidth_new[start_index : start_index + int(show_time/show_interval)] *8/show_interval
    Trans_bandwidth_new = Trans_bandwidth_new[start_index : start_index + int(show_time/show_interval)] *8/show_interval
    time_stamp = np.arange(len(Dst_bandwidth_new)) * show_interval/1000 # 用us做单位
    # print(np.shape(Dst_bandwidth))
    # print(np.shape(time_stamp))
    # plt.scatter(time_stamp, Dst_bandwidth_new, s=5, c='r', label="Dst BW")
    plt.scatter(time_stamp, Trans_bandwidth_new, s=5, c='b', label="Trans BW")
    plt.xlabel(r"Time ($\mu$s)", fontsize=15)
    plt.ylabel("Bandwidth (Gbps)", fontsize=15)
    plt.legend(loc="upper left")
    # plt.ylim((0,500))
    plt.savefig("background.pdf")
