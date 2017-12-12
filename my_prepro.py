#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:10 2017

@author: adleman
"""

import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
    #do something cool
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*_task-bart_bold.nii.gz')):
        input=item
        output_path=item.split('.')[0]
        output=output_path+('_brain')
#        if os.path.exists(input)== True:
#            print('cool!!!')
#        else:
#            print('yikes')
#       pdb.set_trace()
        os.system('bet %s %s -F'%(input,output))
        
def main():
    #load in all the global variables prepro needs, right now this is just the path to the data
    basedir='/Users/adleman/Downloads/data'
    prepro(basedir) #call prepro to do cool things
main()