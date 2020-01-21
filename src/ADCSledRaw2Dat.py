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

    #seperate the file into individual lines
    inputLines  = inFile.readlines()

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

    # OK so now we have all of our files open for writing 
    # or have quit gracefully to allow the user to fix the issue

    # Now begins the sorting of the data into it's proper file while 
    # stripping the data type header.  This will make each file a 
    # Time stamped (micros) from the microcontroller that recorded it
    # The sync pulse from the main C&DH system is recorded in IMUSync

    #The first 4 lines are not data so we strip them here
    for index in range(4,len(inputLines)):
        typeLocation = inputLines[index].find(",")
        dataSplit = inputLines[index].split(",")
        if dataSplit[0] = "49"
            #This is the first data type that represents the data for 

    # This allows the file to run as stand alone or as called to run by another program.
if __name__ == "__main__":
    main()
