# --- Import the required libraries / modules:
import pandas as pd
import time

# --- Using the pandas library, read the contents of a CSV:
data = pd.read_csv("./data-source.csv")

def sum_a_b(sample_name):
    ''' A function to add the values of parta and partb to each other (per row) and put them in a new column'''
    my_sum = data.parta + data.partb
    
    # --- Create a new column / series called equals that will have the value of a+b:
    data["equals"] = my_sum

    # --- print out the contents of the row:
    print(data[data.name == sample_name])
    
    # --- Call the search_data function:
    search_data(sample_name)
    
def search_data(sample_name):
    ''' A function to search for a value in the name column / series and then use that to access 
    values in other columns in the dataframe row '''
    
    # --- retrieve the values of parta and partb columns / series' by filtering by the sampler_name passed.
    # --- Note: Type conversion required as the default type returned is a numpy array:
    a = int(data.parta.values[data.name == sample_name])
    b = int(data.partb.values[data.name == sample_name])
    
    # --- Let's play with the results by printing out the results in a few ways:
    print(f"\n{sample_name} has a set to {a} and b set to {b}")
    print(f"The value of a + b is: {a+b} \n")
    
    # --- Call the remove_from_dataframe function:
    remove_from_dataframe(sample_name)

def remove_from_dataframe(sample_name):
    ''' A function to remove an entry from the dataframe'''    
    # --- Import data into the function:
    global data
    
    # --- Find the index number matching the value of sample_name:
    index_to_drop = int(data.index.values[data.name == sample_name])
    
    # --- Update the data dataframe by dropping the located index:
    data = data.drop(index_to_drop)
    
    # --- Let's be a little user friendly and let them know what we are dropping:
    print(f"Deleting {sample_name} from the dataframe. Please wait....\n")
    time.sleep(3)
    
    # --- Print out the updated dataframe:
    print(data)
    
    # --- Call the export_to_csv function
    export_to_csv(data = data)
    
def export_to_csv(data):
    ''' Just for a laugh, let's export the updated dataframe to a CSV file.'''
    
    # --- Export the dataframe to a new CSV file
    data.to_csv("./data_updated.csv")
    
# --- Let's begin by calling the sum_a_b function:
sum_a_b(sample_name = "sample-one")