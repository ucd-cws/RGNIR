import rgnir_info
import os
import glob
import csv
import index_stats

# directory of this file
dir = os.path.dirname(os.path.realpath("__file__"))


# create folder for NDVI/NDWI
if not os.path.exists(os.path.join(dir, "NDVI")):
	os.makedirs(os.path.join(dir, "NDVI"))

if not os.path.exists(os.path.join(dir, "NDWI")):
	os.makedirs(os.path.join(dir, "NDWI"))

# empty list to hold the results
results = []

# get list of images
for pic in glob.glob("*.JPG"):  # TODO change ending to img file type
	print(pic)
	path = os.path.join(dir, pic)

	# add statistics for individual bands
	band_stats = rgnir_info.get_band_stats(path)
	results.append([pic] + band_stats[0])
	results.append([pic] + band_stats[1])
	results.append([pic] + band_stats[2])

	# add statistics for NDVI
	ndvi = index_stats.ndvi(path)
	results.append([pic] + ndvi)


	# add statistics for NDWI
	ndwi = index_stats.ndwi(path)
	results.append([pic] + ndwi)

print results


# Open File
with open("Image_Band_Statistics.csv", 'wb') as result_csv:
	# Create Writer Object
	wr = csv.writer(result_csv)

	# create header aka "first row"
	wr.writerow(["Image", "Band", "Min", "Max", "Avg", "StdDev"])

	# Write Data to File
	for item in results:
		wr.writerow(item)