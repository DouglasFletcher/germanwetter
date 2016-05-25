

import os
import datetime
import csv

class ModelOutput:
	# ============================================
	# == Class: OutFileLoc
	# == Purpose: write data to flatfile
	# == Inputs: dictionary
	# == Methods: (methods exposed) outputFile
	# ============================================

	def __init__(self):
		self.__location = os.getcwd() + "\\output\\"
		self.__dataOut = []

	def setDataOut(self, dataOut):
		# ===================
		# Method purpose:
		#	pass data to save
		# ===================
		self.__dataOut = dataOut

	def __writeFileRef(self):
		# ======================
		# Method purpose:
		#	create file instance
		# ======================
		for key, value in self.__dataOut.iteritems():
			# create file
			print("creating flatfile for: " + key)
			strTime = str(datetime.date.today()).replace("-","_")
			fileName = self.__location + key + "_"+ strTime + ".txt"
			# data
			alldata = []
			for row in value:
				alldata.append(str(row).strip("[]"))
			# write data to file
			print("writing data to: " + key + "_"+ strTime + ".txt")
			with open(fileName, 'w') as fileRef:
				spamwriter = csv.writer(fileRef, delimiter='\n')
				spamwriter.writerow(alldata)
			fileRef.close()

	def outputFile(self):
		# ================
		# Method purpose:
		#	write all data
		# ================
		self.__writeFileRef()
