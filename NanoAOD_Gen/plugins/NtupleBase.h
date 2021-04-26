#ifndef __validation_NtupleGenJet_NtupleBase_h__
#define __validation_NtupleGenJet_NtupleBase_h__

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include"TTree.h"


class NtupleBase
{
    public:
        NtupleBase(const edm::ParameterSet& conf) {};
        virtual ~NtupleBase(){};	
        virtual void initialize(TTree& , const edm::ParameterSet&, edm::ConsumesCollector&& ) = 0;
        virtual void fill(const edm::Event& , const edm::EventSetup& ) = 0;

    protected:
        virtual void clear() = 0;
};



#endif
