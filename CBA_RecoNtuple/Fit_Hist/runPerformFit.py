import os
import itertools
import json
from FitInputs import *

if not os.path.exists("./RateParams.json"):
    with open("RateParams.json", "w") as f:
        data = {}
        json.dump(data, f)

def runCmd(cmd):
    print "\n\033[01;32m Excecuting: %s \033[00m"%cmd
    os.system(cmd)

for year, decay, channel, mass in itertools.product(Year, Decay, Channel, Mass): 
    args = "-y %s -d %s -c %s -m %s"%(year, decay, channel, mass)
    runCmd("python performFit.py %s --isT2W --isLimit"%args)
