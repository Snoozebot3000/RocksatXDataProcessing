# Rocksat-X Data Processing
This repo is for the Code tidbits for taking the raw data and processing it into data files

This is used on the UMD 2019 Rocksat-X payload.

## Running the ADC and IMU software

```bash
#Running the ADCSledRaw2Dat.py
python3 ADCSledRaw2Dat.py /Input/File/Path.dat /Output/Files/Folder/
#Running the RawADC2windingCurrents.py
python3 RawADC2windingCurrents.py /Input/File/Path.dat /Output/Files/Folder/

```

## Tasks left to do (ADC & IMU)
 - [ ] Figure out what variables need to be stored in the yaml file
 - [ ] Get yaml parsing working
 - [ ] Begin the code for parsing the raw IMU values
 - [ ] write the python wrapper for the subprograms that runs through a yaml list of data files to be processed
 - [ ] profit? :rocket:

 ## Tasks for Processing the load cell data
 - [ ] 



