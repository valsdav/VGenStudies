# from HIG-RunIIFall18wmLHEGS-02021 and SMP-RunIISummer15wmLHEGS-00138
import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/VVjj_SemiLeptonic/WMhadZlepJJ_EWK_LO_SM_mjj100_pTj10_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    generateConcurrently = cms.untracked.bool(False),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

from Configuration.Generator.Herwig7Settings.Herwig7LHECommonSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7StableParticlesForDetector_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7CH3TuneSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7LHEMG5aMCatNLOSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7PSWeightsSettings_cfi import *


generator = cms.EDFilter("Herwig7GeneratorFilter",
    herwig7LHECommonSettingsBlock,
    herwig7LHEMG5aMCatNLOSettingsBlock,
    herwig7PSWeightsSettingsBlock,
    herwig7StableParticlesForDetectorBlock,
    herwig7CH3SettingsBlock,
    configFiles = cms.vstring(),
    crossSection = cms.untracked.double(-1),
    dataLocation = cms.string('${HERWIGPATH:-6}'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    filterEfficiency = cms.untracked.double(1.0),
    generatorModule = cms.string('/Herwig/Generators/EventGenerator'),    
    hw_user_settings = cms.vstring(
        'cd /Herwig/EventHandlers',
        'set EventHandler:LuminosityFunction:Energy 13000*GeV',
        'cd /',
    ),     
    parameterSets = cms.vstring(
        'hw_lhe_common_settings',
        'hw_lhe_MG5aMCatNLO_settings',
        'herwig7CH3PDF', 
        'herwig7CH3AlphaS', 
        'herwig7CH3MPISettings', 
        'herwig7StableParticlesForDetector',
        'hw_PSWeights_settings',
        'hw_user_settings'
    ),
    repository = cms.string('${HERWIGPATH}/HerwigDefaults.rpo'),
    run = cms.string('InterfaceMatchboxTest'),
    runModeList = cms.untracked.string('read,run'),
)

ProductionFilterSequence = cms.Sequence(generator)
