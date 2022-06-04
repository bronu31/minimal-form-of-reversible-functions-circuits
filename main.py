import math
import time

import bulder as lb
import multiprocessing as mp
from multiprocessing import Process
import random as rd
import numpy

lib = lb.library_bulder(4)

test_dict = {"0": 0,
                     "1": 1,
                     "2": 2,
                     "3": 3,
                     "4": [0, 1, 2],
                     "5": [0, 1, 3],
                     "6": [0, 2, 3],
                     "7": [1, 0, 2],
                     "8": [1, 0, 3],
                     "9": [1, 2, 3],
                     "10": [2, 1, 0],
                     "11": [2, 0, 3],
                     "12": [2, 1, 3],
                     "13": [3, 1, 2],
                     "14": [3, 1, 0],
                     "15": [3, 2, 0]
                     }
diff_list=[[],[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]]]
Holder_of_Min_NumberCombos=[1313941673647,
    2789792421136,
    5606234750016,
    11212821043200,
    3237424,
    29727661,
    3876255609,
    592,
    3109,
    1959914985,
    16,
    1565,
    7620485,
    362881,
    7,
    121,
    0]



def factorize(holder):
    arr2 = []
    cout = 0
    for i in range(0, len(holder) - 1):
        for z in range(i, len(holder)):
            if holder[i] > holder[z]:
                cout += 1
        arr2.append(cout)
        cout = 0
    for z in range(0, len(arr2)):
        cout += arr2[z] * math.factorial(len(arr2) - z)
    return cout



def placer_and_calculator(lib,diff_element):
    lib.clear()

    for i in range(0, len(diff_element)):

        if 0 <= diff_element[i] <= 3:
            lib.place_Not(test_dict[str(diff_element[i])])
        else:
            lib.place_Toffoli(test_dict[str(diff_element[i])])
    arrr = [i for i in range(0, 16)]

    for j in arrr: arrr[j] = lib.calculate(j)
    return arrr

def parralel_placer(sub_diff_list,L):
    alef=[]
    sigma=[]
    fact=0
    for i in range(0,len(sub_diff_list)):
        for z in range(0,len(diff_list[1])):

            alef = [*sub_diff_list[i], *diff_list[1][z]]
            sigma=placer_and_calculator(lib,alef)
            fact=factorize(sigma)
            if fact in Holder_of_Min_NumberCombos:
                continue
            else: L.append([alef,sigma])
            Holder_of_Min_NumberCombos.append(fact)




if __name__ == '__main__':




    procs = []
    manager = mp.Manager()
    L = manager.list()
    #Pool_List = manager.list()

    sub_diff_list=[]
    f = open('all of 4 to eight.txt', 'w')
    start=time.time()
    while(True):
        print(time.time()-start, "Loop start")
        L[:] = []
        diff_list.append([])
        l = numpy.array_split(numpy.array(diff_list[-2]), 12)

        sub_diff_list.clear()
        for x in l:
            sub_diff_list.append([])
            for sigma in x.tolist():

                if len(sigma)==1:
                    sub_diff_list[-1].append(sigma)
                else:
                    sub_diff_list[-1].append(sigma)
        #print(sub_diff_list)
        #print(len(sub_diff_list))
        print(len(sub_diff_list[0][0]))
        procs.clear()
        for i in range(0, len(sub_diff_list)):
            proc = Process(target=parralel_placer, args=(sub_diff_list[i], L))
            procs.append(proc)
            proc.start()
        for proc in procs:
            proc.join()
        print(time.time() - start, "writing start")
        print()
        for i in L:
            f.write(str(i) +"\n")
            diff_list[-1].append(i[0])

        if len(diff_list[-1][-1])==8: break
    f.close()



