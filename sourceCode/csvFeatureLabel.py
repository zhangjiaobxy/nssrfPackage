#!/usr/bin/env python
# -*- coding: utf-8 -*-

# *********************************************************************
# get feature_lable csv file,
# it is the input csv file for random forest regression model
#
# if you want to use scipy pacakge
# do:
# sudo apt-get install python-scipy
# pip install scipy
# *********************************************************************

# import the modules needed to run the script
import csv,os,sys
import pandas as pd
from scipy import spatial

subgraphSize = str(sys.argv[1])
metricLabel = sys.argv[2]

Size=['2','3','4','234']
if subgraphSize in Size:
    print '\n*********************************************************************\n'
    print "You have selected subgraph size " + subgraphSize + ' as your feature.\n'
else:
    print '\n*********************************************************************\n'
    print "Invalid subgraph size, system exit! "
    print '\n*********************************************************************\n'
    raise SystemExit

if metricLabel == 'm1':
    print 'You have selected \''+metricLabel+': NETAL EC\' as your label.\n'
    label_file = 'netal_ec_label.txt'
    flabel=open('./../data/netalLabel/'+label_file,'r')
elif metricLabel == 'm2':
    print 'You have selected \''+metricLabel+': NETAL LCCS\' as your label.\n'
    label_file = 'netal_lccs_label.txt'
    flabel=open('./../data/netalLabel/'+label_file,'r')
elif metricLabel == 'm3':
    print 'You have selected \''+metricLabel+': HubAlign EC\' as your label.\n'
    label_file = 'hubalign_ec_label.txt'
    flabel=open('./../data/hubLabel/'+label_file,'r')
elif metricLabel == 'm4':
    print 'You have selected \''+metricLabel+': HubAlign LCCS\' as your label.\n'
    label_file = 'hubalign_lccs_label.txt'
    flabel=open('./../data/hubLabel/'+label_file,'r')
else:
    print 'Invalid label, system exit!'
    print '\n*********************************************************************\n'
    raise SystemExit

line2=flabel.readline()
label=[]
while line2:
    label.append(float(line2.split('\t')[2]))
    line2=flabel.readline()
flabel.close()

if subgraphSize == '234':
    runSize = ['2','3','4']
else:
    runSize = [subgraphSize]

for e_subgraphSize in runSize:

    ffeature=open('./../data/mfinderFeature/featureSize'+e_subgraphSize+'.txt','r')

    if e_subgraphSize=='2':
        csvtitle=['q_name','db_name','q_id2','q_id6','db_id2','db_id6','cos_s2','label']
    if e_subgraphSize=='3':
        csvtitle=['q_name','db_name','q_id6','q_id12','q_id14','q_id36','q_id38','q_id46','q_id74','q_id78','q_id98','q_id102','q_id108','q_id110','q_id238','db_id6','db_id12','db_id14','db_id36','db_id38','db_id46','db_id74','db_id78','db_id98','db_id102','db_id108','db_id110','db_id238','cos_s3','label']
    if e_subgraphSize=='4':
        csvtitle=['q_name','db_name','q_id14','q_id28','q_id30','q_id74','q_id76','q_id78','q_id90','q_id92','q_id94','q_id204','q_id206','q_id222','q_id280','q_id282','q_id286','q_id328','q_id330','q_id332','q_id334','q_id344','q_id346','q_id348','q_id350','q_id390','q_id392','q_id394','q_id396','q_id398','q_id404','q_id406','q_id408','q_id410','q_id412','q_id414','q_id454','q_id456','q_id458','q_id460','q_id462','q_id468','q_id470','q_id472','q_id474','q_id476','q_id478','q_id856','q_id858','q_id862','q_id904','q_id906','q_id908','q_id910','q_id922','q_id924','q_id926','q_id972','q_id974','q_id990','q_id2184','q_id2186','q_id2190','q_id2202','q_id2204','q_id2206','q_id2252','q_id2254','q_id2270','q_id2458','q_id2462','q_id2506','q_id2510','q_id2524','q_id2526','q_id3038','q_id4370','q_id4374','q_id4382','q_id4418','q_id4420','q_id4422','q_id4424','q_id4426','q_id4428','q_id4430','q_id4434','q_id4436','q_id4438','q_id4440','q_id4442','q_id4444','q_id4446','q_id4546','q_id4548','q_id4550','q_id4556','q_id4558','q_id4562','q_id4564','q_id4566','q_id4572','q_id4574','q_id4678','q_id4682','q_id4686','q_id4692','q_id4694','q_id4698','q_id4700','q_id4702','q_id4740','q_id4742','q_id4748','q_id4750','q_id4758','q_id4764','q_id4766','q_id4812','q_id4814','q_id4830','q_id4946','q_id4950','q_id4952','q_id4954','q_id4958','q_id4994','q_id4998','q_id5002','q_id5004','q_id5006','q_id5010','q_id5012','q_id5014','q_id5016','q_id5018','q_id5020','q_id5022','q_id5058','q_id5062','q_id5064','q_id5066','q_id5068','q_id5070','q_id5074','q_id5076','q_id5078','q_id5080','q_id5082','q_id5084','q_id5086','q_id6342','q_id6348','q_id6350','q_id6356','q_id6358','q_id6364','q_id6366','q_id6550','q_id6552','q_id6554','q_id6558','q_id6598','q_id6602','q_id6604','q_id6606','q_id6614','q_id6616','q_id6618','q_id6620','q_id6622','q_id6854','q_id6858','q_id6862','q_id6870','q_id6874','q_id6876','q_id6878','q_id7126','q_id7128','q_id7130','q_id7134','q_id13142','q_id13146','q_id13148','q_id13150','q_id13260','q_id13262','q_id13278','q_id14678','q_id14686','q_id14790','q_id14798','q_id14810','q_id14812','q_id14814','q_id15258','q_id15262','q_id15310','q_id15326','q_id31710','db_id14','db_id28','db_id30','db_id74','db_id76','db_id78','db_id90','db_id92','db_id94','db_id204','db_id206','db_id222','db_id280','db_id282','db_id286','db_id328','db_id330','db_id332','db_id334','db_id344','db_id346','db_id348','db_id350','db_id390','db_id392','db_id394','db_id396','db_id398','db_id404','db_id406','db_id408','db_id410','db_id412','db_id414','db_id454','db_id456','db_id458','db_id460','db_id462','db_id468','db_id470','db_id472','db_id474','db_id476','db_id478','db_id856','db_id858','db_id862','db_id904','db_id906','db_id908','db_id910','db_id922','db_id924','db_id926','db_id972','db_id974','db_id990','db_id2184','db_id2186','db_id2190','db_id2202','db_id2204','db_id2206','db_id2252','db_id2254','db_id2270','db_id2458','db_id2462','db_id2506','db_id2510','db_id2524','db_id2526','db_id3038','db_id4370','db_id4374','db_id4382','db_id4418','db_id4420','db_id4422','db_id4424','db_id4426','db_id4428','db_id4430','db_id4434','db_id4436','db_id4438','db_id4440','db_id4442','db_id4444','db_id4446','db_id4546','db_id4548','db_id4550','db_id4556','db_id4558','db_id4562','db_id4564','db_id4566','db_id4572','db_id4574','db_id4678','db_id4682','db_id4686','db_id4692','db_id4694','db_id4698','db_id4700','db_id4702','db_id4740','db_id4742','db_id4748','db_id4750','db_id4758','db_id4764','db_id4766','db_id4812','db_id4814','db_id4830','db_id4946','db_id4950','db_id4952','db_id4954','db_id4958','db_id4994','db_id4998','db_id5002','db_id5004','db_id5006','db_id5010','db_id5012','db_id5014','db_id5016','db_id5018','db_id5020','db_id5022','db_id5058','db_id5062','db_id5064','db_id5066','db_id5068','db_id5070','db_id5074','db_id5076','db_id5078','db_id5080','db_id5082','db_id5084','db_id5086','db_id6342','db_id6348','db_id6350','db_id6356','db_id6358','db_id6364','db_id6366','db_id6550','db_id6552','db_id6554','db_id6558','db_id6598','db_id6602','db_id6604','db_id6606','db_id6614','db_id6616','db_id6618','db_id6620','db_id6622','db_id6854','db_id6858','db_id6862','db_id6870','db_id6874','db_id6876','db_id6878','db_id7126','db_id7128','db_id7130','db_id7134','db_id13142','db_id13146','db_id13148','db_id13150','db_id13260','db_id13262','db_id13278','db_id14678','db_id14686','db_id14790','db_id14798','db_id14810','db_id14812','db_id14814','db_id15258','db_id15262','db_id15310','db_id15326','db_id31710','cos_s4','label']
    line1=ffeature.readline()

    if not os.path.exists('./../data/csvFeatureLabel/'):
        os.makedirs('./../data/csvFeatureLabel/')

    with open('./../data/csvFeatureLabel/featureSize'+e_subgraphSize+'_'+label_file.replace('.txt','')+'.csv', 'wb') as csvfile:

        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(csvtitle)
        line1_iter=0
        while line1:
            if e_subgraphSize=='2':
                u=[float(line1.split()[2]),float(line1.split()[3])]
                v=[float(line1.split()[4]),float(line1.split()[5])]
                if sum(u)==0 or sum(v)==0:
                    cosditance=0
                else:
                    cosdistance=spatial.distance.cosine(u, v)
                row=line1.split()[0:6]
            if e_subgraphSize=='3':
                u=[]
                v=[]
                for i in range(13):
                    u.append(float(line1.split()[2+i]))
                    v.append(float(line1.split()[15+i]))
                if sum(u)==0 or sum(v)==0:
                    cosditance=0
                else:
                    cosdistance=spatial.distance.cosine(u, v)
                row=line1.split()[0:28]
            if e_subgraphSize=='4':
                u=[]
                v=[]
                for i in range(199):
                    u.append(float(line1.split()[2+i]))
                    v.append(float(line1.split()[201+i]))
                if sum(u)==0 or sum(v)==0:
                    cosditance=0
                else:
                    cosdistance=spatial.distance.cosine(u, v)
                row=line1.split()[0:400]
            floatrow=[]
            for i in range(len(row)):
                floatrow.append(float(row[i]))
            floatrow.append(1-cosdistance)
            floatrow.append(label[line1_iter]) # add label to the end of each row
            spamwriter.writerow(floatrow)
            line1=ffeature.readline()
            line1_iter=line1_iter+1
    ffeature.close()

if subgraphSize == '234':
    dfs2 = pd.read_csv('./../data/csvFeatureLabel/featureSize2_'+label_file.replace('.txt','.csv'), skipinitialspace=True, delimiter=',')
    dfs3 = pd.read_csv('./../data/csvFeatureLabel/featureSize3_'+label_file.replace('.txt','.csv'), skipinitialspace=True, delimiter=',')
    dfs4 = pd.read_csv('./../data/csvFeatureLabel/featureSize4_'+label_file.replace('.txt','.csv'), skipinitialspace=True, delimiter=',')
    features2 = dfs2.columns[:(dfs2.shape[1]-1)]
    features3 = dfs3.columns[2:(dfs3.shape[1]-1)]
    features4 = dfs4.columns[2:(dfs4.shape[1])]
    dfs234 = pd.concat([dfs2[features2],dfs3[features3],dfs4[features4]],axis=1)
    dfs234.to_csv('./../data/csvFeatureLabel/featureSize234_'+label_file.replace('.txt','.csv'), header=True, index = False)  

print 'Congratulation! Final featureLabel csv file is generated successfully!'
print '\n*********************************************************************\n'