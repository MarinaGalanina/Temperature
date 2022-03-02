#
# KNN algorithm
#
# Input file is text file
# each line has three positions
# 'temperature' 'wind speed' 'Class (cold / hot)'
#
# input in command line: input_file, output_file, k-nn, Xmin, Xmax, Ymin, Ymax
#
# --------------------------------------------------------------------------------------------------------------

import sys
from KNN import predict_classification
from data_preparation import load_txt


def write_to_file(fileName, dataList):
    textfile = open(fileName, "w")
    for element in dataList:
        textfile.write(element[0] + " " + element[1] + " " + element[2] + "\n")
    textfile.close()


dataset = load_txt("temperature_preferences.txt")

min_temperature = 0
max_temperature = 30

min_wind = 0
max_wind = 10

new_data = list()

for temperature in range(min_temperature, max_temperature + 1):
    for wind in range(min_wind, max_wind + 1):
        prediction = predict_classification([temperature, wind], dataset,1)
        new_data.append([str(temperature), str(wind), prediction])

write_to_file("newData.txt", new_data)
