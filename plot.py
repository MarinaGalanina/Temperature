import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import data_preparation
import numpy as np


def get_x_y_colors(data):
    dic = {}
    dic['x'] = [0] * len(data)#słownik,dodaje ile miejsca,ile trzeba(300 miejsc)
    dic['y'] = [0] * len(data)
    dic['colors'] = [0] * len(data)
    for i in range(0, len(data)):
        dic['x'][i] = data[i][0]
        dic['y'][i] = data[i][1]
        dic['colors'][i] = data[i][2]
    return dic


temp_from = 0
temp_to = 30
wind_from = 0
wind_to = 10

fileName = "newData.txt"
data = data_preparation.load_txt(fileName)


# change prediction to color in graph
for i in range(0, len(data)):
    if data[i][2] == 'cold':
        data[i][2] = 'blue'
    elif data[i][2] == 'hot':
        data[i][2] = 'red'
    else:
        data[i][2] = 'gray'


data_processed = get_x_y_colors(data)

plt.title('Subiektywne odczuwanie temperatury')
plt.xlabel(u"Temperatura w °C")
plt.ylabel(u"Prędkość wiatru w km/h")
plt.axis([temp_from, temp_to, wind_from, wind_to])

print(data[:][2])

# Dodanie legendy do wykresu.
blue_patch = mpatches.Patch(color='blue', label='zimno')
red_patch = mpatches.Patch(color='red', label=u'ciepło')
plt.legend(handles=[blue_patch, red_patch])

plt.scatter(data_processed['x'], data_processed['y'], s=[250] * len(data), c = data_processed['colors'])
plt.show()