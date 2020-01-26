#!python [optional-arg]
# -*- coding: utf-8 -*-

"""
This Code is used to process the data collected from the ADC Sled on
the Space System Lab's UMD 2019 Rocksat X robotic payload.

This program takes the data file that is generated by ADCSled2Dat.py
and converts the intermediate raw values into real currents. Although
this could have been incorporated into the first file it was felt to
be prudent to pull this into a separate program to be able to reduce
the memory load on the system when processing a bunch of files in a row

This program also reads in a configuration file from the current working
directory that contains the calibration data from the sensors as a yaml
file. This will allow for easy to parse and read calibration values for
the system. The configuration file must exist in the path relative to 
this program.

../config/ADCSledCurrentSenseCalbration.yaml

This tool will accept commands as follows and is written in Python 3

python3 RawADC2windingCurrents.py /Input/File/Path.dat /Output/Files/Folder/

MIT License
"""

# Futures
from __future__ import print_function
# […]

# Built-in/Generic Imports
import os
import sys
import yaml
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
def main():
    if (len(sys.argv) != 3):
        print("wrong arg")
        sys.exit("This command does not have a valid number of arguments. The format is\nCommand /input/File/Path.dat /output/files/path/ ")

    
    #Check to see if the first command line argument is a file
    if not os.path.isfile(str(sys.argv[1])): 
        sys.exit("The input file given is not a file")   
    else:
        inputFileName = str(sys.argv[1])
        
    #Check to see if the second command line argument is a directory
    if (not os.path.isdir(str(sys.argv[2]))):
        sys.exit("The output file path is not a valid directory or does not exist")
    else:
        outputDirectory = str(sys.argv[2])

    #At this point we can assume the file is good and the save directory exists.
    #We will check to see if the save files exist already later

    #open the file in read only mode
    inFile = open(inputFileName, "r")

    #separate the file into individual lines
    inputLines  = inFile.readlines()

    #Load in the values stored in the YAML file
    stream = open("../config/ADCSledCurrentSenseCalbration.yaml", 'r')
    dictionary = yaml.load(stream)
    for key, value in dictionary.items():
        print (key + " : " + str(value))
    
    # Code to here is good but needs fixing beyond this


    # The first 4 lines are human readable garbage and need to be tossed. The first 
    # line with real data is line index 4

    #print(inputLines[3])
    #print(outputDirectory)

    # Create the 3 output files for the different data types
    
    # Check to see if the file exists
    if os.path.isfile(outputDirectory+"ADCCurrentReadings.dat"):
        print("The output file for the current sensor data exist. Overwrite? [y/n]")
        userInput = input()
        if userInput[0] == "y" or userInput[0] == "Y":
            os.remove(outputDirectory+"ADCCurrentReadings.dat")
        else:
            sys.exit("Program exiting so as to not overwrite the file")

    # Open file for output failing nicely if it already exists
    outFileCurrent = open(outputDirectory+"ADCCurrentReadings.dat","x")

    # Check to see if the file exists
    if os.path.isfile(outputDirectory+"IMUReadings.dat"):
        print("The output file for the IMU data exist. Overwrite? [y/n]")
        userInput = input()
        if userInput[0] == "y" or userInput[0] == "Y":
            os.remove(outputDirectory+"IMUReadings.dat")
        else:
            sys.exit("Program exiting so as to not overwrite the file")

    # Open file for output failing nicely if it already exists
    outFileIMU = open(outputDirectory+"IMUReadings.dat","x")

    # Check to see if the file exists
    if os.path.isfile(outputDirectory+"IMUSync.dat"):
        print("The output file for the IMU Sync data exist. Overwrite? [y/n]")
        userInput = input()
        if userInput[0] == "y" or userInput[0] == "Y":
            os.remove(outputDirectory+"IMUSync.dat")
        else:
            sys.exit("Program exiting so as to not overwrite the file")

    # Open file for output failing nicely if it already exists
    outFileIMUSync = open(outputDirectory+"IMUSync.dat","x")

    # This is where the Main code for the program goes


    # This allows the file to run as stand alone or as called to run by another program.
if __name__ == "__main__":
    main()