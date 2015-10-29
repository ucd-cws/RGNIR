import sys
import os
import gdal
import numpy
from numpy import *

# ignore error when denominator is zero
numpy.seterr(divide='ignore', invalid='ignore')

# check if python gdal bindings are installed
version_num = int(gdal.VersionInfo('VERSION_NUM'))
if version_num < 1100000:
	sys.exit('ERROR: Python bindings of GDAL 1.10 or later required')


def ndvi(img):
	# open dataset
	image = gdal.Open(img)

	#get image name
	name, ext = os.path.splitext(os.path.basename(img))

	# bands
	band1 = image.GetRasterBand(1).ReadAsArray()  #  red
	#band2 = image.GetRasterBand(2).ReadAsArray()  #  green
	band3 = image.GetRasterBand(3).ReadAsArray()  # nir

	band1 = array(band1, dtype=float)  # change the array data type from integer to float to allow decimals
	band3 = array(band3, dtype=float)

	# calculate ndvi
	# NDVI = (nearInfrared - Red) / (nearInfrared + Red)
	var1 = subtract(band3, band1)
	var2 = add(band3, band1)
	ndvi_result = divide(var1, var2)

	# https://gist.github.com/arnaldorusso/100b58b8c23d8398fe9d
	shape = band1.shape  # get the image dimensions - format (row, col)
	driver = gdal.GetDriverByName('GTiff')
	dst_ds = driver.Create(os.path.join("NDVI", (name + "_NDVI.tif")), shape[1], shape[0], 1, gdal.GDT_Float32)    # destination filename, number of columns
																					# and rows, num bands, output datatype

	dst_ds.GetRasterBand(1).WriteArray(ndvi_result)  # write numpy array band1 as the first band of the multiTiff
	stat = dst_ds.GetRasterBand(1).GetStatistics(1, 1)  # get the band statistics (min, max, mean, standard deviation)

	# close dataset
	image = None

	return(["NDVI"] + stat)


def ndwi(img):
	# open dataset
	image = gdal.Open(img)

	#get image name
	name, ext = os.path.splitext(os.path.basename(img))

	# bands
	#band1 = image.GetRasterBand(1).ReadAsArray()  #  red
	band2 = image.GetRasterBand(2).ReadAsArray()  #  green
	band3 = image.GetRasterBand(3).ReadAsArray()  # nir

	band2 = array(band2, dtype=float)  # change the array data type from integer to float to allow decimals
	band3 = array(band3, dtype=float)

	# calculate ndvi
	# NDWI = (green - NIR) / (green + NIR)
	var1 = subtract(band3, band2)
	var2 = add(band3, band2)
	ndwi_result = divide(var1, var2)

	# https://gist.github.com/arnaldorusso/100b58b8c23d8398fe9d
	shape = band3.shape  # get the image dimensions - format (row, col)
	driver = gdal.GetDriverByName('GTiff')
	dst_ds = driver.Create(os.path.join("NDWI", (name + "_NDWI.tif")), shape[1], shape[0], 1, gdal.GDT_Float32)    # destination filename, number of columns
																					# and rows, num bands, output datatype

	dst_ds.GetRasterBand(1).WriteArray(ndwi_result)  # write numpy array band1 as the first band of the multiTiff
	stat = dst_ds.GetRasterBand(1).GetStatistics(1, 1)  # get the band statistics (min, max, mean, standard deviation)

	# close dataset
	image = None

	return(["NDWI"] + stat)

