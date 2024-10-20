##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2024
## Author: desa.bolger@duke.edu (for ENV859)
##---------------------------------------------------------------------

#import modules
import sys, os, arcpy 