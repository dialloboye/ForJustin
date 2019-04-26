 #Author: diallo boye <diallo.boye@cern.ch>

#This is a template joboption for generating events with the HAHM madgraph model
#To use it, copy the template and rename it by replacing the XXXXXX and YYYYYYYYY in the filename with:
# make XXXXXX match the runNumber you give to Generate_tf
# make the YYYYYYYY a short description
#Then modify:
# - proc_card (for the process), 
# - param_card_extras (for the model parameters), 
# - run_card_extras (for the generator-level cuts),
# - post_lhe_hook (a hook method for executing code after the lhe making (madgraph) but before showering (pythia)

#Run it with (for example):
# Generate_tf.py --ecmEnergy=13000 --runNumber=302076 --firstEvent=1 --asetup="" --maxEvents=5000 --randomSeed=1 --jobConfig="MC15.302076.MadGraphPythia8EvtGen_A14NNPDF23LO_HAHMggfZdZd4l_mZd5.py" --outputEVNTFile=my.evgen.root

#--------------------------

#<CHANGE THESE SETTINGS. keywords MUST BE IN LIST OF ALLOWED KEYWORDS>
evgenConfig.description="high mass higgs to ZZ"
evgenConfig.keywords+=['exotic','BSMHiggs']
evgenConfig.contact = ['diallo.boye@cern.ch']
evgenConfig.process = "HAHM_H_ZdZd_4l"


#<REPLACE WITH YOUR PROC_CARD CONTENT>
proc_card = """
import model HAHM_variableMW_v3_UFO
define l+ = e+ mu+
define l- = e- mu-
generate g g > h HIG=1 HIW=0 QED=0 QCD=0, (h > Zp Zp, Zp > l+ l-)"""



proc_name = evgenConfig.process #just used for the mg directory name

#modifications to the param_card.dat (generated from the proc_card i.e. the specific model)
#if you want to see the resulting param_card, run Generate_tf with this jobo, and look at the param_card.dat in the cwd
#If you want to see the auto-calculated values of the decay widths, look at the one in <proc_name>/Cards/param_card.dat (again, after running a Generate_tf)

param_card_extras = { "HIDDEN": { 'epsilon': '1e-4', #kinetic mixing parameter
                                 'kap': '1e-4', #higgs mixing parameter
                                 'mzdinput': '91.18', #Zd mass
                                 'mhsinput':'1000.0' }, #dark higgs mass
                     "HIGGS": { 'mhinput':'800'}, #higgs mass
                     "DECAY": { 'wzp':'Auto', 'wh':'302.1', 'wt':'Auto' } #auto-calculate decay widths and BR of Zp, H, t
                  }


run_card_extras = { 'lhe_version':'2.0',
                   'cut_decays':'F',
                   'ptj':'0',
                   'ptb':'0',
                   'pta':'0',
                   'ptl':'0',
                   'etaj':'-1',
                   'etab':'-1',
                   'etaa':'-1',
                   'etal':'-1',
                   'drjj':'0',
                   'drbb':'0',
                   'drll':'0',
                   'draa':'0',
                   'drbj':'0',
                   'draj':'0',
                   'drjl':'0',
                   'drab':'0',
                   'drbl':'0',
                   'dral':'0' }



def post_lhe_hook():
    #You can put code here that will get called after the 'generate' method of MadGraphControl is called
    #What follows is an example for modifying the lifetime of the zd:
    #The 'add_lifetimes' method is defined in the file included below. It modifies the lhe file to include particle lifetimes on the particle with given pdgId
    #add_lifetimes(pdgId=32, avgtau=5)
    pass





include("MC15JobOptions/MadGraphControl_Pythia8_A14_NNPDF23LO_EvtGen_Common.py")












