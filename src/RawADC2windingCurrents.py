#!python [optional-arg]
# -*- coding: utf-8 -*-

"""
This Code is used to process the data collected from the ADC Sled on
the Space System Lab's UMD 2019 Rocksat X robotic payload.

This program takes the data file that is generated by ADCSledRaw2Dat.py
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

This tool will accept commands as follows and is written in Python 3 and
expecting input for files in Unix style

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
# Get the Version number for the code here
__version__ = "unknown"
try:
    from _version import __version__
except ImportError:
    # We're running in a tree that doesn't have a _version.py, so we don't know what our version is.
    pass
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
__maintainer__ = 'Nicholas M Limparis'
__email__ = 'nicholas@github.limpar.is'
__status__ = 'Dev'

# Get configuration values from the YAML file
with open('config/ADCSledCurrentSenseCalibration.yaml') as configFile:
    configData = yaml.safe_load(configFile) #, Loader=yaml.FullLoader)

#Tests to make sure the Yaml file loaded properly
#print(yaml.dump(configData))
#print(configData["ADCBits"])

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
        dataFileNameList = inputFileName.split(os.sep)
        dataFileNameSplit = dataFileNameList[len(dataFileNameList)-1].split(".") # This gives us the final part of the data filename string
        dataFileName = dataFileNameSplit[0]



        
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

    # we are done with the input file so lets close it now
    inFile.close()

    #Load in the values stored in the YAML file
    ######### Trying the input method that loads the config file as a dictionary
   # stream = open("../config/ADCSledCurrentSenseCalbration.yaml", 'r')
   # dictionary = yaml.load(stream)
    #for key, value in dictionary.items():
    #    print (key + " : " + str(value))
    
    # Code to here is good but needs fixing beyond this


    # Create the 3 output files for the different data types
    
    # Check to see if the ADC Current readings file exists
    if os.path.isfile(outputDirectory + dataFileName + "_ADCCurrentReadings.dat"):
        print("The output file for the current sensor data exist. Overwrite? [y/n]")
        userInput = input()
        if userInput[0] == "y" or userInput[0] == "Y":
            os.remove(outputDirectory + dataFileName + "_ADCCurrentReadings.dat")
        else:
            sys.exit("Program exiting so as to not overwrite the ADC Current readings file")

    # Open file for output failing nicely if it already exists
    outFileCurrent = open(outputDirectory + dataFileName + "_ADCCurrentReadings.dat","x")

    # Check IMU Readings file to see if the file exists
    if os.path.isfile(outputDirectory + dataFileName + "_IMUReadings.dat"):
        print("The output file for the IMU data exist. Overwrite? [y/n]")
        userInput = input()
        if userInput[0] == "y" or userInput[0] == "Y":
            os.remove(outputDirectory + dataFileName + "_IMUReadings.dat")
        else:
            sys.exit("Program exiting so as to not overwrite the IMU Readings file")

    # Open IMU Readings file for output failing nicely if it already exists
    outFileIMU = open(outputDirectory + dataFileName + "_IMUReadings.dat","x")

    # Check IMU Sync File to see if the file exists
    if os.path.isfile(outputDirectory + dataFileName + "_IMUSync.dat"):
        print("The output file for the IMU Sync data exist. Overwrite? [y/n]")
        userInput = input()
        if userInput[0] == "y" or userInput[0] == "Y":
            os.remove(outputDirectory + dataFileName + "_IMUSync.dat")
        else:
            sys.exit("Program exiting so as to not overwrite the IMU Sync file")

    # Open file for output failing nicely if it already exists
    outFileIMUSync = open(outputDirectory + dataFileName + "_IMUSync.dat","x")

    # This is where the Main code for the program goes

    # So now everything is now open!

    # The first 4 lines are human readable garbage and need to be not included in the data files. The first 
    # line with real data is line index 3

    #print(inputLines[3])
    #print(outputDirectory)
    
    # Ok now we need to sort out the files into their respective output files
    for i in range(4,len(inputLines)):  #4 is the index of the first line of data
        parsedLineList = inputLines[i].split(",")
        #First index is the datatype (49 is ADC readings,50 is IMU Readings, 51 is IMUSync)
        if parsedLineList[0].isnumeric():
            if int(parsedLineList[0]) == 49:
                #Copy rest of parsed line to outFileCurrent after converting to currents
                #49,micros,adc0,adc1,adc2
                # conversion from adc value to
                adc2Volts = configData["ADCMaxVDC"] / configData["ADCNoCurrent"]
                adc2Amps = configData["CurrentRange"][1] / configData["ADCNoCurrent"]
                current0 = (int(parsedLineList[2]) - configData["ADCNoCurrent"] ) * adc2Amps
                current1 = (int(parsedLineList[3]) - configData["ADCNoCurrent"] ) * adc2Amps
                current2 = (int(parsedLineList[4]) - configData["ADCNoCurrent"] ) * adc2Amps
                outFileCurrent.write(str(parsedLineList[1]) + "," + str(current0) + "," + str(current1) + "," + str(current2) + "\n") # Timestamp (micros), CurrentPhase1 ,CurrentPhase2, CurrentPhase3
                
            elif int(parsedLineList[0]) == 50:
                #Copy rest of parsed line to outFileIMU after converting to human readable values
                #50,micros,AccelX,GyroX,MagX,AccelY,GyroY,MagY,AccelZ,GyroZ,MagZ

                # We are going to go with uncalibrated data for the moment and store it to a file


                outFileIMU.write(str(parsedLineList[1]) + "," + parsedLineList[2] + "," + parsedLineList[5] + "," + parsedLineList[8] + "," + parsedLineList[3] + "," + parsedLineList[6] + "," + parsedLineList[9] + "," + parsedLineList[4] + "," + parsedLineList[7] + "," + parsedLineList[10]) # Timestamp (micros), AccelX, AccelY, AccelZ, GyroX, GyroY, GyroZ, MagX, MagY, MagZ
                pass
            elif int(parsedLineList[0]) == 51:
                #Record the timestamps in Micro seconds for a timesync from the main computer to sync the system IMUs
                #51,microsAtInteruptSync
                outFileIMUSync.write(str(parsedLineList[1]) + "\n") # Timestamp (micros) of sync pulse
            else:
                # not one of the expected data types raise an error
                raise SystemExit("Unexpected data type on line " + str(i) + " of data file " + inputFileName)
        else:
            raise SystemExit("Malformed Data on line "+ str(i) + " of Data File: " + inputFileName)




    # This allows the file to run as stand alone or as called to run by another program.
if __name__ == "__main__":
    main()
