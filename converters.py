"""Library of units converters"""

# Declare useful constants
NPL = 4.44822 # newtons per pound-foot 
IPM = 1550 # square inches per square meter 
LPN = 0.224809 # pound-force per newton 
MPI =  0.00064516 # meters squared per inch squared
MPK = 0.621372 # miles per kilometer 
LPG = 3.78541 # liters per gallon
KPM = 1.60934 # kilometers per mile 
GPL = 0.264172 # gallons per liter 

def psi2kpa(psi):
    """
    Takes in a PSI value and converts it to KPa
    """
    return psi * NPL * IPM / 1000

def kpa2psi(kpa):
    """
    Takes in a KPa value and converts it to PSI
    """
    return kpa * 1000 * LPN * MPI 

def mpg2lp100k(mpg):
    """
    Takes in a MPG value and converts it to liters per 1ookm.
    """
    return (1/mpg) * MPK * LPG * 100 

def lp100k2mpg(lp100k):
    """
    Takes in liters per 100km value and converts it to mpg. 
    """
    return 1/(lp100k * 0.01 * KPM * GPL)