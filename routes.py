!%matplotlib
!pip install pandas

import pandas as pd
import numpy as np
URL1 = "https://vega.github.io/vega/data/airports.csv"
URL2 = "https://vega.github.io/vega/data/flights-airport.csv"
airports = pd.read_csv(URL1)
routes = pd.read_csv(URL2)

#Save  data from as CSV
airports.to_csv('my_path\\airports.csv',index=False, header=True)
routes.to_csv('my_path\\routes.csv',index=False, header=True)
airports = pd.read_csv('my_path\\airports.csv')
routes = pd.read_csv('my_path\\routes.csv')
airports['iata'].duplicated()
airports.describe()
airports.shape
origin = routes['origin'].unique()
destination = routes['destination'].unique()
flights_set = set(np.append(origin,destination))
airports_set = set(airports['iata'])
flights_set.issubset(airports_set)
val = airports['iata'].to_list()
val
indx = pd.Index(val)
indx
routes.insert(1,'Name Origin',airports.loc[indx.get_indexer(routes['origin']),'name'].values)
routes.insert(3,'Name Destination',airports.loc[indx.get_indexer(routes['destination']),'name'].values)
routes
routes.to_csv('new_flights.csv',index = False ,header = True)
