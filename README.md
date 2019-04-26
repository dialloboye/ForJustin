# ForJustin
To run generate sample with Madgraph:
asetup 19.2.5.26
Generate_tf.py --ecmEnergy=13000 --runNumber=450563 --firstEvent=1 --asetup="" --maxEvents=10000 --randomSeed=1 --jobConfig="MC15.450563.MadGraphPythia8EvtGen_A14NNPDF23LO_HAHMggfZdZd4l_91_800.py" --outputEVNTFile=my.output_10000Evt_higgs800_massZ.root >my.output_10000Evt_higgs175_Zmass.log &
