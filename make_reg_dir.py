#!/usr/bin/python


import os
import glob

# This is the path to the directory that contains all the subject directories
basedir = '/Users/adleman/Downloads/data/derivatives/task/'

# Grab all the paths to the bart.feat directories

barts = glob.glob("%s/sub*/bart.feat"%(basedir))

# Now we'll march through each bart.feat and create a reg directory and the files it needs based on my tutorial here: http://mumfordbrainstats.tumblr.com/post/166054797696/feat-registration-workaround
#The new ident.mat file tells FSL NOT to move the data at all and not interpolate in any way
#The third line uses the mean_func that is in the directory (the average of the functional data) to be the standard so that it doesn't change the voxel sizes
for dir in barts:
    os.system("mkdir %s/reg"%(dir))
    os.system("cp $FSLDIR/etc/flirtsch/ident.mat %s/reg/example_func2standard.mat"%(dir))
    os.system("cp %s/mean_func.nii.gz %s/reg/standard.nii.gz"%(dir, dir))
    
