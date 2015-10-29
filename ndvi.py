import sys
import gdal
from numpy import *

# check if python gdal bindings are installed
version_num = int(gdal.VersionInfo('VERSION_NUM'))
if version_num < 1100000:
	sys.exit('ERROR: Python bindings of GDAL 1.10 or later required')


img = r"C:\Users\Andy\Documents\RGNIR\IMG_0081.JPG"

# open dataset
image = gdal.Open(img)

# get the number of bands
num_bands = image.RasterCount

band1 = image.GetRasterBand(1).ReadAsArray()
band2 = image.GetRasterBand(2).ReadAsArray()
band3 = image.GetRasterBand(3).ReadAsArray()

band1 = array(band1, dtype=float)  # change the array data type from integer to float to allow decimals
band2 = array(band2, dtype=float)


# close dataset
image = None


# calculate ndvi
# NDVI = (nearInfrared - Red) / (nearInfrared + Red)

var1 = subtract(band4, band3)
var2 = add(band4, band3)

ndvi = divide(var1, var2)


