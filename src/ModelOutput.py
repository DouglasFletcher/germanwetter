

import os
import datetime
import csv
import codecs

class ModelOutput:
	# =========================================
	# == Class: ModelOutput
	# == Purpose: write data to flatfile
	# == Inputs: dictionary
	# == public methods: outputFile, setDataOut
	# =========================================

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
		# output folder
		if not os.path.exists(self.__location):
			os.makedirs(self.__location)
		for key, data in self.__dataOut.iteritems():
			# create file
			print("creating flatfile for: " + key)
			strTime = str(datetime.date.today()).replace("-","_")
			fileName = self.__location + key + "_"+ strTime + ".txt"
			# write data to file
			print("writing data to: " + key + "_"+ strTime + ".txt")
			with codecs.open(fileName, 'w', encoding="ISO-8859-1") as fileRef:
				for row in data:
					rowlen = len(row) - 1
					for i, val in enumerate(row):
						if isinstance(val, unicode):
							if len(val) != 0:
								fileRef.write(val)
							else:
								fileRef.write(str(None))
						else:
							fileRef.write(str(val))
						# seperator
						if i == rowlen:
							fileRef.write("\n")
						else:
							fileRef.write(", ")
			fileRef.close()


	def outputFile(self):
		# ================
		# Method purpose:
		#	write all data
		# ================
		self.__writeFileRef()
