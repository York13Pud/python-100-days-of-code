# --- Import the required modules / libraries:
from lxml import html
import requests
import smtplib

# --- Define the required constants:
HEADERS = {"Accept-Language": "en-GB,en;q=0.5",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"}

# --- Define the required variables:
url_to_scrape = "https://www.amazon.co.uk/gp/product/B009921IAG/ref=ox_sc_saved_title_2?smid=A1QUF9YVLMW6HS&psc=1"


# ===============================================================================
# =                           Web Scraping Section                              =
# ===============================================================================

# --- Open the site and assign it to a variable:
site_response = requests.get(url = url_to_scrape, headers=HEADERS)

# --- Parse the file:
tree = html.fromstring(site_response.content)

# --- Find all of the information needed:
product_name = tree.xpath('//span[@id="productTitle"]/text()')
price = tree.xpath('//span[@class="a-price aok-align-center reinventPricePriceToPayPadding priceToPay"]//span[@class="a-offscreen"]/text()')
buy_price = float(price[0].strip("£"))
availability = tree.xpath('//div[@id="availability"]//span[@class="a-size-medium a-color-success"]/text()')
seller = tree.xpath('//div[@class="tabular-buybox-text"][@tabular-attribute-name="Sold by"]//span[@class="a-size-small"]//a[@id="sellerProfileTriggerId"]/text()')
dispatched_from = tree.xpath('//div[@class="tabular-buybox-text"][@tabular-attribute-name="Dispatches from"]//span[@class="a-size-small"]/text()')
delivered_by = tree.xpath('//div[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]//span//span[@class="a-text-bold"]/text()')

# --- Due to how Amazon works, third-party sellers have a URL on the sold by listing. Use a try to check this and swap it
# --- to tree path that has no a tags to pull the seller data if the index is out of range. This normally means it is Amazon
# --- being the seller:
try:
    seller[0]
except IndexError:
    seller = tree.xpath('//div[@class="tabular-buybox-text"][@tabular-attribute-name="Sold by"]//span[@class="a-size-small"]/text()')

# --- Print the results:
print("\n\033[1;33;40m===========\033[1;37;40m Amazon Price Checker \033[1;33;40m===========\033[1;37;40m\n")
print(f"\033[1;33;40mProduct Title: \033[1;37;40m{product_name[0].strip()}\n")
print(f"\033[1;33;40mPrice (GBP): \033[1;37;40m{buy_price}\n")
print(f"\033[1;33;40mAvailability: \033[1;37;40m{availability[0].strip()}\n")
print(f"\033[1;33;40mSeller Name: \033[1;37;40m{seller[0]}\n")
print(f"\033[1;33;40mShipped From: \033[1;37;40m{dispatched_from[0]}\n")
print(f"\033[1;33;40mDelivered By: \033[1;37;40m{delivered_by[0]}\n\033[1;37;40m")
print("\033[1;33;40m============================================\033[1;37;40m\n")


# ===============================================================================
# =                       Send Email Yes / No Section                           =
# ===============================================================================

# --- Set the target price:
target_price = float(19.51)

if buy_price <= target_price:  
    print(f"The current price is \033[1;32;40m£{buy_price}\033[1;37;40m and your target price is \033[1;32;40m£{target_price}\033[1;37;40m.")
    print("\n\033[1;32;40mToday is a good day to buy!\033[1;37;40m")
    print("\nSending an email!")
    # --- Setup required email settings:
    my_email = ""
    to_email = ""
    smtp_server = ""
    sender_username = ""
    sender_password = ""
    
    subject = "Buy, Buy, Buy!! Product Is Below Maximum Price"
    message = f"""
Product Title: {product_name[0].strip()}\n\n
Price (GBP): {buy_price}\n\n
Availability: {availability[0].strip()}\n\n
Seller Name: {seller[0]}\n\n
Shipped From: {dispatched_from[0]}\n\n
Delivered By: {delivered_by[0]}
"""
    
    # --- Send an email to inform the recipient that the price is at, or below the target price:
    with smtplib.SMTP(smtp_server, port=25) as connection:
        # --- Make the connection secure:
        connection.starttls()
        # --- Login to the SMTP Server:
        connection.login(user=sender_username,password=sender_password)
        # --- Send a message.
        # --- Note: \n\n after the subject is required to separate the subject and message body:
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,msg=f"Subject:{subject}\n\n{message}")

else:
    print(f"The current price is \033[1;31;40m£{buy_price}\033[1;37;40m and your target price is \033[1;31;40m£{target_price}\033[1;37;40m.")
    print("\n\033[1;31;40mToday is not a good day to buy!\033[1;37;40m")