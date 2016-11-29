#!/usr/bin/env python
# -*- coding: utf-8 -*-

# *********************************************************************
# run mfinder to get subgraph feature OUT files
# *********************************************************************

# import the modules needed to run the script
import os, sys, subprocess

# subgraph size(2,3,4,234)
subgraphSize = str(sys.argv[1]) 

# number of parrallel subprocess 
thread_num = 8  

# valid subgraph size
validSize=['2','3','4','234']
if subgraphSize in validSize:
    print '\n*********************************************************************\n'
    print "Subgraph size: ",subgraphSize,' is valid!'
    print '\n*********************************************************************\n'
else:
    print '\n*********************************************************************\n'
    print "Invalid subgraph size, system exit! "
    print '\n*********************************************************************\n'
    raise SystemExit

# create mfinder feature folder
if not os.path.exists('./../data/mfinderFeature/'):  
    os.makedirs('./../data/mfinderFeature/')

# subgraph size 234 is the combination of subgraph size 2, 3 and 4
if subgraphSize == '234':  
    runSize = ['2','3','4']
else:
    runSize = [subgraphSize]

# run each size of subgraph
for e_subgraphSize in runSize:  
    thread_list = []
    file_list = os.listdir("./../data/rawData/")

    # mfinder command line
    cmd_temp = "./mfinder [FILENAME] -s " + str(e_subgraphSize) +" -r 0 -f [OUTNAME]"+ "_" + str(e_subgraphSize)  

    temp_file_list = []
    for file in file_list:
        if not file.endswith(".txt"):
            continue
        if file.endswith("_OUT.txt"):
            continue
        if file.replace(".txt", "") + "_" + str(e_subgraphSize) + "_OUT.txt" in file_list:
            continue
        temp_file_list.append(file)
    file_list = temp_file_list

    while len(file_list) > 0:
        if len(thread_list) < thread_num:
            file = file_list.pop()
            cmd = cmd_temp.replace("[FILENAME]", "./../data/rawData/"+file).replace("[OUTNAME]","./../data/mfinderFeature/"+file.replace(".txt",""))
            thread = subprocess.Popen(cmd, shell=True)
            thread_list.append(thread)
        else:
            for thread in thread_list:
                thread.poll()
                if thread.returncode != None:
                    thread_list.remove(thread)
                    break

    for thread in thread_list:
    	thread.communicate()

print '\n*********************************************************************\n'
print 'Congratulation! You have generated subgraph of size: ', subgraphSize
print '\n*********************************************************************\n'