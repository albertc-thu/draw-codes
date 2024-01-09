import matplotlib.pyplot as plt
import numpy as np

fodegree = [2, 4, 6, 8, 10, 15, 20, 30, 40, 50]



# NegotiaToR_ratio = []
# workloads = ["fodegree_2", "fodegree_4", "fodegree_6", "fodegree_8", "fodegree_10", "fodegree_15", "fodegree_20", "fodegree_30", "fodegree_40", "fodegree_50"]
# # workloads = ["fodegree_2"]
# for w in workloads:
#   dir_name = "../DATA/NO-PIAS/NegotiaToR/DATA_vote_" + w + "_gossip_300_scheduled_20/"
#   file_name = "accept_ratio.txt"
#   file_path = dir_name + file_name
#   with open(file_path, 'r') as f:
#     for i in range(386):
#       line = f.readline()
#       line = line[:-1]
#       if i == 385:
#         tmp = line.split(": ")
#         data = float(tmp[1])
#         NegotiaToR_ratio.append(data)

# PIM_ratio = []
# workloads = ["fodegree_2", "fodegree_4", "fodegree_6", "fodegree_8", "fodegree_10", "fodegree_15", "fodegree_20", "fodegree_30", "fodegree_40", "fodegree_50"]
# # workloads = ["fodegree_2"]
# for w in workloads:
#   dir_name = "../DATA/NO-PIAS/PIM/DATA_vote_" + w + "_gossip_300_scheduled_20/"
#   file_name = "accept_ratio.txt"
#   file_path = dir_name + file_name
#   with open(file_path, 'r') as f:
#     for i in range(386):
#       line = f.readline()
#       line = line[:-1]
#       if i == 385:
#         tmp = line.split(": ")
#         data = float(tmp[1])
#         PIM_ratio.append(data)

# # print(PIM_ratio)

# plt.figure(1)
# plt.plot(fodegree, NegotiaToR_ratio, color = 'r', marker = 'o', linestyle = 'solid', label = "NegotiaToR PIM")
# plt.plot(fodegree, PIM_ratio, color = 'b', marker = 'o', linestyle = 'solid', label = "Traditional PIM")
# plt.xlabel("Degree (Uniform Load)", fontsize=13)
# plt.ylabel("Match Ratio", fontsize=13)
# plt.xlim((0, 50))
# plt.ylim((0.4, 1))
# plt.legend(loc = 'upper right')
# plt.savefig("../FIGS/match ratio/match ratio.pdf")



# ratio_improvement = np.array(NegotiaToR_ratio) / np.array(PIM_ratio) - 1
# # print(NegotiaToR_ratio)
# # print(PIM_ratio)
# # print(ratio_improvement)

# plt.figure(2)
# plt.plot(fodegree, ratio_improvement, color = 'orange', marker = 'o', linestyle = 'solid', label = "match ratio improvement")
# plt.xlabel("Degree (Uniform Load)", fontsize=13)
# plt.ylabel("Match Ratio Improvement", fontsize=13)
# plt.xlim((0, 50))
# plt.ylim((0, 0.2))
# # plt.legend(loc = 'upper right')
# plt.savefig("../FIGS/match ratio/match ratio improvement.pdf")




# #####################################################################
# #####################################################################

# # fanout only
# # workloads = ["fodegree_2", "fodegree_4", "fodegree_6", "fodegree_8", "fodegree_10", "fodegree_15", "fodegree_20", "fodegree_30", "fodegree_40", "fodegree_50"]
# workloads = ["fofodegree_2","fofodegree_4", "fofodegree_6", "fofodegree_8", "fofodegree_10", "fofodegree_15", "fofodegree_20", "fofodegree_30", "fofodegree_40", "fofodegree_50"]
# # workloads = ["foindegree_2","foindegree_4", "foindegree_6", "foindegree_8", "foindegree_10", "foindegree_15", "foindegree_20", "foindegree_30", "foindegree_40", "foindegree_50"]
# # workloads = ["fodegree_2"]
# NegotiaToR_ratio = []
# for w in workloads:
#   dir_name = "../DATA/NO-PIAS/NegotiaToR/DATA_vote_" + w + "_gossip_300_scheduled_20/"
#   file_name = "accept_ratio.txt"
#   file_path = dir_name + file_name
#   with open(file_path, 'r') as f:
#     for i in range(386):
#       line = f.readline()
#       line = line[:-1]
#       if i == 385:
#         tmp = line.split(": ")
#         data = float(tmp[1])
#         NegotiaToR_ratio.append(data)

# PIM_ratio = []
# # workloads = ["fodegree_2", "fodegree_4", "fodegree_6", "fodegree_8", "fodegree_10", "fodegree_15", "fodegree_20", "fodegree_30", "fodegree_40", "fodegree_50"]
# workloads = ["fofodegree_2","fofodegree_4", "fofodegree_6", "fofodegree_8", "fofodegree_10", "fofodegree_15", "fofodegree_20", "fofodegree_30", "fofodegree_40", "fofodegree_50"]
# # workloads = ["foindegree_2","foindegree_4", "foindegree_6", "foindegree_8", "foindegree_10", "foindegree_15", "foindegree_20", "foindegree_30", "foindegree_40", "foindegree_50"]
# # workloads = ["fodegree_2"]
# for w in workloads:
#   dir_name = "../DATA/NO-PIAS/PIM/DATA_vote_" + w + "_gossip_300_scheduled_20/"
#   file_name = "accept_ratio.txt"
#   file_path = dir_name + file_name
#   with open(file_path, 'r') as f:
#     for i in range(386):
#       line = f.readline()
#       line = line[:-1]
#       if i == 385:
#         tmp = line.split(": ")
#         data = float(tmp[1])
#         PIM_ratio.append(data)



# plt.figure(3)
# plt.plot(fodegree, NegotiaToR_ratio, color = 'r', marker = 'o', linestyle = 'solid', label = "NegotiaToR PIM")
# plt.plot(fodegree, PIM_ratio, color = 'b', marker = 'o', linestyle = 'solid', label = "Traditional PIM")
# plt.xlabel("Fanout Degree (No Incast)", fontsize=13)
# plt.ylabel("Match Ratio", fontsize=13)
# plt.xlim((0, 50))
# plt.ylim((0.4, 1))
# plt.legend(loc = 'upper right')
# plt.savefig("../FIGS/match ratio/fo match ratio.pdf")



# ratio_improvement = np.array(NegotiaToR_ratio) / np.array(PIM_ratio) - 1
# # print(NegotiaToR_ratio)
# # print(PIM_ratio)
# # print(ratio_improvement)

# plt.figure(4)
# plt.plot(fodegree, ratio_improvement, color = 'orange', marker = 'o', linestyle = 'solid', label = "match ratio improvement")
# plt.xlabel("Fanout Degree (No Incast)", fontsize=13)
# plt.ylabel("Match Ratio Improvement", fontsize=13)
# plt.xlim((0, 50))
# plt.ylim((-0.1, 0.2))
# plt.hlines(0, 0, 50, colors='k')
# # plt.legend(loc = 'upper right')
# plt.savefig("../FIGS/match ratio/fo match ratio improvement.pdf")




#####################################################################
#####################################################################


# incast only
# workloads = ["fodegree_2", "fodegree_4", "fodegree_6", "fodegree_8", "fodegree_10", "fodegree_15", "fodegree_20", "fodegree_30", "fodegree_40", "fodegree_50"]
# workloads = ["fofodegree_2","fofodegree_4", "fofodegree_6", "fofodegree_8", "fofodegree_10", "fofodegree_15", "fofodegree_20", "fofodegree_30", "fofodegree_40", "fofodegree_50"]
workloads = ["foindegree_2","foindegree_4", "foindegree_6", "foindegree_8", "foindegree_10", "foindegree_15", "foindegree_20", "foindegree_30", "foindegree_40", "foindegree_50"]
workloads = ["W4_0.1", "W4_0.25", "W4_0.5", "W4_0.75", "W4_1"]
NegotiaToR_ratio = []
for w in workloads:
  dir_name = "../DATA/PIAS/Big-Switch/NegotiaToR/ITER_1/ACC_2_no_prop_delay/DATA_vote_" + w + "/"
  file_name = "accept_ratio.txt"
  file_path = dir_name + file_name
  with open(file_path, 'r') as f:
    for i in range(386):
      line = f.readline()
      line = line[:-1]
      if i == 385:
        tmp = line.split(": ")
        data = float(tmp[1])
        NegotiaToR_ratio.append(data)

PIM_ratio = []
# workloads = ["fodegree_2", "fodegree_4", "fodegree_6", "fodegree_8", "fodegree_10", "fodegree_15", "fodegree_20", "fodegree_30", "fodegree_40", "fodegree_50"]
# workloads = ["fofodegree_2","fofodegree_4", "fofodegree_6", "fofodegree_8", "fofodegree_10", "fofodegree_15", "fofodegree_20", "fofodegree_30", "fofodegree_40", "fofodegree_50"]
# workloads = ["foindegree_2","foindegree_4", "foindegree_6", "foindegree_8", "foindegree_10", "foindegree_15", "foindegree_20", "foindegree_30", "foindegree_40", "foindegree_50"]
workloads = ["W4_0.1", "W4_0.25", "W4_0.5", "W4_0.75", "W4_1"]
# workloads = ["fodegree_2"]
for w in workloads:
  dir_name = "../DATA/PIAS/Big-Switch/ProjrcToR/ITER_1/ACC_2_no_prop_delay/DATA_vote_" + w + "/"
  file_name = "accept_ratio.txt"
  file_path = dir_name + file_name
  with open(file_path, 'r') as f:
    for i in range(386):
      line = f.readline()
      line = line[:-1]
      if i == 385:
        tmp = line.split(": ")
        data = float(tmp[1])
        PIM_ratio.append(data)



plt.figure(5)
plt.plot(fodegree, NegotiaToR_ratio, color = 'r', marker = 'o', linestyle = 'solid', label = "NegotiaToR")
plt.plot(fodegree, PIM_ratio, color = 'b', marker = 'o', linestyle = 'solid', label = "ProjrcToR")
plt.xlabel("Incast Degree (No Fanout)", fontsize=13)
plt.ylabel("Match Ratio", fontsize=13)
plt.xlim((0, 50))
plt.ylim((0.4, 1))
plt.legend(loc = 'upper right')
plt.savefig("../FIGS/match ratio/NegotiaToR_ProjecToR.pdf")



ratio_improvement = np.array(NegotiaToR_ratio) / np.array(PIM_ratio) - 1
# print(NegotiaToR_ratio)
# print(PIM_ratio)
# print(ratio_improvement)

plt.figure(6)
plt.plot(fodegree, ratio_improvement, color = 'orange', marker = 'o', linestyle = 'solid', label = "match ratio improvement")
plt.xlabel("Incast Degree (No Fanout)", fontsize=13)
plt.ylabel("Match Ratio Improvement", fontsize=13)
plt.xlim((0, 50))
plt.ylim((0, 0.4))
# plt.legend(loc = 'upper right')
# plt.savefig("../FIGS/match ratio/in match ratio improvement.pdf")



# fct1 = [7.415, 7.587, 7.662, 7.626, 7.644, 8.079, 8.712, 10.05, 11.66, 12.44]
# fct2 = [7.453, 7.78, 8.202, 8.299, 8.552, 9.045, 9.749, 11.74, 13, 13.43]

# plt.figure(1)
# plt.plot(fodegree, fct1, color = 'r', marker = 'o', linestyle = 'solid', label = "NegotiaToR PIM")
# plt.plot(fodegree, fct2, color = 'b', marker = 'o', linestyle = 'solid', label = "Traditional PIM")
# plt.xlabel("incast degree (no fanout)", fontsize=13)
# plt.ylabel(r'FCT ($\mu$s)', fontsize=13)
# plt.xlim((0, 50))
# # plt.ylim((0.4, 1))
# plt.legend(loc = 'upper left')
# plt.savefig("../FIGS/match ratio/in FCT.pdf")



# fct_improvement = 1 - np.array(fct1) / np.array(fct2)
# # print(NegotiaToR_ratio)
# # print(PIM_ratio)
# # print(ratio_improvement)

# plt.figure(2)
# plt.plot(fodegree, fct_improvement, color = 'orange', marker = 'o', linestyle = 'solid', label = "FCT improvement")
# plt.xlabel("incast degree (no fanout)", fontsize=13)
# plt.ylabel("FCT improvement", fontsize=13)
# plt.xlim((0, 50))
# # plt.ylim((0, 0.4))
# plt.legend(loc = 'upper right')
# plt.savefig("../FIGS/match ratio/in FCT improvement.pdf")
