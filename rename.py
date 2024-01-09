import os

# Pias = ['PIAS', 'No-PIAS']
Pias = ['NO-PIAS']
# Topo = ['Benes', 'Big-Switch']
Topo = ['Big-Switch']
# Algo = ['NegotiaToR', 'VLB']
Algo = ['NegotiaToR']
Iter = ['ITER_1', 'ITER_2', 'ITER_3', 'ITER_4', 'ITER_5', 'ITER_6', 'ITER_7']
# Iter = ['ITER_1']
Acc =  ['ACC_1', 'ACC_2', 'ACC_3', 'ACC_4', 'ACC_5']
# Acc =  ['ACC_1']

for pias in Pias:
    for topo in Topo:
        for algo in Algo:
            for iter in Iter:
                for acc in Acc:
                    path = "./../DATA/{0}/{1}/{2}/{3}/{4}".format(pias, topo, algo, iter, acc)
                    fileList=os.listdir(path)
                    for file in fileList:
                        # print(file[:-5])
                        file = path+ os.sep + file
                        # print(file[:-13])
                        file_new = file[:-13]
                        os.rename(file, file_new) 

    



   