import json
import pandas as pd
import os
import time
import nlgeojson as nl
import geopandas as gpd
from shapely.geometry import shape

# returns the feature strings of a given geojson
def split_features(data):
	data = str.replace(data,', ',',')
	data = str.replace(data,': ',':')
	data = str.replace(data,'} ','}')

	data = str.split(data,'{"type":"FeatureCollection","features":')[1]


	data = data[1:-2]
	data = str.split(data,'},{')

	count = 1
	for i in data[1:-1]:
		i = '{%s}' % i
		data[count] = i
		count += 1

	data[0] = data[0] + '}'
	data[-1] = '{' + data[-1]

	return data


# gets coords and properties
def read_coords_props(feat):
	coords = str.split(feat[1:-1],'"coordinates":')[1]
	coords = str.split(coords,']]]')[0] + ']]]'

	properties =  str.split(feat,'"properties":')[1]
	properties = str.split(properties,'}')[0] + '}'
	properties = json.loads(properties)
	properties['COORDS'] = coords
	return properties


# gets coords and properties
def read_coords_props2(feat):
	coords = str.split(feat[1:-1],'"geometry":')[1]
	coords = str.split(coords,']},')[0] + ']}'



	properties =  str.split(feat,'"properties":')[1]
	properties = str.split(properties,'}')[0] + '}'
	properties = json.loads(properties)
	
	coords = json.loads(coords)

	coords = shape(coords)
	properties['geometry'] = coords

	return properties



def convert_geojson(filename,remove=False,return_data=False,load_array=False,return_gpd=False):
	with open(filename,'rb') as f:
		data = f.read()

	outcsv = str.split(filename,'.geojson')[0] + '.csv'
	data = split_features(data)
	if return_data == False and return_gpd == False:
		data = pd.DataFrame([read_coords_props(i) for i in data])
	elif return_gpd == True:
		data = pd.DataFrame([read_coords_props2(i) for i in data])
		data = gpd.GeoDataFrame(data,geometry='geometry')
		return data
	else:
		if load_array == True:
			data = pd.DataFrame([read_coords_props(i) for i in data])
			data.COORDS = data.COORDS.map(load_to_array)
			return data
		return pd.DataFrame([read_coords_props(i) for i in data])
	data.to_csv(outcsv,index=False)
	if remove == True:
		os.remove(filename)

# loads a coord string as an array
def load_to_array(coords):
	data = '{"a":%s}' % coords
	data = json.loads(data)	
	return data['a']



def read_file_gpd(filename):	
	data = convert_geojson(filename,return_gpd=True)
	return data	
	'''
	cols = data.columns.values
	newcols = []
	for i in cols:
		if i == 'COORDS':
			newcols.append('geometry')
		else:
			newcols.append(i)
	data.columns = newcols
	'''




