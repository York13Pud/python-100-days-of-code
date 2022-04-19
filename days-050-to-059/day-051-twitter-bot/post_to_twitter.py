# --- Import the required variables:
import tweepy
import os


def post_tweet(download_getting: float, download_should_be: float, upload_getting:float, upload_should_be:float):
    """This function will create a tweet to complain about your bad internet speed."""
    
    # --- Get the required Twitter API keys from O/S environment variables:
    consumer_key = os.environ.get('CONSUMER_KEY', "Test")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    access_token = os.environ.get("ACCESS_KEY")
    access_token_secret = os.environ.get("ACCESS_SECRET")

    # --- Authenticate with the Twitter API
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )
    
    # --- Post the tweet:
    response = client.create_tweet(
        text=f"My download speed is: {download_getting}Mbps (should be: {download_should_be}Mbps)\nMy upload speed is: {upload_getting}Mbps (should be: {upload_should_be}Mbps)\n\nPlease Investigate."
    )
    
    # --- Get the URL for the tweet:
    tweet_link = f"https://twitter.com/user/status/{response.data['id']}"
    
    # --- Return the URL back to the main.py file:
    return tweet_link