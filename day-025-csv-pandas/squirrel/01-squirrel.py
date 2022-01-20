# primary fur colour (cinnamon, grey, black), 
# create dataframe to show the count of how many cinnamon, grey, black squirrels there are:
# Output should be fur colour and count.

import pandas

source_data = pandas.read_csv("./squirrel-data.csv")
source_data = source_data.rename(columns = {"Primary Fur Color": "Fur Color"})

total_counts = (source_data.groupby(["Fur Color"])["Fur Color"].count().reset_index(name="count"))
total_counts.to_csv("./count-of-squirrels.csv")