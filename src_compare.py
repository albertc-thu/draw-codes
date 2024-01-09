import numpy as np
import matplotlib.pyplot as plt


# workloads = ["foindegree_2","foindegree_4", "foindegree_6", "foindegree_8", "foindegree_10", "foindegree_15", "foindegree_20", "foindegree_30", "foindegree_40", "foindegree_50"]
workloads = ["uniformincast_2", "uniformincast_4", "uniformincast_6", "uniformincast_8", "uniformincast_10", "uniformincast_15", "uniformincast_20", "uniformincast_30", "uniformincast_40", "uniformincast_50"]
fodegree = [2, 4, 6, 8, 10, 15, 20, 30, 40, 50]

src_delay_negotiaor = []
for w in workloads:
  file_name = "../DATA/NO-PIAS/NegotiaToR/incast/DATA_vote_"+ w + "_gossip_300_scheduled_20/src_delay.txt"
  total = 0
  cnt = 0
  with open(file_name, 'r') as f:
    data = f.readlines()
    for item in data:
      item = item.strip('\n')
      total += int(item)
      cnt += 1
    src_delay_negotiaor.append(total/cnt/1000)
print(src_delay_negotiaor)

src_delay_pim = []
for w in workloads:
  file_name = "../DATA/NO-PIAS/benes-vlb/incast/DATA_vote_"+ w + "_gossip_300_scheduled_20/src_delay.txt"
  total = 0
  cnt = 0
  with open(file_name, 'r') as f:
    data = f.readlines()
    for item in data:
      item = item.strip('\n')
      total += int(item)
      cnt += 1
    src_delay_pim.append(total/cnt / 1000)
print(src_delay_pim)



improvement = 1 - np.array(src_delay_negotiaor) / np.array(src_delay_pim)
print(improvement)

plt.figure(1)

plt.plot(fodegree, src_delay_negotiaor, color = 'r', marker = 'o', linestyle = 'solid', label = "NegotiaToR")
plt.plot(fodegree, src_delay_pim, color = 'b', marker = 'o', linestyle = 'solid', label = "Sirius")
plt.xlabel("Incast Degree ", fontsize=13)
plt.ylabel(r'Src Delay ($\mu$s)', fontsize=13)
plt.xlim((0, 50))
# plt.ylim((0.4, 1))
plt.legend(loc = 'upper left')
plt.savefig("../FIGS/uniformincast/src delay/src delay.pdf")





plt.figure(2)
plt.plot(fodegree, improvement, color = 'orange', marker = 'o', linestyle = 'solid', label = "Src Delay Improvement")
plt.xlabel("Incast Degree", fontsize=13)
plt.ylabel("Src Delay Improvement", fontsize=13)
plt.xlim((0, 50))
# plt.ylim((0, 0.2))
plt.legend(loc = 'upper right')
plt.savefig("../FIGS/uniformincast/src delay/src delay improvement.pdf")





# workloads = ["fodegree_2","fodegree_4", "fodegree_6", "fodegree_8", "fodegree_10", "fodegree_15", "fodegree_20", "fodegree_30", "fodegree_40", "fodegree_50"]
# fodegree = [2, 4, 6, 8, 10, 15, 20, 30, 40, 50]

# src_delay_negotiaor = []
# for w in workloads:
#   file_name = "../DATA/NegotiaToR/DATA_vote_"+ w + "_gossip_300_scheduled_20/src_delay.txt"
#   total = 0
#   with open(file_name, 'r') as f:
#     data = f.readlines()
#     for item in data:
#       item = item.strip('\n')
#       total += int(item)
#     src_delay_negotiaor.append(total)
# print(src_delay_negotiaor)

# src_delay_pim = []
# for w in workloads:
#   file_name = "../DATA/PIM/DATA_vote_"+ w + "_gossip_300_scheduled_20/src_delay.txt"
#   total = 0
#   with open(file_name, 'r') as f:
#     data = f.readlines()
#     for item in data:
#       item = item.strip('\n')
#       total += int(item)
#     src_delay_pim.append(total)
# print(src_delay_pim)



# improvement = 1 - np.array(src_delay_negotiaor) / np.array(src_delay_pim)
# print(improvement)

# plt.figure(2)
# plt.plot(fodegree, improvement, color = 'orange', marker = 'o', linestyle = 'solid', label = "src delay improvement")
# plt.xlabel("fanout degree", fontsize=13)
# plt.ylabel("src delay improvement", fontsize=13)
# plt.xlim((0, 50))
# plt.ylim((0, 0.2))
# plt.legend(loc = 'upper right')
# plt.savefig("../FIGS/src delay/src delay improvement(fanout).pdf")






# workloads = ["fofodegree_2","fofodegree_4", "fofodegree_6", "fofodegree_8", "fofodegree_10", "fofodegree_15", "fofodegree_20", "fofodegree_30", "fofodegree_40", "fofodegree_50"]
# fodegree = [2, 4, 6, 8, 10, 15, 20, 30, 40, 50]

# src_delay_negotiaor = []
# for w in workloads:
#   file_name = "../DATA/NegotiaToR/DATA_vote_"+ w + "_gossip_300_scheduled_20/src_delay.txt"
#   total = 0
#   with open(file_name, 'r') as f:
#     data = f.readlines()
#     for item in data:
#       item = item.strip('\n')
#       total += int(item)
#     src_delay_negotiaor.append(total)
# print(src_delay_negotiaor)

# src_delay_pim = []
# for w in workloads:
#   file_name = "../DATA/PIM/DATA_vote_"+ w + "_gossip_300_scheduled_20/src_delay.txt"
#   total = 0
#   with open(file_name, 'r') as f:
#     data = f.readlines()
#     for item in data:
#       item = item.strip('\n')
#       total += int(item)
#     src_delay_pim.append(total)
# print(src_delay_pim)



# improvement = 1 - np.array(src_delay_negotiaor) / np.array(src_delay_pim)
# print(improvement)

# plt.figure(3)
# plt.plot(fodegree, improvement, color = 'orange', marker = 'o', linestyle = 'solid', label = "src delay improvement")
# plt.xlabel("degree(uniform)", fontsize=13)
# plt.ylabel("src delay improvement", fontsize=13)
# plt.xlim((0, 50))
# plt.ylim((-0.1, 0.2))
# plt.hlines(0, 0, 50, colors='k')
# plt.legend(loc = 'upper right')
# plt.savefig("../FIGS/src delay/src delay improvement(uniform).pdf")

