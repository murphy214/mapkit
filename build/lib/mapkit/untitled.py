
# makes a test block and returns the points for the index
def make_test_block5(ultindex,number):
	from mapkit import unique_groupby
	#indexdict = read_json('states_ind.json')
	extrema = {'n': 50.449779,'s': 20.565774,'e':-70.493017,'w':-130.578836}
	data = pg.random_points_extrema(number,extrema)
	data = ult.map_table(data,12,map_only=True)
	s = time.time()

	data = ult.area_index(data,ultindex)
	print 'Time for just indexing: %s' % (time.time() - s)
	data = data[data['AREA'].str.len() > 0]
	data = unique_groupby(data,'AREA',hashfield=True,small=True)
	return data