# Author: Dustin Burnham
# Last Updated: 1/11/2021
# Data Source: https://www.kaggle.com/unsdsn/world-happiness

# Read in libraries
import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

# Read in data for each year
happy_2015 = pd.read_csv("../data/2015.csv")
happy_2016 = pd.read_csv("../data/2016.csv")
happy_2017 = pd.read_csv("../data/2017.csv")
happy_2018 = pd.read_csv("../data/2018.csv")
happy_2019 = pd.read_csv("../data/2019.csv")

# Add year variable
happy_2015['Year'] = 2015
happy_2016['Year'] = 2016
happy_2017['Year'] = 2017
happy_2018['Year'] = 2018
happy_2019['Year'] = 2019

# Combine into one dataset
happy_list = [happy_2015, happy_2016, happy_2017, happy_2018, happy_2019]
total = pd.concat(happy_list)
assert(len(total) == np.sum(len(happy_2015) + len(happy_2016) + len(happy_2017) + len(happy_2018) + len(happy_2019)))

# Export into data folder
total.to_csv("../data/combined_happiness.csv")