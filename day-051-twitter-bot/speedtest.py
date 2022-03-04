import json
import os

def gather_speedtest_json():
    """This function will run a speedtest and output it to a JSON file. If it fails, an error will be displayed."""
    
    # --- Define variables required for this function:
    speedtest_cli = "speedtest -f json > speedtest.json 2> /dev/null"
    missing_speedtest_msg = "\033[1;31;40m[ERROR]:\033[1;37;40m Speedtest is not installed or accessible. Please check you have it installed and/or you have permission to run it."
    
    # --- Check if there is a JSON file present. If so, return the contents:
    try:
        with open("./speedtest.json", mode="r") as data_file:
            print("\033[1;32;40m[NOTICE]:\033[1;37;40m JSON File found. Processing file...\n")
            data = json.load(data_file)
        return data
    
    # --- If the JSON file is not present, run speedtest to generate a new one:    
    except FileNotFoundError:
        print("\033[1;33;40m[WARNING]:\033[1;37;40m File not found. Running SpeedTest...\n")
        
        # --- Run the speedtest command. If it fails, display an error:
        if os.system(speedtest_cli) !=0:
            os.system('rm speedtest.json')
            print(missing_speedtest_msg)
            data = None
            return data
            
        # --- Recurse through the function to process the JSON file:
        else:
            return gather_speedtest_json()