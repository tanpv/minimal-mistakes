# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# scope = ['https://spreadsheets.google.com/feeds']

# credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret_211939942558-a1cn854v4llmvpbrtdhkbrko7fuhrg48.apps.googleusercontent.com.json', scope)

# gc = gspread.authorize(credentials)

# wks = gc.open("12EmLWnjqYMVTfrFlGxnIE4sMCDgYGIWHF-62hfXQtCU").sheet1

import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('gspread-ffbbb9529042.json', scope)
client = gspread.authorize(creds)
 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Require API of EmotivBCI from Product Team").sheet1
 
# Extract and print all of the values
list_of_hashes = sheet.get_all_records()

print sheet.acell()


# for h in list_of_hashes:
# 	print h