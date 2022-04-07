import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
# from matplotlib.ticker import mtick


df = pd.read_csv('all_data.csv')

print(df.Country.unique())