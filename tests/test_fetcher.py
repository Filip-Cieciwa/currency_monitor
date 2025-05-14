import unittest
from unittest.mock import patch, Mock
from currency_monitor.fetcher import fetch_exchange_rates

class TestFetcher(unittest.TestCase):
    @patch('currency_monitor.fetcher.requests.get')
    def test_fetch_exchange_rates(self, mock_get):
        # Przygotuj sztuczne dane zwracane przez API NBP
        fake_data = [{
            'effectiveDate': '2025-05-13',
            'rates': [
                {'code': 'USD', 'mid': 4.0},
                {'code': 'EUR', 'mid': 4.5},
                {'code': 'GBP', 'mid': 5.5},
                {'code': 'CHF', 'mid': 4.2}  # inna waluta, powinna zostać pominięta
            ]
        }]
        # Skonfiguruj mock, aby zwrócić fake_data
        mock_response = Mock()
        mock_response.json.return_value = fake_data
        mock_get.return_value = mock_response

        # Wywołaj funkcję i sprawdź wyniki
        rates = fetch_exchange_rates()
        self.assertEqual(rates['USD'], 4.0)
        self.assertEqual(rates['EUR'], 4.5)
        self.assertEqual(rates['GBP'], 5.5)
        # Powinny być dokładnie te 3 waluty
        self.assertNotIn('CHF', rates)

        # Sprawdź, czy requests.get został wywołany z odpowiednim URL
        mock_get.assert_called_with('https://api.nbp.pl/api/exchangerates/tables/A?format=json')

if __name__ == '__main__':
    unittest.main()