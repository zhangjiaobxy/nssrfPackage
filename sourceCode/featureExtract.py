#!/usr/bin/env python
# -*- coding: utf-8 -*-

# *********************************************************************
# featureExtract() function will extract subgraph features
# *********************************************************************

# import the modules needed to run the script
import os,sys

subgraphSize = str(sys.argv[1])  # subgraph size(2,3,4,234)
dbEnd = int(sys.argv[2])  # the end number of the database

# valid subgraph size
validSize=['2','3','4','234']
if subgraphSize in validSize:
    print '\n*********************************************************************\n'
    print "Subgraph size: ",subgraphSize,' is valid!\n'
else:
    print '\n*********************************************************************\n'
    print "Invalid subgraph size, system exit! "
    print '\n*********************************************************************\n'
    raise SystemExit

# subgraph size 234 is the combination of subgraph size 2, 3 and 4
if subgraphSize == '234':
    runSize = ['2','3','4']
else:
    runSize = [subgraphSize]

# subgraph size 2, 3 and 4 have 2, 13 and 199 types of subgraph, respectively
for e_subgraphSize in runSize:
    subgraphTypes = 0
    if e_subgraphSize == '2':
        subgraphTypes = 3   
    elif e_subgraphSize == '3': 
        subgraphTypes = 14  
    elif e_subgraphSize == '4':
        subgraphTypes = 200  

    # read feature from file
    def readfeature(filename):
        selectedFile=open(filename)
        line=selectedFile.readline()
        while line:
            if "Total number of 2-node subgraphs" in line:
                total=float(line.split()[-1])
            if "( Total num of different subgraphs size 2 is : 2 )" in line:
                line=selectedFile.readline()
                line=selectedFile.readline()
                line=selectedFile.readline()
                line=selectedFile.readline()
                while "(Application total runtime was:" not in line:
                    if len(line)>5:
                        print line.split()[0],float(line.split()[1])/total
                    line=selectedFile.readline()
            line=selectedFile.readline()
        selectedFile.close()

    # read each feature file in dir
    def Traversaldir(rootDir):
        list_dirs = os.walk(rootDir)
        for root, dirs, files in list_dirs:
            for f in files:
                if f[-9]=='2':
                    readfeature(os.path.join(root,f))

    rootDir='./../data/mfinderFeature/'  
    fwdb=open(rootDir+"dbSubgraphSize"+e_subgraphSize+".txt",'wb')
    fwquery=open(rootDir+"querySubgraphSize"+e_subgraphSize+".txt",'wb')

    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            # if f[-9] == 2:
            if f[-9]==e_subgraphSize:  
                dbnum=f.split('_')[0]
                netnum=int(dbnum.split('.')[0])
                if netnum<=dbEnd:
                    # fwdb.write(dbnum+'_network_2_out.txt')
                    fwdb.write(dbnum+'_network_'+e_subgraphSize+'_out.txt') 
                    fwdb.write('\t')
                    filename=os.path.join(root,f)
                    selectedFile=open(filename)
                    line=selectedFile.readline()
                    while line:
                        # if "Total number of 2-node subgraphs" in line:
                        if "Total number of "+e_subgraphSize+"-node subgraphs" in line:
                            total=float(line.split()[-1])
                        # if "( Total num of different subgraphs size 2 is : 2 )" in line:
                        if "( Total num of different subgraphs size "+e_subgraphSize+" is :" in line:
                            line=selectedFile.readline()
                            line=selectedFile.readline()
                            line=selectedFile.readline()
                            line=selectedFile.readline()
                            while "(Application total runtime was:" not in line:
                                if len(line)>5:
                                    fwdb.write(line.split()[0])
                                    fwdb.write(',')
                                    fwdb.write(str(float(line.split()[1])/total))
                                    fwdb.write('\t')
                                line=selectedFile.readline()
                        line=selectedFile.readline()
                    selectedFile.close()
                    fwdb.write('\n')
                if netnum>dbEnd:
                    # fwquery.write(dbnum+'_network_2_out.txt')
                    fwquery.write(dbnum+'_network_'+e_subgraphSize+'_out.txt')
                    fwquery.write('\t')
                    filename=os.path.join(root,f)
                    selectedFile=open(filename)
                    line=selectedFile.readline()
                    while line:
                        # if "Total number of 2-node subgraphs" in line:
                        if "Total number of "+e_subgraphSize+"-node subgraphs" in line:
                            total=float(line.split()[-1])
                        # if "( Total num of different subgraphs size 2 is : 2 )" in line:
                        if "( Total num of different subgraphs size "+e_subgraphSize+" is :" in line:
                            line=selectedFile.readline()
                            line=selectedFile.readline()
                            line=selectedFile.readline()
                            line=selectedFile.readline()
                            while "(Application total runtime was:" not in line:
                                if len(line)>5:
                                    fwquery.write(line.split()[0])
                                    fwquery.write(',')
                                    fwquery.write(str(float(line.split()[1])/total))
                                    fwquery.write('\t')
                                line=selectedFile.readline()
                        line=selectedFile.readline()
                    selectedFile.close()
                    fwquery.write('\n')
    fwdb.close()
    fwquery.close()

    ##########################################################################################################
    # read raw data feature for query networks and db networks, respectively
    def readRawData_featrue(fil2read,file2write):
        f = open(fil2read,"r")
        line = f.readline()
        dict2write={}
        while line:
            list2write=[]
            item0=line.split()[0]
            for x in range(1,subgraphTypes):
                item=line.split()[x]
                list2write.append(item.split(',')[1])
            dict2write[item0.split('_')[0]]=list2write
            line = f.readline()
        f.close()

        f = open(file2write,"wb")
        for key in dict2write:
            f.write(key)
            f.write(' ')
            for iter in dict2write[key]:
                f.write(iter)
                f.write(' ')
            f.write('\n')
        f.close()
    readRawData_featrue(rootDir+"querySubgraphSize"+e_subgraphSize+".txt",rootDir+"querySubgraphSize"+e_subgraphSize+"Feature.txt")
    readRawData_featrue(rootDir+"dbSubgraphSize"+e_subgraphSize+".txt",rootDir+"dbSubgraphSize"+e_subgraphSize+"Feature.txt")

    # combine the features of query network and db network 
    def combine_q_db_features(queryfile,netfile,file2write):
        fquery=open(queryfile)
        ftraining=open(netfile)
        ftrain = open(file2write,"wb")
        line1=fquery.readline()
        line2=ftraining.readline()
        traindict={}
        querydict={}
        while line2:
            line2split=line2.split(' ');
            traindict[line2split[0]]=line2split[1:subgraphTypes]
            line2=ftraining.readline()
        while line1:
            line1split=line1.split(" ")
            querydict[line1split[0]]=line1split[1:subgraphTypes]
            line1=fquery.readline()

        for keyquery in querydict:
            for keytrain in traindict:
                ftrain.write(keyquery)
                ftrain.write('\t')
                ftrain.write(keytrain)
                ftrain.write('\t')
                for iter in range(len(querydict[keyquery])):
                    list=querydict[keyquery]
                    ftrain.write(list[iter].strip())
                    ftrain.write('\t')
                # ftrain.write('\t')
                for iter in range(len(traindict[keytrain])):
                    list=traindict[keytrain]
                    ftrain.write(list[iter].strip())
                    ftrain.write('\t')
                ftrain.write('\n')

        fquery.close()
        ftraining.close()
        ftrain.close()
    combine_q_db_features(rootDir+"querySubgraphSize"+e_subgraphSize+"Feature.txt",rootDir+"dbSubgraphSize"+e_subgraphSize+"Feature.txt",rootDir+'featureSize'+e_subgraphSize+'.txt')

print 'Congratulation! You have generated features of subgraph of size: ', subgraphSize
print '\n*********************************************************************\n'
