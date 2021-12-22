from NanoAOD_Gen_Samples import sampleList_2016, sampleList_2017, sampleList_2018
from getFilesFromDisk import getFileList_DAS, getNEvents_DAS, getFileList_EOS

for year in [2016,2017,2018]:
    splitJobs = {}
    print '--------------------------'
    print  year 
    print  "nEvents\t  Samples"
    print '--------------------------'
    line = ""
    sampleListTmp = eval("sampleList_%i"%year)
    sampleList = sorted(sampleListTmp.items())
    for sampleName, sample in sampleList:
        nevents = getNEvents_DAS(sample)
        print("%s  %s"%(nevents,sample))
    print '=================='

 
