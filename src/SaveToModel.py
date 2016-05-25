
from src.APIZipFolders import APIZipFolders

class SaveToModel:
	# ===========================================
	# == Class: Save to Model
	# == Purpose: worker class to output all data
	# == from ftp to model
	# == Inputs: ftp connection, model output
	# == Methods: ftpToModel
	# ===========================================

	def __init__(self, ftpConn, modOutput):
		# ====
		# init
		# ====
		self.__ftpConn = ftpConn
		self.__modOutput = modOutput

	def ftpToModel(self):
		# ========================
		# Method purpose:
		#	iterates through files
		#	downloads from server
		#	saves to model
		# ========================
		insertdata = []
		# ftp tasks
		self.__ftpConn.ftpRunTasks()

		# get zipfile properties
		fileLoc = self.__ftpConn.getFtpServ()+self.__ftpConn.getSource()
		startDate = self.__ftpConn.getStartDate()
		ZipFolderList = self.__ftpConn.getZipFolderList()

		# zip folder init
		zipFolderInst = APIZipFolders(fileLoc, startDate)

		# file properties - headers
		headers = zipFolderInst.fileHeaders()
		insertdata.append(headers)

		# unpack all data for each zipfile and append
		for row, zipFile in enumerate(ZipFolderList):
			# set Zip name
			zipFolderInst.setZipFile(zipFile)
			# get Zip data
			datareturn = zipFolderInst.zipFolderRunTasks()
			insertdata.append(datareturn)

		# combined dictionary objects
		dataOut = {}
		for i, zipOut in enumerate(insertdata):
			for keys, values in zipOut.iteritems():
				if i == 0:
					dataOut[keys] = values
				else:
					dataOut[keys] += values

		# output data
		self.__modOutput.setDataOut(dataOut)
		self.__modOutput.outputFile()
