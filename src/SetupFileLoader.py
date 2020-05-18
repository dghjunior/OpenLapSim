"""
---------------------------
Setup File - OLS
---------------------------
Below an example of setupFile.json (REMOUVE comments "#..." on real JSON file)

{
    "setupName" : "Gp2Dummy",
    "mcar"		: 728,        #[Kg]; total car mass
    "clt"		: 3.1,        #[100 pt.]; Lift coeffitien (-)
    "cx"		: 1.0,        #[100 pt.]; Drag coeffitien
    "afrcar"	: 1.0,        #[m2]; Frontal Area
    "mbrk"		: 7000,       #[m2]; Max Braking Torque
    "gripx"		: 1.0,        #tyre friction coeff long
    "gripy"		: 1.25,       #tyre friction coeff lat
    "rtyre"		: 0.32,       #[m]; tyre radius
    "rGearRat"	: [10.0,7.8,6.1,7.8,5.2,4.5,4.0],  #Final Gear Ratio
    "reff"		: 0.95,       # drive line efficiency
    "EngNm"     : [200,300,430,380], # [Nm]; Engine Torque 
    "EngRpm"    : [0,3000,7000,10000],  # [rpm]Engine rmp
    "rho"		: 1.22        #[Kg/m3]; air density
}
                                                                      
"""
# Import Packages
import numpy as np
import json

class SetupFileLoader:
    
    def __init__(self, setupFileName):
        self.setupFileName = setupFileName
        self.setupDict = {}
        
    def loadJSON(self):
        # load json
        with open(self.setupFileName) as f: 
            data = json.load(f)         
        # set setupDict
        self.setupDict = data
        
{
    "setupName" : "Gp2Dummy",
    "mcar"		: 728,        #[Kg]; total car mass
    "clt"		: 3.1,        #[100 pt.]; Lift coeffitien (-)
    "cx"		: 1.0,        #[100 pt.]; Drag coeffitien
    "afrcar"	: 1.0,        #[m2]; Frontal Area
    "rho"		: 1.22        #[Kg/m3]; air density
    "mbrk"		: 7000,       #[m2]; Max Braking Torque
    "gripx"		: 1.0,        #tyre friction coeff long
    "gripy"		: 1.25,       #tyre friction coeff lat
    "rtyre"		: 0.32,       #[m]; tyre radius
    "reff"		: 0.95,       # drive line efficiency
    "rGearRat"	: [10.0,7.8,6.1,7.8,5.2,4.5,4.0],  #Final Gear Ratio
    "EngNm"     : [200,300,430,380], # [Nm]; Engine Torque 
    "EngRpm"    : [0,3000,7000,10000],  # [rpm]Engine rmp
}