#  ----------------------------------------------------------------------------
# bus_clean.py 
# Copyright Kimi Holsapple 2022
# 
# ----------------------------------------------------------------------------- 
# Pursose : Script to clean the metro_raw.csv data.

# Goals   : - rename columns
#		    - Reformat time columns such that they are times for each bus 
#				arriving at that stop
#		    - Rename all stop values to their according bus IDs
# 		    - Remove missing values
# ----------------------------------------------------------------------------- 

# ----------------------------------------------------------------------------- 
#          				DATA SET DESCRIPTION
#
# Santa_Cruz_METRO_raw_complete.csv
#	 buses in dt set 19,20,18,15,10
#    Columns: 	Bus0621arrivesin3minutesat10 : arrival_1        
#					(date_time) tracks arrivals of bus
# 				Bus1201arrivesin122minutesat12 : 	arrival_2
#					(date_time) tracks arrival of bus 	
# 				Bus1202arrivesin62minutesat11 : arrival_3
#					(date_time) tracks arrival of bus 	
# 				Text : stop_id
#					(int) according to stop_id_dictionary @ line 40
# 				current_time -- remains unchanged **
#					(date_time)
#				adding extra column called bus_id
#					(int)  according to bus_id_dictionary @ line 
# ----------------------------------------------------------------------------- 


import pandas as pd 
import numpy as np
import csv
import sys


column_dictionary = {
						0: "arrival_1",
						1: "arrival_2",
						2: "arrival_3",
						3: "stop_id",
						4: "current_time",
						# 5: "bus_id",
					}

stop_id_dictionary = {
						# east to west routes include bus 10,20,18
						1: "2102",		# east west bookstore
						2: "1617",		# east west crown merril		
						3: "1616",		# east to west college 9/10		
						4: "1615",		# east to west science hill
						5: "2448",		# east to west RCC
						# west to east routes include bus 19, 15
						6: "2676",		# west to east bookstore
						7: "2675",		# west to east 9/10
						8: "2674",		# west to east science hill
						9: "2672",		# west to east kerr hall
						10: "2671",		# west to east RCC
					}



bus_id_dictionary = {
						("Rachel Carson", "Main Gate"): stop_id_dictionary.get(5),
						("Science Hill", "Main Gate"): stop_id_dictionary.get(4),
						("College 9", "Main Gate"): stop_id_dictionary.get(3),
						("Crown", "Main Gate") : stop_id_dictionary.get(2),	# east to west 10,20,18 bus
						("Bookstore", "Main Gate"): stop_id_dictionary.get(1),

						("Rachel Carson", "West "): stop_id_dictionary.get(10),
						("Kerr Hall", "West " ) : stop_id_dictionary.get(9),
						("Science Hill", "West "): stop_id_dictionary.get(8),
						("College 9", "West "): stop_id_dictionary.get(7),					# 19,15
						("Bookstore", "West "): stop_id_dictionary.get(6),
					}

bus_name_dictionary = {
						"on 19": 19,
						"on 18" : 18,
						"on 10": 10,
						"on 20": 20,					
						"on 15": 15,
					}




raw_df = pd.read_csv('/Users/kimigrace/Desktop/Math140/scrape/Santa_Cruz_METRO_raw_complete.csv')
raw_df.rename(columns={'Bus0621arrivesin3minutesat10': 'arrival_1'}, inplace=True)
raw_df.rename(columns={'Bus1201arrivesin122minutesat12': 'arrival_2'}, inplace=True)
raw_df.rename(columns={'Bus1202arrivesin62minutesat11': 'arrival_3'}, inplace=True)
raw_df.rename(columns={'Text': 'stop_id'}, inplace=True)
raw_df.rename(columns={'Current_time': 'current_time'}, inplace=True)

num_rows = raw_df.shape[0]
num_col = raw_df.shape[1]

bus_list = []

for column_name, column_data in raw_df.iteritems():
	
	# print("original value", value)

	for values in column_data.values:
		stop_direction = ''
		stop_name = ''
		bus_name = ''
		stop_text = str(values)

		if ( column_name == "arrival_1" or column_name == "arrival_2" or column_name == "arrival_3"):
			time_string = stop_text[-9:-1]
			time_string.strip()
			raw_df.replace(to_replace = stop_text,value = time_string, inplace = True)

		if (column_name == "stop_id"):

			if(stop_text.find('on 15') != -1):
				bus_name = bus_name_dictionary.get('on 15')
			if(stop_text.find('on 20') != -1):
				bus_name = bus_name_dictionary.get('on 20')
			if(stop_text.find('on 10') != -1):
				bus_name = bus_name_dictionary.get('on 10')
			if(stop_text.find('on 19') != -1):
				bus_name = bus_name_dictionary.get('on 19')
			if(stop_text.find('on 18') != -1):
				bus_name = bus_name_dictionary.get('on 18')

			if ( stop_text.find("Main Gate") != -1 or stop_text.find("West ") != -1 ):
				if(stop_text.find('Main Gate') != -1):
					stop_direction = "Main Gate"
				else: 
				 	stop_direction = "West "

			if(stop_text.find('Rachel Carson') != -1):
				stop_name = 'Rachel Carson'

			if(stop_text.find('Kerr Hall') != -1):
				stop_name = 'Kerr Hall'

			if(stop_text.find('Science Hill') != -1):
				stop_name = 'Science Hill'

			if(stop_text.find('College 9') != -1):
				stop_name = 'College 9'

			if(stop_text.find('Bookstore') != -1):
				stop_name = 'Bookstore'

			if(stop_text.find('Crown') != -1):
				stop_name = 'Crown'
				stop_direction = "Main Gate"

			if(stop_text.find('xcssh') != -1):
				stop_name = 'Crown'
				stop_direction = "Main Gate"
					
			numeric_stop_id = ( bus_id_dictionary.get( (stop_name, stop_direction)) )

			raw_df.replace(to_replace = stop_text,value = numeric_stop_id, inplace = True)
			bus_list.append(bus_name)
			# 
				# raw_df.loc[raw_df[column_name]==stop_text] = numeric_stop_id
				
	# print("new value: ", value)


raw_df["bus_id"] = bus_list

# # clean the data
# for column_no in range(4):
# 	column = column_dictionary.get(column)
# 	print("Working on " + column + " ...")
# 	for i in range(num_rows):
# 		match column_no:
# 			# arrival_1
# 			case 0:		
# 				df[column_dictionary.get(column)] = df[column].replace({'P': 'A'}
# 			case 1:

# 			case 2:

# 			case 3:



raw_df.to_csv("Santa_Cruz_METRO_complete.csv", index=False)

print(num_rows)

