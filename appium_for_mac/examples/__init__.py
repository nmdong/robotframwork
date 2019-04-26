
#!/usr/bin/python

#Python default packages used in this lib.
import sys, os

##Get framework base path from environment variable
##which is set in user .basrhrc file.
base_path = os.environ['examples']

##Lib PATH SET
sys.path.append(base_path+'Library')

