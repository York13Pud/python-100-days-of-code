import csv

# Import the csv file data into a variable, split each row into a list entry and then
# print the contents of the list:
# with open("./weather_data.csv") as weather_data:
#     weather = weather_data.readlines()
#     print(weather)
    
# The above method works but it will need a lot of cleaning up. Instead, another method is to use the csv library:
with open("./weather_data.csv") as weather_data:
    weather = csv.reader(weather_data)
    temperatures = []
    for row in weather:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# The above is a pain in the a$$ as you need to write a lot of code to do a very basic thing.
# This is where pandas come in. These are designed to help with tabular-based data analysis.