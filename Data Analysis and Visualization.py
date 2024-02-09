import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd

def load_data(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def plot_box(data, x, y, xlabel, ylabel, title):
    data.boxplot(column=y, by=x)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.suptitle("")
    plt.show()

def main():
    data = load_data('housing_price_dataset.csv')
    if data is None:
        return

    square_feet_array = data['SquareFeet'].values
    price_array = data['Price'].values

    mean_price = np.mean(price_array)
    median_price = np.median(price_array)
    std_dev_price = np.std(price_array)

    plt.scatter(square_feet_array, price_array, label='Square Feet vs. Price')
    plt.xlabel('Square Feet')
    plt.ylabel('Price')
    plt.title('Housing Price vs. Square Feet')
    plt.legend()
    plt.show()

    plot_box(data, 'Square Feet', 'Price', 'Square Feet', 'Price', 'Box Plot of Housing Price vs. Square Feet')
    print(data.columns)
main()
