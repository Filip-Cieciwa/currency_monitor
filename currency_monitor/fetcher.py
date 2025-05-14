import requests
import csv
from datetime import datetime

def fetch_exchange_rates():
    """
    Pobiera aktualne kursy USD, EUR, GBP z API NBP i zapisuje do CSV.
    Zwraca słownik {kod_waluty: kurs}.
    """
    url = 'https://api.nbp.pl/api/exchangerates/tables/A?format=json'
    response = requests.get(url)
    data = response.json()  # lista, pierwszy element zawiera tabelę kursów
    table = data[0]
    date = table['effectiveDate']  # data publikacji kursów

    # Filtrujemy interesujące nas waluty USD, EUR, GBP
    rates = {}
    for item in table['rates']:
        code = item['code']
        if code in ['USD', 'EUR', 'GBP']:
            rates[code] = item['mid']

    # Zapis kursów do pliku CSV (każde odświeżenie to kolejny wiersz)
    filename = 'currency_data.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([date, rates.get('USD'), rates.get('EUR'), rates.get('GBP')])

    return rates