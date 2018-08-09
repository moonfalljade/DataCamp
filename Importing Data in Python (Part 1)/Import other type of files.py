---- Not so flat any more
import os
wd = os.getcwd()
os.listdir(wd)

---- Listing sheets in Excel files
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
---- Importing sheets from Excel files
# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2=xl.parse('2002')

# Print the head of the DataFrame df2
print(df2.head())
---- Customizing your spreadsheet import
# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=[0], names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xl.parse(0, parse_cols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())


---- Importing SAS files
# Import sas7bdat package
from sas7bdat import SAS7BDAT
import pandas as pd
import matplotlib.pyplot as plt

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas=file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
---- Importing Stata files
# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df= pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

---- Using File to import HDF5 files
h5py_data = h5py.File(h5py_file, 'r')

---- Using h5py to import HDF5 files
# Import packages
import numpy as np
import h5py

# Assign filename: file
file='LIGO_data.hdf5'

# Load file: data
data = h5py.File('LIGO_data.hdf5', 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)

---- Extracting data from your HDF5 file
# Get the HDF5 group: group
group= data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain

strain=data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples=10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

---- Loading .mat files
# Import package
import scipy.io

# Load MATLAB file: mat
mat=scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))


---- The structure of .mat in Python
# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
