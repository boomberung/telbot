import requests

r = requests.get("https://api.telegram.org/bot286888171:AAGb0YLpt_aXbeI3DvjTz7TlASwO0nq49-8/getUpdates")
print(r.text)