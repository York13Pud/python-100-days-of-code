import datetime

# --- Ask the user which date they would like to look up:
def get_date_to_use():
    """This function will ask the user to provide a date to use that will be later used to gather the top-100 
    songs for that date."""
    
    date_correct = False
    while date_correct is False:
        date_format = "%Y-%m-%d"
        date_from_user = input("\033[1;37;40mPlease enter a date to get the top 100 songs from? YYYY-MM-DD: ")
        try:
            datetime.datetime.strptime(date_from_user, date_format)
        except ValueError:
            print("\n\033[1;31;40mERROR\033[1;37;40m: This is the incorrect date format. It should be YYYY-MM-DD.\n")
        else:
            date_correct = True
            return date_from_user