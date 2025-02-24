"""
Created on Sun Feb 23 21:55:09 2025

@author: allyschmidt
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import dataset
dataset = pd.read_csv('all_items.csv')
dataset.dtypes
dataset.describe()
dataset.info()


# Convert Date column type
dataset['Date'] = pd.to_datetime(dataset['Date'])


# Remove repeated listings
dataset = (dataset.sort_values('Date')).drop_duplicates(subset = ['Category', 'Item', 'Price', 'User', 'Description'], keep = 'first')
dataset.head()

marketplace_dataset = dataset[dataset['Category'] == 'Marketplace']
rental_dataset = dataset[dataset['Category'] == 'Rental/Roommates']


market_q1 = marketplace_dataset['Price'].quantile(.25)
market_q3 = marketplace_dataset['Price'].quantile(.75)
market_IQR = market_q3 - market_q1

rental_q1 = rental_dataset['Price'].quantile(.25)
rental_q3 = rental_dataset['Price'].quantile(.75)
rental_IQR = rental_q3 - rental_q1

plt.boxplot(marketplace_dataset['Price'].dropna())
plt.show()

plt.boxplot(rental_dataset['Price'].dropna())
plt.show()

# Remove Marketplace price outliers
marketplace_dataset_modified = marketplace_dataset[~((marketplace_dataset['Price'] < (market_q1 - 1.5*market_IQR)) | (marketplace_dataset['Price'] > (market_q3 + 1.5*market_IQR)))]
marketplace_dataset_modified = marketplace_dataset_modified.dropna()
plt.boxplot(marketplace_dataset_modified['Price'])
plt.show()

# Remove Rental price outliers
rental_dataset_modified = rental_dataset[~((rental_dataset['Price'] < (rental_q1 - 1.5*rental_IQR)) | (rental_dataset['Price'] > (rental_q3 + 1.5*rental_IQR)))]
rental_dataset_modified = rental_dataset_modified.dropna()
plt.boxplot(rental_dataset_modified['Price'])
plt.show()







