#!python [optional-arg]
# -*- coding: utf-8 -*-

"""
This Code is used to process the data collected from the ADC Sled on the Space System Lab's UMD 2019 Rocksat X robotic payload.

The purpose is to take the raw file and convert it to serveral sperate data files for each of the sensors.
The script will take two inputs from the command line. The first is the path of the data file that is being parsed. The second is the location to store the data files that have been parsed from the raw data file.
MIT License
"""

# Futures
from __future__ import print_function
# […]

# Built-in/Generic Imports
import os
import sys
# […]

# Libs
import pandas as pd # Or any other
# […]

# Own modules
#from {path} import {class}
# […]

__author__ = 'Nicholas M Limparis'
__copyright__ = 'Copyright 2019, UMD Rocksat-X'
__credits__ = ['Nicholas M Limparis']
__license__ = '{MIT}'
__version__ = '0.1.0'
__maintainer__ = 'Nicholas M Limparis'
__email__ = 'nicholas@github.limpar.is'
__status__ = 'Dev'


#Code goes here.

