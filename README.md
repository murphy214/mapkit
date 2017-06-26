# mapkit
A namespace in which I can bring in all the misc. repos into my dev enviroment.

This module is essentially me bringing in the stack / repos I use on a daily basis it includes:
## 4 visualization functions from output geojson.
  * a - outputs html canvas geojson on osm basemap (fast)
  
  * b - outputs leaflet on osm basemap (slow but with labels)
  
  * c - outputs leaflet on mapbox og (slow but with labels)**
    
## A series of mapping functionality based function in quickmaps
 * make_colorkey(dataframe,field) - creates colorkey based on unique values in given column or range values if specificied as numeric
 
 Example:
 ```python
 make_colorkey(data,'AREA') # will return a dataframe with a column colorkeys about unique area values
 make_colorkey(data,'gid',numeric=True) # will return a dataframe from a float or int field from ranges assembled
 ```

## Blazing Geojson output 

Brings in nlgeojson into this namespace from another repo (as a requirement) for geojson output at 10 of mbs / s easily. Please see documentation for more info in the nlgeoson repo.
