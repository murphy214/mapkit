import math
import pandas as pd
import mapkit as mk
# gets coords from a string representation of coords
def get_cords_json(coords):
	data = '{"a":%s}' % coords
	data = json.loads(data)	
	return data['a']

def num2deg(xtile, ytile, zoom):
  n = 2.0 ** zoom
  lon_deg = xtile / n * 360.0 - 180.0
  lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
  lat_deg = math.degrees(lat_rad)
  return (lon_deg, lat_deg)

def get_bounds(x,y,z):
	pt1 = num2deg(x,y,z)

	pt2 = num2deg(x+1,y+1,z)

	deltax,deltay = [(pt2[0] - pt1[0])/2.0,(pt2[1] - pt1[1])/2.0]

	return {'e':pt1[0]+deltax,'w':pt1[0]-deltax,'s':pt1[1]-deltay,'n':pt1[1]+deltay}

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return '%s/%s/%s' % (xtile, ytile,zoom)

# maps mapbox / osm coordinate precisions against a given dataframe set
# assuems the dataframe given has a 'lat' and 'long' fiel
def map_xyz(data,z):
	for i in data.columns.values:
		if 'lat' in str(i).lower():
			latheader = i
		elif 'lon' in str(i).lower() or 'lng' in str(i).lower():
			longheader = i


	data['XYZ'] = [deg2num(lat,long,z) for lat,long in data[[latheader,longheader]].values]

	return data 

# just a wrap bounds method to keep it in a comprehension
def wrapbounds(x,y,z):
	return get_bounds(int(x),int(y),int(z))


# if a dataframe contains an xyz field expands out to cardinal coords
# that can be sent into make_blocks
# lol im done
# in this context now that bad of an assumption
def map_cards(data):
	for i in data.columns.values:
		if 'xyz' in str(i).lower():
			xyzheader = i
	
	cards = pd.DataFrame([wrapbounds(*str.split(i,'/')) for i in data[xyzheader].values])
	data[['NORTH','SOUTH','EAST','WEST']] = cards[['n','s','e','w']]

	return data



'''
data = pd.read_csv('points_example.csv')

data = map_xyz(data,10)

data = map_cards(data)

data = data.groupby('XYZ').first().reset_index()

data = mk.make_colorkey(data,'XYZ')
mk.make_map([data,'blocks'])


'''