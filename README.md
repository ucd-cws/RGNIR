# RGNIR

## About 

Calculate band statistics for modified Green-Red-NIR 800 to 900nm images. Script will export 
min, max, avg, and stddev for each band to a csv file. NDVI and NDWI rasters are created in 
sub-folders and included in the statistic list. 

## Reqs

GDAL python bindings


## Usage

1. Clone this repo to folder with RGNiR images. Change file extension in ```get_info_all.py``` 
if images are something other than JPGs. 
2. run ```python get_info_all.py```
3. Script will create folders called NDWI and NDVI if they don't exist to store index rasters. 
4. GDAL GetStatistics will return the band statistics (min, max, mean, standard deviation) for 
each band as well as NDVI and NDWI.
5. Open CSV file with the results.
