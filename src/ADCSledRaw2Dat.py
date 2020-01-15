#!python [optional-arg]
# -*- coding: utf-8 -*-

"""
This Code is used to process the data collected from the ADC Sled on 
the Space System Lab's UMD 2019 Rocksat X robotic payload.

The purpose is to take the raw file and convert it to serveral sperate
data files for each of the sensors. The script will take two inputs
from the command line. The first is the path of the data file that is 
being parsed. The second is the location to store the data files that 
have been parsed from the raw data file.

This tool will accept commands as follows and is written in Python 3

python3 ADCSledRaw2Dat.py /Input/File/Path.dat /Output/Files/Folder/

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
#import pandas as pd # Or any other
# […]

# Own modules
#from {path} import {class}
# […]

__author__ = 'Nicholas M Limparis'
__copyright__ = 'Copyright 2020, UMD Rocksat-X'
__credits__ = ['Nicholas M Limparis']
__license__ = '{MIT}'
__version__ = '0.1.0'
__maintainer__ = 'Nicholas M Limparis'
__email__ = 'nicholas@github.limpar.is'
__status__ = 'Dev'


#Code goes here.


# print(sys.argv)  # Arguments at index 1 and greater contain the 
# print(len(sys.argv))
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

def main():
    if len(sys.argv) != 3:
        sys.exit("This command does not have a valid number of arguments. It should be in the format  Command /input/File/Path.dat /output/files/path/ Please run the command again.")
    
    #Check to see if the first command line argument is a file
    if not os.path.isfile(sys.argv[1]):
        sys.exit("The input file is not a file")
    
    #Check to see if the second command line argument is a directory
    if not os.path.isdir(str(sys.argv[2])):
        sys.exit("The output file path is not a valid directory or does not exist")


if __name__ == "__main__":
    main()