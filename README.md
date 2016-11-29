nssrf 1.0 Python package - linux version
------------------------

nssrf 1.0 is a Python package.

This tool performs global network similarity search based on random forest regression with subgraph signatures.

This package includes nssrf 1.0 Python package and related scripts and files for the following paper:

NSSRF: global network similarity search with subgraph signatures and its applicaitons
(Jiao Zhang, Sam Kwong, Yuheng Jia and Ka-Chun Wong)


CONTAINS:
------------------------

* sourceCode : a folder contains nssrf 1.0 Python package related scripts and binaries. It has following files :

	* nssrf.py : nssrf 1.0 Python module

	* runMfinder.py : Python script to run mfinder and get subgaph raw data
	
	* featureExtract.py : Python script to extract subgraph features
	
	* mfinder : mfinder executable binary
	
	* runNetal.sh : shell scripts to run NETAL
	
	* runNetal.py : Python script to run NETAL and get label raw data
	
	* netalEC.py : Python script to extract NETAL EC label
	
	* netalLCCS.py : Python script to extract NETAL LCCS label
	
	* NETAL : NETAL executable binary
	
	* runHubalign.sh : shell script to run HubAlign
	
	* runHubalign.py : Python script to run HubAlign and get label raw data
	
	* hubalignEC.py : Python script to extract HubAlign EC label
	
	* hubalignLCCS.py : Python script to extract HubAlign LCCS label
	
	* HubAlign : HubAlign executable binary
	
	* csvFeatureLabel.py : Python script to generate a csv file, which contains final feature and label
	
	* rfRegression.py : Python script to call random forest regression, train the model and perform network query
	
* data : this folder stores all the data related to nssrf 1.0 Python package. It has following files :

	* rawData : it stores the input network txt files of nssrf 1.0 Python package, which exists in the initial stage
	
	* mfinderFeature : it stores subgraph output files of mfinder and raw subgraph raw features, which is created in the program execution stage
	
	* netalLabel : it stores output files of NETAL and HubAlign and raw labels, which is created in the program execution stage
	
	* csvFeatureLabel : it stores final feature label csv file, which is created in the program execution stage
	
	* output : it stores top k percent similar networks, which is created in the program execution stage

* LICENSE : MIT License

* README.md : this file


PREREQUISITE
------------------------

nssrf 1.0 Python package was tested by using Python 2.7.6 version on Ubuntu 14.04 LTS. Following Python packages should be installed:

* scipy

* numpy

* pandas

* scikit-learn


HOW TO USE
------------------------

* import nssrf 1.0 Python package
	
	$ cd /nssrfPackage/sourceCode

	$ import nssrf

* call functions in nssrf 1.0 Python package:

	$ nssrf.runMfinder(SUBGRAPH_SIZE)

	$ featureExtract(SUBGRAPH_SIZE)

	$ labelExtract(LABEL, DB_START, DB_END, QUERY_START, QUERY_END)

	$ csvFeatureLabel(SUBGRAPH_SIZE, LABEL)

	$ rfRegression(SUBGRAPH_SIZE, LABEL, TOP_K_PERCENT)
 
* Example:

	$ cd /nssrfPackage/sourceCode

	$ import nssrf

	$ nssrf.runMfinder(2)

	$ featureExtract(2)

	$ labelExtract('m1', 1, 100, 101, 110)

	$ csvFeatureLabel(2,'m1')

	$ rfRegression(2,'m1',10)

* Parameters:

	* [SUBGRAPH_SIZE] : 2, 3, 4 or 234 (234 indicates that feature is the combination of subgraph size 2, 3 and 4)

	* [LABEL] : m1, m2, m3 or m4 (m1: NETAL EC, m2: NETAL LCCS, m3: HubAlign EC, m4: HubAlign LCCS)

	* [TOP_K_PERCENT] : top k percent similar networks in the network database

	* [DB_START] : integer number, it should be the smallest file name in the database

	* [DB_END] : integer number, it should be the largest file name in the database

	* [QUERY_START] : integer number, it should be the smallest file name in the query network set

	* [QUERY_END] : integer number, it should be the largest file name in the query network set


FILE NAMING RULE
------------------------

* Input network file is named in the txt file format. File name is interger number. File name in the database should not have any interaction with the query set file name.

* For example, if there are 100 networks in the database and 10 query networks in the query set. Therefore, file names in the database should start from 1.txt to 100.txt. File names in the query set should start from 101.txt to 110.txt.


FILE FORMAT
------------------------

* Input network is in the txt file format, which has the following format: 

 Each line corresponds to an interaction and contains the name of two nodes and the edge weight of the corresponding interaction (separated by a tab).

 Here is an example for "network.txt" :

	1	2	1

	1	3	1

	2	3	1

	3	4	1

	1	4	1

* Output file is in the csv file format, which has the following format: 

 The output file returns top K similar networks against each query network. Each line contains the name of the query network, the name of similar netowrk in the database, label for regression and prediction of the similarity score (separated by a tab).

 Here is an example for the output file "topkNetwork.csv" :

	q_name	db_name	label	pred

	101	7	0.7	0.8

	101	79	0.9	0.9

	101	62	0.7	0.8

	101	35	0.4	0.6

	101	36	0.6	0.5


------------------------
Jiao Zhang

jiaozhang9-c@my.cityu.edu.hk

November 29 2016

