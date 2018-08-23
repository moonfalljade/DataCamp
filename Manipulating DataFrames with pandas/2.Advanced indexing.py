---Changing index of a DataFrame

# Create the list of new indexes: new_idx
new_idx = [i.upper() for i in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)

----Building an index, then a DataFrame
# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index=months

# Print the modified sales DataFrame
print(sales)

----Extracting data with a MultiIndex
# Print sales.loc[['CA', 'TX']]
print(sales.loc[['CA', 'TX']])

# Print sales['CA':'TX']
print(sales['CA':'TX'])

----Setting & sorting a MultiIndex
# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)

----Using .loc[] with nonunique indexes
# Set the index to the column 'state': sales
sales = sales.set_index('state')

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])

----Indexing multiple levels of a MultiIndex
sales
# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY',1)]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA','TX'],2),:]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(['CA','NY','TX'],2),:]
