import smtplib

import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_daily_closing_price() -> list:
    API_KEY = "AZTR41DL1KSBO8P0"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": API_KEY,
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    temp_data = response.json()["Time Series (Daily)"]
    return [value for (key, value) in temp_data.items()]

data_daily_list = get_daily_closing_price()

yesterday_closing_price = float(data_daily_list[0]["4. close"])
before_yesterday_closing_price = float(data_daily_list[1]["4. close"])

percentage_change = (yesterday_closing_price - before_yesterday_closing_price) / before_yesterday_closing_price * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

def get_before_yesterday_date():
    now = dt.datetime.now()
    two_days_ago = now - dt.timedelta(days=2)
    return str(two_days_ago)

def get_news_pieces() -> list:
    API_KEY = "c5e2b1a8cf1644f8a26e5a3ebd4c1001"
    parameters = {
        "q": "tesla",
        "from": get_before_yesterday_date(),
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    data_article_list = response.json()["articles"]
    print(data_article_list)
    return data_article_list

def send_mail(to_addr, subject, msg_body):
    from_addr = "aliard.bks@gmail.com"
    password = 'kdbh fovj odwn bmhe'
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=from_addr, password=password)
        connection.sendmail(from_addr, to_addr, f"Subject:{subject}\n\n{msg_body}")

if abs(percentage_change) < 5:
    message_title = ""
    article_list = get_news_pieces()
    if percentage_change < 0:
        message_title = f"TESLA 🔻 {abs(percentage_change)}%"
    else:
        message_title = f"TESLA 🔺 {abs(percentage_change)}%"
    print("sending....")
    send_mail("fojev41305@noomlocs.com", f"{message_title}", msg_body=article_list[0]["content"])
    print("mail sent")


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""








































