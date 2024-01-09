import numpy as np
from matplotlib import pyplot as plt

my_figsize = [11, 8]
my_fontsize = 26

NUM_BINS = 500000

workloads = ['W4_0.1', 'W4_0.25', 'W4_0.5', 'W4_0.75', 'W4_1']
workloads = ['W4_1']
host_to_observe = 73


dir_name = "../DATA/Count_BW_13/DATA_vote_" + workloads[0]
Dst_filename = dir_name + '/RECEIVER_BANDWIDTH.txt'
Trans_filename = dir_name + '/TRANSFER_BANDWIDTH.txt'

Dst_bandwidth = np.loadtxt(Dst_filename, delimiter=" ", usecols=(host_to_observe-1,))
Trans_bandwidth = np.loadtxt(Trans_filename, delimiter=" ", usecols=(host_to_observe-1,))

sample_interval = 13
show_interval = 104
# show_time = 10000
# start_time = 100000
# start_index = int(start_time/show_interval)
# start_index = 10000
merge = int(show_interval/sample_interval)
print(merge)
Dst_bandwidth_new = np.zeros(int(len(Dst_bandwidth)) - merge)
Trans_bandwidth_new = np.zeros(int(len(Trans_bandwidth)) - merge)

for i in range(len(Dst_bandwidth_new)):
    Dst_bandwidth_new[i] = np.sum(Dst_bandwidth[i : i + merge]) 
for i in range(len(Trans_bandwidth_new)):
    Trans_bandwidth_new[i] = np.sum(Trans_bandwidth[i : i + merge]) 

counts1, bin_edges1 = np.histogram(Dst_bandwidth, bins=NUM_BINS)
cdf1 = np.cumsum(counts1)
plt.plot(bin_edges1[:-1], cdf1/len(Dst_bandwidth), linewidth=5, color = 'black')

