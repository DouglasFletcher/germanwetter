
# database schema
from APIObjects import APIObjects

# standard imports
from zipfile import ZipFile
import urllib2
import io
from re import search
from sqlalchemy import 	String, Integer, Float


class APIZipFolders:
	# ==============================================
	# == Class: APIZipFolders
	# == Purpose: extract data from zipfile on ftp
	# == Inputs: zipfile name, location, start date 
	# == of data to extract
	# == dependencies: APIObjects
	# == Public methods: zipFolderRunTasks()
	# ==============================================

	def __init__(self, fileLoc, startDate):
		# =========================
		# zipFile from ftp server
		# =========================
		self.__zipFile = None
		self.__fileLoc = fileLoc
		self.__startDate = startDate
		self.__zipFolderDict = {}
		self.__zipFolderExtract = None
		self.__InsertData = {}


	def setZipFile(self, zipFile):
		# ============
		# set zip file
		# ============
		self.__zipFile = zipFile


	def __requestZipFolder(self):
		# ============
		# unzip folder
		# ============
		self.__zipFolderExtract = None
		# get from zipfolder location
		print "requesting zip file : " + self.__zipFile + " from server"
		request = urllib2.Request("ftp://"+self.__fileLoc+self.__zipFile)
		response = urllib2.urlopen(request)
		memfile = io.BytesIO(response.read())
		# extract zip file
		self.__zipFolderExtract = ZipFile(memfile, 'r')


	def __requestFileNames(self):
		# ===============================
		# zip file with filenames mapping
		# ===============================
		request = urllib2.Request("ftp://"+self.__fileLoc+self.__zipFile)
		response = urllib2.urlopen(request)
		memfile = io.BytesIO(response.read())
		self.__zipFolderDict = {}
		with ZipFile(memfile, 'r') as zipFolder:
			txts = [x for x in zipFolder.namelist() if search('txt', x)]
			self.__zipFolderDict[self.__zipFile] = txts


	def fileHeaders(self):
		# ================
		# get data headers
		# ================
		headerOut = {}
		for objs in APIObjects:
			# header properties
			apiobjkey = objs.value.keys()[0]
			apiobjcol = objs.value.values()[0][1].keys()
			headerOut[apiobjkey] = [apiobjcol]
		return headerOut


	def __downloadData(self):
		# =============
		# download data
		# =============
		# extaction rules
		fnFlt = lambda x: float(x.strip()) if x.strip() != "-999" else None
		fnStr = lambda x: x.strip() if x.strip() != "-999" else None
		# initialize dictionary
		self.__InsertData = {}
		# api objects to extract
		for objs in APIObjects:
			# api obj key
			apiobjkey = objs.value.keys()[0]
			apiobjval = objs.value.values()[0][1]
			filterkey = objs.value.values()[0][0]
			# data filenames
			fileNames = [x for x in self.__zipFolderDict[self.__zipFile] \
			if search(apiobjkey, x.lower())][0]
			# start reading data process
			print "\t 1. Unzipping data from file : " + str(fileNames)
			readdata = self.__zipFolderExtract.read(fileNames)
			# init datainsert for rawdata
			self.__insertData = []
			# failed row counter
			rowdatafails = 0
			# extract data by row
			zipTrans = []
			for line, row in enumerate(readdata.splitlines()):
				linesplit = row.replace(" ","").split(";")
				rowTrans = []
				# data starts row 1 - length check
				if line > 0 and len(linesplit) == len(apiobjval):
					# check for filtering data
					if filterkey != None:
						if int(linesplit[filterkey]) <= self.__startDate:
							continue
					# for each column apply extract rules
					try:
						for col, coltype in enumerate(apiobjval):
							# get col properties
							colVar = apiobjval[coltype][0]
							colPos = apiobjval[coltype][1]
							# apply extraction rules
							if colVar == Float:
								colrow = fnFlt(linesplit[colPos])
							elif colVar == String:
								colrow = fnStr(linesplit[colPos])
							else:
								raise ValueError("type not: Float or String")
							# save row
							rowTrans.append(colrow)
						# save file data
						zipTrans.append(rowTrans)
					except:
						# counter of failed insert rows
						rowdatafails += 1
			# progress of data extraction
			print "\t 2. extraction report : "
			print "\t\t successful : " + str(len(zipTrans)) + " rows "
			print "\t\t failed : " + str(rowdatafails) + " rows" + "\n"
			# save data
			self.__InsertData[apiobjkey] = zipTrans


	def zipFolderRunTasks(self):
		# ==================
		# run zip file tasks
		# ==================
		self.__requestFileNames()
		self.__requestZipFolder()
		self.__downloadData()
		return self.__InsertData

