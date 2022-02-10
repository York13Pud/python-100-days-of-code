# Pandas are designed to help with tabular-based data analysis.

# Pandas can use either Series (1-dimentional) or data frame (2-dimentional) data structures.
# Series is essentially a list from say a column (1 dimention). 
# data frame is the entire table (row / column (2-dimentional))

# import the pandas library:
import pandas

# Using the pandas library, read the contents of a CSV:
data = pandas.read_csv("./weather_data.csv")

# Now, print out the values of the temp column in the CSV file:
print(data["temp"])

# You can convert the data variable contents into different formats. For example (json format):
data_json = data.to_json()
print(data_json)

# Another example is to convert the temp column to a list:
data_list = data["temp"].to_list()
print(data_list)

# Work out the average temp:
print(data["temp"].mean())

# You could do this instead:
print(sum(data_list) / len(data_list))

# Get the max value of the temp column / series:
print(data["temp"].max())
# Note: you can also use data.temp instead to call the series / column as pandas creates attributes for each column header.
# They are both case specific.

# To print a row matching Monday in the day column:
print(data[data.day == "Monday"])

# Print out the row with the highest temp:
print(data[data.temp == (data["temp"].max())])

print(data.temp[data.temp == (data["temp"].max())])

# Work out what Monday's temp was in f rather than c:
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print(f"Monday's temperature was {monday_temp}c / {(monday_temp * 9/5) + 32 }f")

# Create a dataframe from a dictionary:
# A sample dictionary:
data_dict = {"students": ["Bob", "Jane", "Joe"],
             "scores": [76, 56, 65]
             }

# Create a dataframe and print out the contents:
data_dict_df = pandas.DataFrame(data_dict)
print(data_dict_df)

# To save the dataframe to a CSV file:
data_dict_df.to_csv("./data_dict_df.csv")
