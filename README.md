# US Energy Information Administration info retrieval

As part of the interview process for Geodesic Energy LLC I was tasked to come up with a program that connected to some webservice endpoint, fetched a time series with a year's worth of info, and to output simple statistics per quarter (every three months).

The API I am using is provided by the [US Energy Information Administration](https://www.eia.gov/opendata/) (EIA). I found it using the [Data.gov](https://www.data.gov/) service which lists many of the freely available US government data endpoints.

To use this program first you have to request an API key from the EIA [here](https://www.eia.gov/opendata/register.php). Then, you must export an API_KEY environment variable with yout API key. The particular dataset I'm fetching is the total consumption of natural gas in Texas in the year 2018 and can be found [here](https://www.eia.gov/opendata/qb.php?category=432&sdid=ELEC.CONS_TOT.NG-TX-99.M). API documentation can be found [here](https://www.eia.gov/opendata/commands.php).
