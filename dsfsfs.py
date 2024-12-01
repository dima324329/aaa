import requests
import re

url = "https://bank.gov.ua/ua/markets/exchangerates"

response = requests.get(url)
response.raise_for_status()

html_text = response.text
match = re.search(r'USD.*?<td.*?>(.*?)</td>', html_text, re.DOTALL)
if match:
    rate = match.group(1).strip()
    print(f"Курс USD: {rate} грн")
else:
    print("Курс USD не найден")
