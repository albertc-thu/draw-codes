import numpy as np
import matplotlib.pyplot as plt

# Incast_degree = [2, 4, 6, 8, 10, 12, 14, 16]
Incast_degree = [2, 4, 6, 8, 10, 15, 20, 30, 40, 50]
# Incast_degree = [2]
group = 20
workloads = 'uniformincast'
# SCHEMES = ['NegotiaToR-8uplinks', 'benes']
# SCHEMES = ['NegotiaToR', 'benes-vlb']
# SCHEMES = ['benes/incast_1', 'benes/incast_2', 'benes/incast_3', 'benes/incast_4', 'benes/incast_5', 'benes-vlb/incast_1', 'benes-vlb/incast_2', 'benes-vlb/incast_3', 'benes-vlb/incast_4', 'benes-vlb/incast_5']
# SCHEMES = ['NegotiaToR/incast_2', 'NegotiaToR/incast_3','NegotiaToR/incast_4','NegotiaToR/incast_5', 'PIM/incast_2', 'PIM/incast_3', 'PIM/incast_4', 'PIM/incast_5']
# SCHEMES = ['benes']
SCHEMES = ['NegotiaToR', 'benes']

fct = np.zeros([2 * group, len(Incast_degree)], dtype = float) 

for i, scheme in enumerate(SCHEMES): 
    for group_index in range(group):  
        for j, incast_degree in enumerate(Incast_degree):
            path_name = '../DATA/NO-PIAS/' + scheme + '/incast/incast_' + str(group_index) + '/DATA_vote_uniformincast_' + str(incast_degree) + '_gossip_300_scheduled_30/FCT.txt'
            print(path_name)
            data = np.array(np.loadtxt(path_name, delimiter=' ', dtype=float))
            # print(data)
            # print(data[:, -1])
            
            fct[i * group + group_index][j] = max(data[:, -1])
            # print("fct[{0}][{1}] = {2}".format(i, j, fct[i][j]))
            # print(type(data))
            # print(data.shape)

# print(fct)
fct = fct * 1e6
fct1 = fct[0:group, :]
fct2 = fct[group:2*group, :]

fct1_average = np.average(fct1, axis=0)
fct2_average = np.average(fct2, axis=0)
# print(fct1_average)
# print(fct2_average)
fct1_stdd = np.std(fct1,axis=0)
fct2_stdd = np.std(fct2,axis=0)
print(fct1_stdd)
print(fct2_stdd)
Labels = ['NegotiaToR', 'Benes-NegotiaToR']
# plt.plot(Incast_degree, fct1_average, color = 'r', marker = 'o', linestyle = 'solid', label = Labels[0])
# plt.plot(Incast_degree, fct2_average, color = 'b', marker = 'o', linestyle = 'solid', label = Labels[1])
plt.errorbar(Incast_degree,fct1_average,yerr=fct1_stdd,fmt='o-',ecolor='r',color='r',elinewidth=1,capsize=4,label = Labels[0])
plt.errorbar(Incast_degree,fct2_average,yerr=fct2_stdd,fmt='o-',ecolor='b',color='b',elinewidth=1,capsize=4,label = Labels[1])
plt.xlabel("Incast Degree", fontsize=13)
plt.ylabel(r'Incast Finish Time ($\mu$s)', fontsize=13)
# plt.xlim((0, 50))
# plt.ylim((0, 0.2))
plt.legend(loc = 'upper left')
plt.savefig("../FIGS/uniformincast/FCT/uniform incast finish time.pdf")


    