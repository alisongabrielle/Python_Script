#Purpose: Convert multiple in a file from .xlsx files to .csv

#importing pandas as pd
import pandas as pd
import os

dirname = 'C:/Users/gonzaa14/OneDrive - Southern California Edison/Scripts/'
dir = os.fsencode(dirname)

for currentfile in os.listdir(dir):
	filename = os.fsdecode(currentfile)
	if '.xlsx' in filename:
		print("opening...",filename)
		read_file = pd.read_excel(dirname + filename, 'Completed Events')
		read_file.to_csv (filename.replace('.xlsx', '.csv'), index = None, header=True)
			
print("Scripting Done!")

