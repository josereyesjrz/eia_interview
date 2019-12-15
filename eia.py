import requests
import json
from statistics import mean, stdev
from os import environ

# get_quarter(int) -> string
# takes a month and returns the quarter
# it belongs to as string to use as key
# for gas_per_quarter dictionary
def get_quarter(month):
	if 1 <= month <= 3:
		return "Q1"
	elif 4 <= month <= 6:
		return "Q2"
	elif 7 <= month <= 9:
		return "Q3"
	elif 10 <= month <= 12:
		return "Q4"

# series_id specifies which data set you want to get
# in particular, ELEC.CONS_TOT.NG-TX-99.M has the
# total consumption of natural gas in thousand McF
# per month in Texas
parameters = {
	"api_key": environ['API_KEY'],
	"series_id": "ELEC.CONS_TOT.NG-TX-99.M",
	"start": 201801,
	"end": 201812
}

# try to fetch from endpoint
try:
	response = requests.get("https://api.eia.gov/seriesqwsadx", params=parameters)
	response.raise_for_status()

# if connection unsuccessful raise and print error info
except requests.exceptions.HTTPError as err:
	print(f"HTTP error: {err.response.status_code}")

else:
	# retrieve the data we care about
	data = response.json()['series'][0]['data']
	# retrieve unit of data for later printing of statistics
	units = response.json()['series'][0]['units']

	# dict to store gas consumption per quarter
	gas_per_quarter = {"Q1":[], "Q2":[], "Q3":[], "Q4":[]}

	# since the date format given is YYYYMM, splice the
	# last two chars from date, cast to int and save as
	# month variable. then append consumption value into
	# corresponding quarter in gas_per_quarter
	for date, val in data:
		month = int(date[-2:])
		gas_per_quarter[get_quarter(month)].append(float(val))

	# retrieve data per quarter and output statistics
	print("Total consumption of natural gas in Texas in 2018")
	print("Quarterly statistics:\n")
	for quarter in gas_per_quarter.keys():
		print(f"{quarter}:")
		print(f"average: {mean(gas_per_quarter[quarter])}")
		print(f"standard deviation: {stdev(gas_per_quarter[quarter])}")
		print(f"max value: {max(gas_per_quarter[quarter])}")
		print(f"min value: {min(gas_per_quarter[quarter])}")
		print("")