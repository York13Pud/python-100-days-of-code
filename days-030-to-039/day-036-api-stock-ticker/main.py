# --- Import the required modules:
from clear import clear_screen
from itertools import islice
from logo import logo, goodbye
import requests
import time

# --- Ask the user for a stock ticker:    
def ask_for_stock_ticker():
    """This function will request the user to provide a stock ticker to check and then call the check_stock_ticker function to
    check the prices and news."""
    
    # --- Ask the user to supply a stock ticker to look up:    
    stock_name = input("Please enter a valid stock ticker (e.g AAPL): ")
    clear_screen()
    check_stock_ticker(ticker_code=stock_name.upper())
    
def check_stock_ticker(ticker_code="AAPL"):
    """Required: ticker_code. This function will check the supplied stock ticker and retrieve the pricing and news."""    
    
    # --- These are the parameters required for the alphavantage API call:
    STOCK_PARAMETERS = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker_code,
        "datatype": "json",
        "apikey": "Change_Me"
    }

    # --- These are the parameters required for the news API call:
    NEWS_PARAMETERS = {
        "q": ticker_code,
        "apiKey": "Change_Me",    
    }

    # --- These are the endpoints for the stock and news API's:
    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    # --- Execute the API call to get the stock data:
    stock_price_call = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)

    # --- If an error occurs, this will print out the response and its meaning:
    stock_price_call.raise_for_status()

    # --- Format the response from the API call to json:
    stock_price_data = stock_price_call.json()

    # --- Add the prices for yesterdays and the day before yesterday to a new list called prices:
    prices = []
    for value in islice(stock_price_data["Time Series (Daily)"],2):
        prices.append(float(stock_price_data["Time Series (Daily)"][value]["4. close"]))

    # --- Create two variables for the two prices:
    yesterday_close_price = prices[0]
    day_before_yesterday_close_price = prices[1]

    # --- Determine the price of the stock at close for yesterday:
    print(f"\033[1;36;40mClose yesterday: \033[1;37;40m{yesterday_close_price:.2f}")
    print(f"\033[1;36;40mClose day before yesterday: \033[1;37;40m{day_before_yesterday_close_price:.2f}")

    # --- Work out the $ change between the two days:
    price_difference = abs(yesterday_close_price - day_before_yesterday_close_price)
    print(f"\033[1;36;40mPrice difference: \033[1;37;40m${price_difference:.2f}")

    # --- Work out the % change between the two days:
    price_difference_percent = float((price_difference/day_before_yesterday_close_price) * 100)
    print(f"\033[1;36;40mPrice difference: \033[1;37;40m{price_difference_percent:.2f}%\n")

    input("Press any key to continue.")
    clear_screen()
    if price_difference_percent >= 1:
        #--- Execute the API call to get the news data:
        news_call = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)

        # --- If an error occurs, this will print out the response and its meaning:
        news_call.raise_for_status()

        # --- Format the response from the API call to json:
        news_data = news_call.json()
        
        # --- Add the first three articles to a list:
        news_articles = []
        for article in news_data["articles"][:3]:
            news_articles.append(article)
        
        # --- Using the news_articles list, print out the details in a nice format:
        print(f"Top Three News Articles relating To {ticker_code}\n")
        for news_article in news_articles:
            print(f'\033[1;32;40mSource: \033[1;34;40mhttps://www.{news_article["source"]["name"]}\033[1;37;40m')
            print(f'\033[1;32;40mWritten By: \033[1;35;40m{news_article["author"]}\033[1;37;40m')
            print(f'\033[1;32;40mTitle: \033[1;35;40m{news_article["title"]}\033[1;37;40m')
            print(f'\033[1;32;40mDescription: \033[1;35;40m{news_article["description"]}\033[1;37;40m')
            print(f'\033[1;32;40mLink:\033[1;34;40m {news_article["url"]}\033[1;37;40m\n')
    else:
        print("\033[1;31;40mThe price difference was less that 1%. No news to show.\033[1;37;40m\n")
    
    input("Press any key to continue.")
    clear_screen()
    # --- Ask the user if they would like to check another stock ticker. 
    # --- If so, call ask_for_stock_ticker. If not, exit the program:
    check_another = input("Would you like to check another stock? (Yes / No): ")
    if check_another == "Yes" or check_another == "yes" or check_another == "y" or check_another == "Y":
        clear_screen()
        ask_for_stock_ticker()
    else:
        clear_screen()
        print(goodbye)

# --- Display the programs logo:
print(logo)
time.sleep(2)
clear_screen()

# --- Start the main program:
ask_for_stock_ticker()


# Requirements:

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Note: Changed to 1% due to state of the market on the day.

#Done TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#Done TODO 2. - Get the day before yesterday's closing stock price
#Done TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#Done TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#Done TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#Done TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#Done TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#Done TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#Skipped TODO 9. - Send each article as a separate message via Twilio. 
# Instead I opted for some printed text instead.
