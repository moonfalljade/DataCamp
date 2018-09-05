---Reading a csv file
# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the DataFrame
df = pd.read_csv(grant_file)

---Comparing a histogram and distplot
The pandas library supports simple plotting of data, which is very convenient when data is already likely to be in a pandas DataFrame.

Seaborn generally does more statistical analysis on data and can provide more sophisticated insight into the data. In this exercise, we will compare a pandas histogram vs the seaborn distplot.
# Display pandas histogram
df['Award_Amount'].plot.hist()
plt.show()

# Clear out the pandas histogram
plt.clf()

# Display a Seaborn distplot
sns.distplot(df['Award_Amount'])
plt.show()

# Clear the distplot
plt.clf()

---Plot a histogram
The distplot() function will return a Kernel Density Estimate (KDE) by default. The KDE helps to smooth the distribution and is a useful way to look at the data. However, Seaborn can also support the more standard histogram approach if that is more meaningful for your analysis.
# Create a distplot
sns.distplot(df['Award_Amount'],
             kde=False,
             bins=20)

# Display the plot
plt.show()



---Rug plot and kde shading
# Create a distplot of the Award Amount
sns.distplot(df['Award_Amount'],
             hist=False,
             rug=True,
             kde_kws={'shade':True})

# Plot the results
plt.show()


---Create a regression plot
df.head()
sns.lmplot(data=df,
         x="insurance_losses",
         y="premiums")

# Display the plot
plt.show()

---Plotting multiple variables
# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()
The results are bit difficult to read. Maybe using multiple lines is not the best approach. Let's try another one in the next exercise.


---Facetting multiple regressions
# Create a regression plot with multiple rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Show the plot
plt.show()
The lmplot function supports plotting regression data by column, row and hue. This concept is used repeatedly throughout Seaborn.
