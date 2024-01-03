import numpy as np 
import csv
import math

with open('housing_price_dataset.csv', 'r') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        price = row[0]
        price = int(price)
        data = list(price)
        data_array = np.array(price)
        data_array = np.array(price, dtype=float)
        mean = np.mean(data_array)
        max_value = np.max(data_array)

print("Data array", data_array)
