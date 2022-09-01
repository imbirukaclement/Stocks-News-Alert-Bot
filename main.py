import requests
from twilio.rest import Client
#from twilio.http.http_client import TwillioHttpClient



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = "ACeec9f9ab642e6df2ac8d2c7a8131065c"
auth_token = "4a17a2824bb945692f5bd4716eda5b7d"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "eee31709f9084c9f894c742b5b6c7525"
STOCK_API_KEY = "BV45W3I4XPJDVK4R"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT,params=stock_params)
print(response.json())
data = response.json()["Time Series (Daily)"]

data_list = [value for (key,value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = yesterdays_data["4. close"]

day_before_yesterdays_data = data_list[1]
day_before_yesterdays_closing_price = day_before_yesterdays_data["4. close"]
difference = float(yesterdays_closing_price) - float(day_before_yesterdays_closing_price)
diff_percent = round((difference / float(yesterdays_closing_price)) * 100)
updown = None
if abs(diff_percent) > 1:
    updown = "🔺"
else:
    updown = "🔻"
news_params = {
    "apiKey":API_KEY,
    "qInTitle": COMPANY_NAME,
}
news_response = requests.get(NEWS_ENDPOINT,params=news_params)
articles = news_response.json()["articles"]
three_articles = articles[:3]
print(three_articles)
formatted_articles = [f"{STOCK_NAME}:{updown} {diff_percent}% Headline: {article ['title']}. \nBrief : {article ['description']}" for article in three_articles]
client = Client(account_sid,auth_token)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+18593506477",
        to=["+254715522758","254725988419"]
    )



