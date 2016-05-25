
from sqlalchemy import Column, String, Integer, Float
from enum import Enum

class APIObjects(Enum):

	#== API objects of the form:
	#==	{"filename form on ftp":
	#==		[
	#==			"filter column position (string)"
	#==			, "column metadata (dictionary): [type, position]"
	#==		]
	#==	}

	# object Stationsmetadaten_*.txt
	fileMeta = {
		"stationsmetadaten":[
			None
			, {"Stations_id":[String,0],"Stationshoehe":[Float,1]
				,"Geogr.Breite":[Float,2],"Geogr.Laenge":[Float,3]
				,"von_datum":[String,4],"bis_datum":[String,5]
				,"Stationsname":[String,6]
			}
		]
	}

	# object produkt_klima_Tageswerte_*.txt
	fileData = {
		"produkt_klima":[
			1
			, {"STATIONS_ID":[String,0] ,"MESS_DATUM":[String,1]
				,"QUALITAETS_NIVEAU":[Float,2],"LUFTTEMPERATUR":[Float,3]
				,"DAMPFDRUCK":[Float,4],"BEDECKUNGSGRAD":[Float,5]
				,"LUFTDRUCK_STATIONSHOEHE":[Float,6],"REL_FEUCHTE":[Float,7]
				,"WINDGESCHWINDIGKEIT":[Float,8],"LUFTTEMPERATUR_MAXIMUM":[Float,9]
				,"LUFTTEMPERATUR_MINIMUM":[Float,10]
				,"LUFTTEMP_AM_ERDB_MINIMUM":[Float,11]
				,"WINDSPITZE_MAXIMUM":[Float,12],"NIEDERSCHLAGSHOEHE":[Float,13]
				,"NIEDERSCHLAGSHOEHE_IND":[Float,14],"SONNENSCHEINDAUER":[Float,15]
				,"SCHNEEHOEHE":[Float,16],"eor":[String,17]
			}
		]
	}

