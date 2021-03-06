# Copyright (C) 2013 Nathan Charles
#
# This program is free software. See terms in LICENSE file.
"""
NFPA NEC tables
"""
# pragma: no cover

# 700 is a standard size, but isn't listed in some tables
CONDUCTOR_STANDARD_SIZES = ["14", "12", "10", "8", "6", "4", "2", "1", "1/0",
                            "2/0", "3/0", "4/0", "250", "300", "350", "400",
                            "500", "600", "750"]
# NEC 240.6
OCP_STANDARD_SIZES = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100,
                      110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450,
                      500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000,
                      4000, 5000, 6000]

OCP_STANDARD_FUSES = [1, 3, 6, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70,
                      80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 300,
                      350, 400, 450, 500, 600, 601, 700, 800, 1000, 1200,
                      1600, 2000, 2500, 3000, 4000, 5000, 6000]

# NEC 310.15(B)(16)
CU_AMPACITY_A30_75 = {"14":20, \
        "12":25, \
        "10":35, \
        "8":50, \
        "6":65, \
        "4":85, \
        "3":100, \
        "2":115, \
        "1":130, \
        "1/0":150, \
        "2/0":175, \
        "3/0":200, \
        "4/0":230, \
        "250":255, \
        "300":285, \
        "350":310, \
        "400":335, \
        "500":380, \
        "600":420, \
        "700":460, \
        "750":475}
AL_AMPACITY_A30_75 = {"14": .1, \
        "12":20, \
        "10":30, \
        "8":40, \
        "6":50, \
        "4":65, \
        "3":75, \
        "2":90, \
        "1":100, \
        "1/0":120, \
        "2/0":135, \
        "3/0":155, \
        "4/0":180, \
        "250":205, \
        "300":230, \
        "350":250, \
        "400":270, \
        "500":310, \
        "600":340, \
        "700":375, \
        "750":385}
# Ambiant Temperature Correction Factor

PVC_X = {"14" : 0.058, \
    "12" : 0.054, \
    "10" : 0.050, \
    "8" : 0.052, \
    "6" : 0.051, \
    "4" : 0.048, \
    "3" : 0.047, \
    "2" : 0.045, \
    "1" : 0.046, \
    "1/0" : 0.044, \
    "2/0" : 0.043, \
    "3/0" : 0.042, \
    "4/0" : 0.041, \
    "250" : 0.041, \
    "300" : 0.041, \
    "350" : 0.040, \
    "400" : 0.040, \
    "500" : 0.039, \
    "600" : 0.039, \
    "750" : 0.038}

AL_X = PVC_X

STEEL_X = {"14" : 0.073, \
    "12" : 0.068, \
    "10" : 0.063, \
    "8" : 0.065, \
    "6" : 0.064, \
    "4" : 0.060, \
    "3" : 0.059, \
    "2" : 0.057, \
    "1" : 0.057, \
    "1/0" : 0.055, \
    "2/0" : 0.054, \
    "3/0" : 0.052, \
    "4/0" : 0.051, \
    "250" : 0.052, \
    "300" : 0.051, \
    "350" : 0.050, \
    "400" : 0.049, \
    "500" : 0.048, \
    "600" : 0.048, \
    "750" : 0.048}

PVC_CU = {"14" : 3.100, \
    "12" : 2.000, \
    "10" : 1.200, \
    "8" : 0.780, \
    "6" : 0.490, \
    "4" : 0.310, \
    "3" : 0.250, \
    "2" : 0.190, \
    "1" : 0.150, \
    "1/0" : 0.120, \
    "2/0" : 0.100, \
    "3/0" : 0.077, \
    "4/0" : 0.062, \
    "250" : 0.052, \
    "300" : 0.044, \
    "350" : 0.038, \
    "400" : 0.033, \
    "500" : 0.027, \
    "600" : 0.023, \
    "750" : 0.019}

AL_CU = {"14" : 3.100, \
    "12" : 2.000, \
    "10" : 1.200, \
    "8" : 0.780, \
    "6" : 0.490, \
    "4" : 0.310, \
    "3" : 0.250, \
    "2" : 0.200, \
    "1" : 0.160, \
    "1/0" : 0.130, \
    "2/0" : 0.100, \
    "3/0" : 0.082, \
    "4/0" : 0.067, \
    "250" : 0.057, \
    "300" : 0.049, \
    "350" : 0.043, \
    "400" : 0.038, \
    "500" : 0.032, \
    "600" : 0.028, \
    "750" : 0.024}

STEEL_CU = {"14" : 3.100, \
    "12" : 2.000, \
    "10" : 1.200, \
    "8" : 0.780, \
    "6" : 0.490, \
    "4" : 0.310, \
    "3" : 0.250, \
    "2" : 0.200, \
    "1" : 0.160, \
    "1/0" : 0.120, \
    "2/0" : 0.100, \
    "3/0" : 0.079, \
    "4/0" : 0.063, \
    "250" : 0.054, \
    "300" : 0.045, \
    "350" : 0.039, \
    "400" : 0.035, \
    "500" : 0.029, \
    "600" : 0.025, \
    "750" : 0.021}

PVC_AL = {"14" : 5.100, \
    "12" : 3.200, \
    "10" : 2.000, \
    "8" : 1.300, \
    "6" : 0.810, \
    "4" : 0.510, \
    "3" : 0.400, \
    "2" : 0.320, \
    "1" : 0.250, \
    "1/0" : 0.200, \
    "2/0" : 0.160, \
    "3/0" : 0.130, \
    "4/0" : 0.100, \
    "250" : 0.085, \
    "300" : 0.071, \
    "350" : 0.061, \
    "400" : 0.054, \
    "500" : 0.043, \
    "600" : 0.036, \
    "750" : 0.029}

AL_AL = {"14" : 5.100, \
    "12" : 3.200, \
    "10" : 2.000, \
    "8" : 1.300, \
    "6" : 0.810, \
    "4" : 0.510, \
    "3" : 0.410, \
    "2" : 0.320, \
    "1" : 0.260, \
    "1/0" : 0.210, \
    "2/0" : 0.160, \
    "3/0" : 0.130, \
    "4/0" : 0.110, \
    "250" : 0.090, \
    "300" : 0.076, \
    "350" : 0.066, \
    "400" : 0.059, \
    "500" : 0.048, \
    "600" : 0.041, \
    "750" : 0.034}

STEEL_AL = {"14" : 5.100, \
    "12" : 3.200, \
    "10" : 2.000, \
    "8" : 1.300, \
    "6" : 0.810, \
    "4" : 0.510, \
    "3" : 0.400, \
    "2" : 0.320, \
    "1" : 0.250, \
    "1/0" : 0.200, \
    "2/0" : 0.160, \
    "3/0" : 0.130, \
    "4/0" : 0.100, \
    "250" : 0.086, \
    "300" : 0.072, \
    "350" : 0.063, \
    "400" : 0.055, \
    "500" : 0.045, \
    "600" : 0.038, \
    "750" : 0.031}

_CU = {"14" : 3.140, \
    "12" : 1.980, \
    "10" : 1.240, \
    "8" : 0.778, \
    "6" : 0.491, \
    "4" : 0.308, \
    "3" : 0.245, \
    "2" : 0.194, \
    "1" : 0.154, \
    "1/0" : 0.122, \
    "2/0" : .0967, \
    "3/0" : .0766, \
    "4/0" : .0608, \
    "250" : .0515, \
    "300" : .0429, \
    "350" : .0367, \
    "400" : .0321, \
    "500" : .0258, \
    "600" : .0214, \
    "750" : .0171}

_AL = {"14" : 5.170, \
    "12" : 3.250, \
    "10" : 2.040, \
    "8" : 1.280, \
    "6" : 0.808, \
    "4" : 0.508, \
    "3" : 0.403, \
    "2" : 0.319, \
    "1" : 0.253, \
    "1/0" : 0.201, \
    "2/0" : 0.159, \
    "3/0" : 0.126, \
    "4/0" : 0.100, \
    "250" : .0847, \
    "300" : .0707, \
    "350" : .0605, \
    "400" : .0529, \
    "500" : .0424, \
    "600" : .0353, \
    "750" : .0282}


#NEC Table 250.122
EGC_CU = {15:"14", \
        20:"12", \
        60:"10", \
        100:"8", \
        200:"6", \
        300:"4", \
        400:"3", \
        500:"2", \
        600:"1", \
        800:"1/0", \
        1000:"2/0", \
        1200:"3/0", \
        1600:"4/0", \
        2000:"250", \
        2500:"350", \
        3000:"400", \
        4000:"500", \
        5000:"700", \
        6000:"800"}

#NEC Table 250.122
EGC_AL = {15:"12", \
        20:"10", \
        60:"8", \
        100:"6", \
        200:"4", \
        300:"2", \
        400:"1", \
        500:"1/0", \
        600:"2/0", \
        800:"3/0", \
        1000:"4/0", \
        1200:"250", \
        1600:"350", \
        2000:"400", \
        2500:"600", \
        3000:"600", \
        4000:"750", \
        5000:"1200", \
        6000:"1200"}

CMIL = {"18":1620, \
        "16":2580, \
        "14":4110, \
        "12":6530, \
        "10":10380, \
        "8":16510, \
        "6":26240, \
        "4":41740, \
        "3":52620, \
        "2":66360, \
        "1":83690, \
        "1/0":105600, \
        "2/0":133100, \
        "3/0":167800, \
        "4/0":211600, \
        "250":250000, \
        "300":300000, \
        "350":350000, \
        "400":400000, \
        "500":500000, \
        "600":600000, \
        "700":700000, \
        "750":750000, \
        "800":800000, \
        "900":900000, \
        "1000":1000000, \
        "1250":1250000, \
        "1500":1500000, \
        "2000":2000000}

# Article 358
# Total Area
EMT = {"1/2":.304, \
        "3/4":.533, \
        "1":.864, \
        "1 1/4":1.496, \
        "1 1/2":2.036, \
        "2":3.356, \
        "2 1/2":5.858, \
        "3":8.846, \
        "3 1/2":11.545, \
        "4":14.753}

EMT_TRADE_SIZES = ["1/2", "3/4", "1", "1 1/4", "1 1/2", "2", "2 1/2", "3", \
        "3 1/2", "4"]

PVC40 = {"1/2":.217, \
        "3/4":.409, \
        "1":.688, \
        "1 1/4":1.237, \
        "1 1/2":1.711, \
        "2":2.874, \
        "2 1/2":4.119, \
        "3":6.442, \
        "3 1/2":8.688, \
        "4":11.258, \
        "5":17.855, \
        "6":25.598}

PVC40_TRADE_SIZES = ["1/2", "3/4", "1", "1 1/4", "1 1/2", "2", "2 1/2", "3", \
        "3 1/2", "4", "5", "6"]

# Chapter 9 Table 5
THWN = { \
        "14":  0.111, \
        "12":  0.13, \
        "10":  0.164, \
        "8":   0.216, \
        "6":   0.254, \
        "4":   0.324, \
        "3":   0.352, \
        "2":   0.384, \
        "1":   0.446, \
        "1/0": 0.486, \
        "2/0": 0.532, \
        "3/0": 0.584, \
        "4/0": 0.642, \
        "250": 0.711, \
        "300": 0.766, \
        "350": 0.817, \
        "400": 0.864, \
        "500": 0.949, \
        "600": 1.051, \
        "700": 1.122, \
        "750": 1.156, \
        }
# Southwire
PV = { \
        "14":  0.222, \
        "12":  0.237, \
        "10":  0.261, \
        "8":   0.312, \
        "6":   0.349, \
        "4":   0.396, \
        "2":   0.456, \
        "1":   0.531, \
        "1/0": 0.570, \
        "2/0": 0.614, \
        "3/0": 0.664, \
        "4/0": 0.720 \
        }

# Chapter 9 Table 5
XHHW = {"6":.29, #Values estimated from various datasheets
        "4":.33, \
        "3":.36, \
        "2":.4, \
        "1": 0.442, #Table Starts Here
        "1/0": 0.482, \
        "2/0": 0.528, \
        "3/0": 0.58, \
        "4/0": 0.638, \
        "250": 0.705, \
        "300": 0.76, \
        "350": 0.811, \
        "400": 0.858, \
        "500": 0.943, \
        "600": 1.053, \
        "700": 1.124, \
        "750": 1.158}
