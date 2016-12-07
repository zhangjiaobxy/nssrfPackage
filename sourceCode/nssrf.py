# nssrf library

import os,sys,subprocess

########################################################################
# step 1: run mfinder to get subgraph feature OUT files
# input: ./data/rawData/
# output: ./data/mfinderFeature/*_subgraphSize_OUT.txt (mfinder output file)
# parameter: subgraphSize (subgraphSize = 2, 3, 4 or 234)
# callExample: nssrf.runMfinder(2)

def runMfinder(subgraphSize):
    cmd = 'python runMfinder.py ' + str(subgraphSize)
    os.system(cmd)

########################################################################
# step 2: featureExtract() function will extract subgraph features
# input: ./../data/mfinderFeature/*_OUT.txt
# output: ./../data/mfinderFeature/querySubgraphSize2.txt (querySubgraphSize3.txt, querySubgraphSize4.txt)
#         ./../data/mfinderFeature/dbSubgraphSize2.txt (dbSubgraphSize3.txt, dbSubgraphSize4.txt)
#         ./../data/mfinderFeature/querySubgraphSize2Feature.txt (querySubgraphSize3Feature.txt, querySubgraphSize4Feature.txt)
#         ./../data/mfinderFeature/dbSubgraphSize2Feature.txt (dbSubgraphSize3Feature.txt, dbSubgraphSize4Feature.txt)
#         ./../data/mfinderFeature/featureSize2.txt  (featureSize3.txt, featureSize4.txt)
# parameter: subgraphSize (subgraphSize = 2, 3, 4 or 234)
#            dbEnd: the end range of database
# callExample: nssrf.featureExtract(2,100)

def featureExtract(subgraphSize, dbEnd):
    cmd = 'python featureExtract.py ' + str(subgraphSize) + ' ' + str(dbEnd)
    print cmd
    os.system(cmd)

########################################################################
# step 3: run labelExtract to get label files
# input: ./data/rawData/
# output: /data/netalLabel (netal output file: *.eval files, netal_ec_label.txt, netal_lccs_label.txt)
#         /data/hubLabel (hubalign output file: *.eval files, hubalign_ec_label.txt, hubalign_lccs_label.txt)
# parameter: label (label = m1, m2, m3, m4;
#                  (note: m1: NETAL EC, m2: NETAL LCCS, m3: HubAlign EC, m4: HubAlign LCCS)
#            dbStart: the start range of database
#            dbEnd: the end range of database
#            queryStart: the start range of query networks
#            queryEnd: the end range of query networks
# callExample: nssrf.labelExtract('m1', 1, 100, 101, 110)

def labelExtract(label, dbStart, dbEnd, queryStart, queryEnd):
    if label == 'm1' or label == 'm2':
        os.system('bash runNetal.sh ' + str(dbStart) + ' ' + str(dbEnd) + ' ' + str(queryStart) + ' ' + str(queryEnd))
    elif label == 'm3' or label == 'm4':
        os.system('bash runHubalign.sh ' + str(dbStart) + ' ' + str(dbEnd) + ' ' + str(queryStart) + ' ' + str(queryEnd))
    else:
        print '\n*********************************************************************\n'
        print "Invalid label, system exit! "
        print '\n*********************************************************************\n'
        raise SystemExit

########################################################################
# step 4: get feature_lable csv file, it is the input csv file for random forest regression model
# input: ./../data/mfinderFeature/featureSize2.txt  (featureSize3.txt, featureSize2=4.txt)
#        ./../data/netalLabel/netal_ec_label.txt  (netal_lccs_label.txt, hubalign_ec_label.txt, hubalign_lccs_label.txt)
# output: ./../data/csvFeatureLabel/featureSize2_netal_ec_label.csv (...)
# parameter: subgraphSize (subgraphSize = 2, 3, 4 or 234)
#            label (label = m1, m2, m3, m4)
#                  (m1: NETAL EC, m2: NETAL LCCS, m3: HubAlign EC, m4: HubAlign LCCS)
# callExample: nssrf.csvFeatureLabel(2,'m1')

def csvFeatureLabel(subgraphSize, label):
    cmd = 'python csvFeatureLabel.py ' + str(subgraphSize) + ' '+ str(label)
    os.system(cmd)

########################################################################
# step 5: run random forest regression
# input: ./../data/csvFeatureLabel/featureSize2_netal_ec_label.csv (...)
# output: ./../data/output/topkNetwork.csv
# parameter: subgraphSize (subgraphSize = 2, 3, 4 or 234)
#            label (label = m1, m2, m3, m4)
#                  (m1: NETAL EC, m2: NETAL LCCS, m3: HubAlign EC, m4: HubAlign LCCS)
#            topk (output top k percent similar networks)
# callExample: nssrf.rfRegression(2,'m1',10)

def rfRegression(subgraphSize, label, topk):
    cmd = 'python rfRegression.py ' + str(subgraphSize) + ' '+ str(label) + ' ' + str(topk)
    os.system(cmd)

########################################################################
