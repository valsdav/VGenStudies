from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'WplusToJJWminusToLNuJJ_VBS_Herwig7'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/WplusToJJWminusToLNuJJ_VBS_Herwig7.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 1

config.Data.outputPrimaryDataset = 'WplusToJJWminusToLNuJJ_VBS_Herwig7'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000
NJOBS = 30  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFNDirBase = '/store/group/cmst3/user/kelong/' 
config.Data.outLFNDirBase = '/store/group/phys_smp/VJets_NLO_VBSanalyses/Samples/NanoGEN' 
config.Data.publication = False
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_CH_CERN'
