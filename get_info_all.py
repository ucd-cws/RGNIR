import rgnir_info
import os
import glob
import csv

# directory of this file
dir = os.path.dirname(os.path.realpath("__file__"))

# empty list to hold the results
results = []

# get list of images
for pic in glob.glob("*.JPG"):  # TODO change ending to img file type
	print(pic)
	path = os.path.join(dir, pic)

	band_stats = rgnir_info.main(path)
	results.append([pic] + band_stats[0])
	results.append([pic] + band_stats[1])
	results.append([pic] + band_stats[2])

print results


# Open File
with open("output.csv", 'wb') as result_csv:
	# Create Writer Object
	wr = csv.writer(result_csv)

	# create header aka "first row"
	wr.writerow(["Image", "Band", "Min", "Max", "Avg", "StdDev"])

	# Write Data to File
	for item in results:
		wr.writerow(item)