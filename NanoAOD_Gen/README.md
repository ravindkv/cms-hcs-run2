## Decay of charged Higgs using pythia
The process "p p > t t~ [QCD]" are generated using MadGraph and the 
subsequent decay  "t t~ > H+ b W- b~" is performed using MadSpin. The
final decay "H+ > c s~" and "W- > l- vl~" is performed using Pythia
before the parton shower. To perform these, run the following commands

### cmsrel CMSSW_10_6_18
### cd CMSSW_10_6_18/src
### cmsenv
### git clone https://github.com/ravindkv/cms-hcs-run2.git
### cd NanoAOD_Gen 
### scram b
### cd test
### cmsRun hplusGenerator_cfg.py 

After these commands, root files containing generator level information
will be created. To read these files and plot basic kinematic distributions,
run the following commands:

### cmsRun genAnalyzer_cfg.py 

