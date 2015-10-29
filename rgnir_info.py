import sys
import gdal
from numpy import *

# check if python gdal bindings are installed
version_num = int(gdal.VersionInfo('VERSION_NUM'))
if version_num < 1100000:
	sys.exit('ERROR: Python bindings of GDAL 1.10 or later required')


def get_band_stats(img):
	""" Get stats (Min, Max, Mean, StdDev) for each band"""
	# open dataset
	image = gdal.Open(img)

	# get the number of bands
	num_bands = image.RasterCount

	# create an empty list
	band_stats = []

	# loop through the bands and get band stats
	for i in range(1, num_bands + 1):
		print "Band: %s" % i
		stats = image.GetRasterBand(i).GetStatistics(0,1)  # min, max, mean, stddev
		band_stats.append([i] + stats) # add band id to stats list

	# close dataset
	image = None

	return band_stats


if __name__ == '__main__':

	if len(sys.argv) < 2:
		print
		"""
		[ ERROR ] you must supply the image you want to calc band stats
		"""
	get_band_stats(sys.argv[1])





