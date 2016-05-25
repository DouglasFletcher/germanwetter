"""
Created on Mon Nov 24 10:30:51 2015
@author: douglas.fletcher
purpose: get raw data from dwd ftp server
		 save to staging files
"""

# Global libraries
import os
import time
import datetime

# set working dir
cwd = os.getcwd()
os.chdir(cwd)

# module classes
from src.FtpConnect import FtpConnect
from src.SaveToModel import SaveToModel
from src.ModelOutput import ModelOutput

if __name__ == "__main__":

	start_time = time.time()

	# recent data loaded to ftp server
	source = "/pub/CDC/observations_germany/climate/daily/kl/recent/"
	days = 30

	# ftp data location
	ftpConn = FtpConnect(source = source, days = days)

	# model output
	modOutputInst = ModelOutput()

	# process data
	SaveToModelInst = SaveToModel(ftpConn, modOutputInst)
	SaveToModelInst.ftpToModel()

	print("--- %s seconds ---" % (time.time() - start_time))




