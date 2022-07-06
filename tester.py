import requests

API_KEY = "AIzaSyB0gfsEQdsGeW8xb-rerFG-CehoThKHUr0"

url =  "https://www.googleapis.com/youtube/v3/activities"

response = requests.get(url, {"key":API_KEY, "channelId":"UCq27-1ZCNMYs4csa86q3SGw"})
print(response.json())