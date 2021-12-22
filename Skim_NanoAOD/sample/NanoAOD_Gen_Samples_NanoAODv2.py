#--------------------------
# 2016
#--------------------------
#MCType16='RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1'
#MCType16='RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1'
# MCType16v7='RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_backup_102X_mcRun2_asymptotic_v8-v1'

# MCType16_ext1=MCType16.replace('-v1','_ext1-v1')
# MCType16_ext2=MCType16.replace('-v1','_ext2-v1')
# MCType16_ext3=MCType16.replace('-v1','_ext3-v1')
# MCType16_noPULabel = MCType16.replace('PUMoriond17_','')
# MCType16_bkp= MCType16.replace('Nano25Oct2019_102X','Nano25Oct2019_backup_102X')
# MCType16_v2 = MCType16.replace('-v1','-v2')

# DataType16='Nano1June2019-v1'
# DataType16_ver2='_ver2-Nano1June2019_ver2-v1'

MCType16    = 'RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1'
MCType16_v2 = 'RunIISummer19UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1'

DataType16='UL2016_MiniAODv1_NanoAODv2-v1'
DataType16_hipm='HIPM_UL2016_MiniAODv1_NanoAODv2-v1'
DataType16_hipm_v2='ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1'
DataType16_v2 = DataType16.replace('-v1','-v2')

sampleList_2016 = {
# # 'HplusM080' : '/ChargedHiggsToCS_M080_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# # 'HplusM090' : '/ChargedHiggsToCS_M090_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# # 'HplusM100' : '/ChargedHiggsToCS_M100_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# # 'HplusM120' : '/ChargedHiggsToCS_M120_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# # 'HplusM140' : '/ChargedHiggsToCS_M140_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# # 'HplusM150' : '/ChargedHiggsToCS_M150_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# # 'HplusM155' : '/ChargedHiggsToCS_M155_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# # 'HplusM160' : '/ChargedHiggsToCS_M160_13TeV-madgraph/'+MCType16+'/NANOAODSIM',

'Data_SingleMu_b' : '/SingleMuon/Run2016B-'+DataType16_hipm_v2+'/NANOAOD',
'Data_SingleMu_c' : '/SingleMuon/Run2016C-'+DataType16+'/NANOAOD',
'Data_SingleMu_d' : '/SingleMuon/Run2016D-'+DataType16+'/NANOAOD',
'Data_SingleMu_e' : '/SingleMuon/Run2016E-'+DataType16+'/NANOAOD',
'Data_SingleMu_f' : '/SingleMuon/Run2016F-'+DataType16_hipm+'/NANOAOD',
'Data_SingleMu_g' : '/SingleMuon/Run2016G-'+DataType16+'/NANOAOD',
'Data_SingleMu_h' : '/SingleMuon/Run2016H-'+DataType16+'/NANOAOD',

'Data_SingleEle_b' : '/SingleElectron/Run2016B-'+DataType16_hipm_v2+'/NANOAOD',
'Data_SingleEle_c' : '/SingleElectron/Run2016C-'+DataType16+'/NANOAOD',
'Data_SingleEle_d' : '/SingleElectron/Run2016D-'+DataType16+'/NANOAOD',
'Data_SingleEle_e' : '/SingleElectron/Run2016E-'+DataType16_v2+'/NANOAOD',
'Data_SingleEle_f' : '/SingleElectron/Run2016F-'+DataType16_hipm+'/NANOAOD',
'Data_SingleEle_g' : '/SingleElectron/Run2016G-'+DataType16+'/NANOAOD',
'Data_SingleEle_h' : '/SingleElectron/Run2016H-'+DataType16+'/NANOAOD',

'TTbarPowheg_Dilepton' : '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Hadronic' : '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Semilept' : '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',

'TTbarPowheg_Dilepton_CP5up'           : '/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Dilepton_CP5down'         : '/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Dilepton_hdampup'         : '/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Dilepton_hdampdown'       : '/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Dilepton_mtop1695'        : '/TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Dilepton_mtop1755'        : '/TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',

'TTbarPowheg_Hadronic_CP5up'           : '/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Hadronic_CP5down'         : '/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Hadronic_hdampup'         : '/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Hadronic_hdampdown'       : '/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Hadronic_mtop1695'        : '/TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Hadronic_mtop1755'        : '/TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',

'TTbarPowheg_Semilept_CP5up'           : '/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Semilept_CP5down'         : '/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Semilept_hdampup'         : '/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Semilept_hdampdown'       : '/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Semilept_mtop1695'        : '/TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'TTbarPowheg_Semilept_mtop1755'        : '/TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',

'W1jets'      : '/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'W2jets'      : '/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'W3jets'      : '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'W4jets'      : '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',

'DYjetsM10to50' : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',
'DYjetsM50_ext1' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType16+'/NANOAODSIM',

'ST_s_channel' : '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType16+'/NANOAODSIM',
'ST_t_channel' : '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/'+MCType16+'/NANOAODSIM',
'ST_tbar_channel' : '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/'+MCType16+'/NANOAODSIM',
'ST_tW_channel' : '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',
'ST_tbarW_channel' : '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/'+MCType16+'/NANOAODSIM',

'WW'      : '/WW_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'WZ'      : '/WZ_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'ZZ'      : '/ZZ_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',

'QCD_Pt15to20_Mu'         : '/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt20to30_Mu'         : '/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt30to50_Mu'         : '/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt50to80_Mu'         : '/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt80to120_Mu'        : '/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt120to170_Mu'       : '/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt170to300_Mu'       : '/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt300to470_Mu'       : '/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt470to600_Mu'       : '/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt600to800_Mu'       : '/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt800to1000_Mu'      : '/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt1000toInf_Mu'      : '/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',

'QCD_Pt20to30_Ele'        : '/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType16_v2+'/NANOAODSIM',
'QCD_Pt30to50_Ele'        : '/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt50to80_Ele'        : '/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt80to120_Ele'       : '/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt120to170_Ele'      : '/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt170to300_Ele'      : '/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',
'QCD_Pt300toInf_Ele'      : '/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/'+MCType16+'/NANOAODSIM',

}

#--------------------------
# 2017
#--------------------------
#MCType17 = 'RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1'
# MCType17 = 'RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1'
# MCType17_pmx = MCType17.replace('102X','new_pmx_102X')
# MCType17_v2 = MCType17.replace('-v1','-v2')
# MCType17_ext1 = MCType17.replace('-v1','_ext1-v1')
# MCType17_ext2 = MCType17.replace('-v1','_ext2-v1')
# MCType17_RECOSIM = MCType17.replace('PU2017','PU2017RECOSIMstep')
# MCType17_RECOSIM_ext1 = MCType17_RECOSIM.replace('-v1','_ext1-v1')
# MCType17_oddTTZ = 'RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_v7_102X_mc2017_realistic_v7-v1'
# MCType17_oddWW = 'RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1'
# DataType17='Nano1June2019-v1'

MCType17    = 'RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1'
MCType17S20 = 'RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1'
MCType17_v2 = MCType17.replace('-v1','-v2')

DataType17 = 'UL2017_MiniAODv1_NanoAODv2-v1'

sampleList_2017 = {

# 'HplusM080' : '/ChargedHiggsToCS_M080_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM090' : '/ChargedHiggsToCS_M090_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM100' : '/ChargedHiggsToCS_M100_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM120' : '/ChargedHiggsToCS_M120_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM140' : '/ChargedHiggsToCS_M140_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM150' : '/ChargedHiggsToCS_M150_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM155' : '/ChargedHiggsToCS_M155_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM160' : '/ChargedHiggsToCS_M160_13TeV-madgraph/'+MCType16+'/NANOAODSIM',

'Data_SingleMu_b' : '/SingleMuon/Run2017B-'+DataType17+'/NANOAOD',
'Data_SingleMu_c' : '/SingleMuon/Run2017C-'+DataType17+'/NANOAOD',
'Data_SingleMu_d' : '/SingleMuon/Run2017D-'+DataType17+'/NANOAOD',
'Data_SingleMu_e' : '/SingleMuon/Run2017E-'+DataType17+'/NANOAOD',
'Data_SingleMu_f' : '/SingleMuon/Run2017F-'+DataType17+'/NANOAOD',
'Data_SingleMu_g' : '/SingleMuon/Run2017G-'+DataType17+'/NANOAOD',

'Data_SingleEle_b' : '/SingleElectron/Run2017B-'+DataType17+'/NANOAOD',
'Data_SingleEle_c' : '/SingleElectron/Run2017C-'+DataType17+'/NANOAOD',
'Data_SingleEle_d' : '/SingleElectron/Run2017D-'+DataType17+'/NANOAOD',
'Data_SingleEle_e' : '/SingleElectron/Run2017E-'+DataType17+'/NANOAOD',
'Data_SingleEle_f' : '/SingleElectron/Run2017F-'+DataType17+'/NANOAOD',

'TTbarPowheg_Dilepton' : '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Hadronic' : '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Semilept' : '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',

'TTbarPowheg_Dilepton_CP5up'           : '/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Dilepton_CP5down'         : '/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Dilepton_hdampup'         : '/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Dilepton_hdampdown'       : '/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Dilepton_mtop1695'        : '/TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Dilepton_mtop1755'        : '/TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',

'TTbarPowheg_Hadronic_CP5up'           : '/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Hadronic_CP5down'         : '/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Hadronic_hdampup'         : '/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Hadronic_hdampdown'       : '/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Hadronic_mtop1695'        : '/TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Hadronic_mtop1755'        : '/TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',

'TTbarPowheg_Semilept_CP5up'           : '/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Semilept_CP5down'         : '/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Semilept_hdampup'         : '/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Semilept_hdampdown'       : '/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Semilept_mtop1695'        : '/TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',
'TTbarPowheg_Semilept_mtop1755'        : '/TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/'+MCType17+'/NANOAODSIM',

'W1jets'      : '/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',
'W2jets'      : '/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',
'W3jets'      : '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',
'W4jets'      : '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',

'DYjetsM10to50'      : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17S20+'/NANOAODSIM',
'DYjetsM50' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType17+'/NANOAODSIM',

'ST_s_channel' : '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType17+'/NANOAODSIM',
'ST_t_channel' : '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/'+MCType17+'/NANOAODSIM',
'ST_tbar_channel' : '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/'+MCType17+'/NANOAODSIM',
'ST_tW_channel' : '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/'+MCType17S20+'/NANOAODSIM',
'ST_tbarW_channel' : '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/'+MCType17S20+'/NANOAODSIM',

'WW'      : '/WW_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'WZ'      : '/WZ_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'ZZ'      : '/ZZ_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',

'QCD_Pt15to20_Mu'         : '/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt20to30_Mu'         : '/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt30to50_Mu'         : '/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt50to80_Mu'         : '/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt80to120_Mu'        : '/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt120to170_Mu'       : '/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt170to300_Mu'       : '/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt300to470_Mu'       : '/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt470to600_Mu'       : '/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt600to800_Mu'       : '/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt800to1000_Mu'      : '/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',
'QCD_Pt1000toInf_Mu'      : '/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType17S20+'/NANOAODSIM',

'QCD_Pt20to30_Ele'        : '/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17_v2+'/NANOAODSIM',
'QCD_Pt30to50_Ele'        : '/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17_v2+'/NANOAODSIM',
'QCD_Pt50to80_Ele'        : '/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt80to120_Ele'       : '/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt120to170_Ele'      : '/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt170to300_Ele'      : '/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',
'QCD_Pt300toInf_Ele'      : '/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType17+'/NANOAODSIM',

}


#--------------------------
# 2018
#--------------------------
#MCType18='RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1'
# MCType18='RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1'
# MCType18_ext1 = MCType18.replace('-v1','_ext1-v1')
# MCType18_ext2 = MCType18.replace('-v1','_ext2-v1')
# MCType18_ext3 = MCType18.replace('-v1','_ext3-v1')
# MCType18_4cores5k = MCType18.replace('102X','4cores5k_102X')
# MCType18_v3 = MCType18.replace('-v1','-v3')

# DataType='Nano1June2019-v1'

MCType18='RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1'
MCType18_ele='RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1'

DataType18 = 'UL2018_MiniAODv1_NanoAODv2-v2'
DataType18_v3 = DataType18.replace('-v2','-v3')

DataType18_ele = 'UL2018_MiniAODv1_NanoAODv2-v1'
DataType18_ele_v2 = DataType18_ele.replace('-v1','-v2')

sampleList_2018 = {
# 'HplusM080' : '/ChargedHiggsToCS_M080_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM090' : '/ChargedHiggsToCS_M090_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM100' : '/ChargedHiggsToCS_M100_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM120' : '/ChargedHiggsToCS_M120_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM140' : '/ChargedHiggsToCS_M140_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM150' : '/ChargedHiggsToCS_M150_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM155' : '/ChargedHiggsToCS_M155_13TeV-madgraph/'+MCType16+'/NANOAODSIM',
# 'HplusM160' : '/ChargedHiggsToCS_M160_13TeV-madgraph/'+MCType16+'/NANOAODSIM',

'Data_SingleMu_a' : '/SingleMuon/Run2018A-'+DataType18_v3+'/NANOAOD',
'Data_SingleMu_b' : '/SingleMuon/Run2018B-'+DataType18+'/NANOAOD',
'Data_SingleMu_c' : '/SingleMuon/Run2018C-'+DataType18+'/NANOAOD',
'Data_SingleMu_d' : '/SingleMuon/Run2018D-'+DataType18+'/NANOAOD',

'Data_SingleEle_a' : '/EGamma/Run2018A-'+DataType18_ele+'/NANOAOD',
'Data_SingleEle_b' : '/EGamma/Run2018B-'+DataType18_ele+'/NANOAOD',
'Data_SingleEle_c' : '/EGamma/Run2018C-'+DataType18_ele+'/NANOAOD',
'Data_SingleEle_d' : '/EGamma/Run2018D-'+DataType18_ele_v2+'/NANOAOD',

'TTbarPowheg_Dilepton' : '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Hadronic' : '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Semilept' : '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',

'TTbarPowheg_Dilepton_CP5up'           : '/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Dilepton_CP5down'         : '/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Dilepton_hdampup'         : '/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Dilepton_hdampdown'       : '/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Dilepton_mtop1695'        : '/TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Dilepton_mtop1755'        : '/TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',

'TTbarPowheg_Hadronic_CP5up'           : '/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Hadronic_CP5down'         : '/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Hadronic_hdampup'         : '/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Hadronic_hdampdown'       : '/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Hadronic_mtop1695'        : '/TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Hadronic_mtop1755'        : '/TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',

'TTbarPowheg_Semilept_CP5up'           : '/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Semilept_CP5down'         : '/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Semilept_hdampup'         : '/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Semilept_hdampdown'       : '/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Semilept_mtop1695'        : '/TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'TTbarPowheg_Semilept_mtop1755'        : '/TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',

'W1jets'      : '/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'W2jets'      : '/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'W3jets'      : '/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'W4jets'      : '/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',

'DYjetsM10to50'      : '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',
'DYjetsM50' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/'+MCType18+'/NANOAODSIM',

'ST_s_channel' : '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/'+MCType18+'/NANOAODSIM',
'ST_t_channel' : '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/'+MCType18+'/NANOAODSIM',
'ST_tbar_channel' : '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/'+MCType18+'/NANOAODSIM',
'ST_tW_channel' : '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',
'ST_tbarW_channel' : '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/'+MCType18+'/NANOAODSIM',

'WW'      : '/WW_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'WZ'      : '/WZ_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'ZZ'      : '/ZZ_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',

'QCD_Pt15to20_Mu'         : '/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt20to30_Mu'         : '/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt30to50_Mu'         : '/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt50to80_Mu'         : '/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt80to120_Mu'        : '/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt120to170_Mu'       : '/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt170to300_Mu'       : '/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt300to470_Mu'       : '/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt470to600_Mu'       : '/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt600to800_Mu'       : '/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt800to1000_Mu'      : '/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',
'QCD_Pt1000toInf_Mu'      : '/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/'+MCType18+'/NANOAODSIM',

'QCD_Pt20to30_Ele'        : '/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18_ele+'/NANOAODSIM',
'QCD_Pt30to50_Ele'        : '/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18_ele+'/NANOAODSIM',
'QCD_Pt50to80_Ele'        : '/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18_ele+'/NANOAODSIM',
'QCD_Pt80to120_Ele'       : '/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18_ele+'/NANOAODSIM',
'QCD_Pt120to170_Ele'      : '/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18_ele+'/NANOAODSIM',
'QCD_Pt170to300_Ele'      : '/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18_ele+'/NANOAODSIM',
'QCD_Pt300toInf_Ele'      : '/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/'+MCType18_ele+'/NANOAODSIM',


}
