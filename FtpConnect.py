
from ftplib import FTP
from re import search
import datetime

class FtpConnect:
	# ===================================================
	# == Class:  
	# == Purpose: 
	# == Inputs:  
	# == Methods:
	# =================================================== 

	def __init__(self, source, days):
		# ========================= 
		# ftp connection parameters
		# ========================= 
		self.ftpServ = "ftp-cdc.dwd.de"
		self.source = source
		self.zipFolderNames = []
		self.startDate = None
		self.days = days

	def getFtpServ(self):
		# ==================
		# get zip file names
		# ==================
		return self.ftpServ

	def getSource(self):
		# ==================
		# get zip file names
		# ==================
		return self.source

	def getStartDate(self):
		# ==================
		# get startDate
		# ==================
		return self.startDate

	def getZipFolderList(self):
		# ==================
		# get zip file names
		# ==================
		return self.zipFolderNames

	def __setStartDate(self):
		# ==================
		# set startDate
		# ==================
		now = datetime.datetime.now()
		dif = datetime.timedelta(self.days)
		act = now - dif
		self.startDate = int(str(act.year)+str(act.strftime("%m"))+str(act.strftime("%d")))

	def __zipFolderList(self):
		# ============================
		# get zipfiles from ftp server
		# ============================
		print "Getting .zip filesnames from ftp server ..." + "\n"
		# clear data contents
		self.zipFolderNames = []
		try:
			# ftp connection
			server = FTP(self.ftpServ)
			server.login()
			# change dir
			server.cwd(self.source)
			# get filenames
			ls = []
			ls = server.nlst()
			# get zip files only
			self.zipFolderNames = [x for x in ls if search('zip', x)]
			# message
			server.quit()
		except:
			print "cannot login to ftp server"

	def ftpRunTasks(self):
		# =================
		# run private tasks
		# =================
		self.__setStartDate()
		self.__zipFolderList()
