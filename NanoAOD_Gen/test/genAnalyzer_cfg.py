import FWCore.ParameterSet.Config as cms

process = cms.Process("Validation")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(
        #'file:/afs/cern.ch/work/l/lata/grid_pack/genproductions/bin/JHUGen/production_validation_HIG/susy_gridpack_validation/2016_LHEs/HIG-RunIISummer15wmLHEGS-01479.root'
        
       #'file:/afs/cern.ch/user/g/gkole/work/public/HIG-RunIISummer15wmLHEGS-01479.root' # for bbHToTauTau 
                                    #'file:/tmp/gkole/CMSSW_10_6_18/src/HIG-RunIISummer20UL16wmLHEGEN-00039.root'
                                    'file:../../../HIG-RunIISummer20UL16wmLHEGEN-00039.root'
                )
                            )



ntuple_genHiggs = cms.PSet(
     NtupleName = cms.string('NtupleGenJet'),
     genParticles = cms.InputTag('genParticles'),
)
process.demo = cms.EDAnalyzer(
    "NtupleGenJet",
    Ntuples = cms.VPSet(
	ntuple_genHiggs,
    )
)
process.TFileService = cms.Service("TFileService",
    fileName = cms.string("output_GenAnalyzer.root"
))
process.p = cms.Path(process.demo)
process.MessageLogger.cerr.FwkReport.reportEvery = 1


