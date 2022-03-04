# --- Import required modules:
from speedtest import gather_speedtest_json
from process_json import ProcessJson
from post_to_twitter import post_tweet

# --- Call the gather_speedtest_json function to either get the existing data 
# --- or run a speedtest to generate a new result:
print("\n\033[1;35;40m====================\033[1;37;40m ISP Speed Check \033[1;35;40m====================\033[1;37;40m\n")

speedtest_data = gather_speedtest_json()

# --- Define variables used for what your speed should actually be:
supposed_download_speed_bits = float(65000000)
supposed_download_speed_mbps = float(round(supposed_download_speed_bits / 125 / 1000, 2))
supposed_upload_speed_bits = float(1800000)
supposed_upload_speed_mbps = float(round(supposed_upload_speed_bits / 125 / 1000, 2))


# --- If the JSON file is empty / None, stop the program:
if speedtest_data == None:
    pass

else:
    # --- Process the contents of the JSON file into an object.
    processed_data = ProcessJson(json_to_process = speedtest_data)


    # --- Convert bits to Mbps:
    download_speed_mbps = round(processed_data.home_download_speed_bits / 125 / 1000, 2)
    upload_speed_mbps = round(processed_data.home_upload_speed_bits / 125 / 1000, 2)


    # --- Display the results:
    print("\033[1;35;40m===================\033[1;37;40m SpeedTest Results \033[1;35;40m===================\033[1;37;40m\n")
    print(f"\033[1;35;40m[ISP]: \033[1;37;40m{processed_data.home_isp}")
    print(f"\033[1;35;40m[Date]: \033[1;37;40m{processed_data.date}")
    print(f"\033[1;35;40m[Time]: \033[1;37;40m{processed_data.time}")
    print(f"\033[1;35;40m[Download Speed]: \033[1;37;40m{download_speed_mbps} Mb/s, ISP Supplied: ({supposed_download_speed_mbps}Mbps)")
    print(f"\033[1;35;40m[Download Test Time]: \033[1;37;40m{round(processed_data.home_download_time / 1000, 2)} Seconds")
    print(f"\033[1;35;40m[Upload Speed]: \033[1;37;40m{upload_speed_mbps} Mb/s, ISP Supplied: ({supposed_upload_speed_mbps}Mbps)")
    print(f"\033[1;35;40m[Upload Test Time]: \033[1;37;40m{round(processed_data.home_upload_time / 1000, 2)} Seconds\n")
    print("\033[1;35;40m=========================================================\033[1;37;40m\n")

    # --- Define variables to determine if bandwith is ok (used for comparison later):
    download_ok = True
    upload_ok = True
    
    
    # --- Determine if the upload / download speed is better or worse that what you pay for:
    if supposed_download_speed_bits > processed_data.home_download_speed_bits:
        print("\033[1;33;40m[WARNING]:\033[1;37;40m Your Download speed sucks!\n")
        download_ok = False
    else:
        print("\033[1;32;40m[NOTICE]:\033[1;37;40m Your Download Speed Is All good!\n")
        
    if supposed_upload_speed_bits > processed_data.home_upload_speed_bits:
        print("\033[1;33;40m[WARNING]:\033[1;37;40m Your Upload Speed Sucks!\n")
        upload_ok = False
    else:
        print("\033[1;32;40m[NOTICE]:\033[1;37;40m Your Upload Speed Is All good!\n")
   
       
    # --- Post a tweet if either download_ok / upload_ok is False:
    if download_ok is False or upload_ok is False:
        print("\033[1;35;40m===================\033[1;37;40m Raise A Complaint \033[1;35;40m===================\033[1;37;40m\n")
        print("\033[1;31;40m[OH SHIT!]\033[1;37;40m Well that just isn't cricket now is it!!\n\n\033[1;31;40m[OH SHIT!]\033[1;37;40m I shall complain with a sternly worded Tweet!!\n")
        print("\033[1;35;40m===================\033[1;37;40m Posting A Tweet \033[1;35;40m=====================\033[1;37;40m\n")
        print(f"\033[1;35;40m[Tweet URL]: \033[1;36;40m{post_tweet(download_getting=download_speed_mbps, download_should_be=supposed_download_speed_mbps, upload_getting=upload_speed_mbps, upload_should_be=supposed_upload_speed_mbps)}\n\033[1;37;40m")
        print("\033[1;35;40m=========================================================\033[1;37;40m\n")        