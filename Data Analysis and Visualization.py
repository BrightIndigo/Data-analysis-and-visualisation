import numpy as np 
import csv
import matplotlib.pyplot as plt

# Lists to store individual columns from the CSV
square_feet = []
bedrooms = []
bathrooms = []
neighborhood = []
year_built = []
price = []

# Read data from CSV and populate lists
with open('housing_price_dataset.csv', 'r') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)  # Skip header row
    for row in reader:
        square_feet.append(float(row[0]))
        bedrooms.append(float(row[1]))
        bathrooms.append(float(row[2]))
        neighborhood.append(row[3])
        year_built.append(int(row[4]))
        price.append(float(row[5]))

# Convert lists to NumPy arrays for further analysis
square_feet_array = np.array(square_feet)
bedrooms_array = np.array(bedrooms)
bathrooms_array = np.array(bathrooms)
year_built_array = np.array(year_built)
price_array = np.array(price)

# Basic statistics
mean_price = np.mean(price_array)
median_price = np.median(price_array)
std_dev_price = np.std(price_array)

# Data visualization
plt.scatter(square_feet_array, price_array, label='Square Feet vs. Price')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.title('Housing Price vs. Square Feet')
plt.legend()
plt.show()

# Example of additional analysis
average_price_by_bedrooms = np.mean(price_array / bedrooms_array)

print(f"Mean Price: {mean_price}")
print(f"Median Price: {median_price}")
print(f"Standard Deviation of Price: {std_dev_price}")
print(f"Average Price per Bedroom: {average_price_by_bedrooms}")
