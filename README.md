# Currency Monitor

**Currency Monitor** to niewielka, ale praktyczna aplikacja desktopowa napisana w Pythonie z wykorzystaniem Tkinter. Pokazuje ona aktualne kursy USD, EUR i GBP wobec PLN, pobierając je z publicznego API Narodowego Banku Polskiego. Dane prezentowane są w czytelnej tabeli i na wykresie słupkowym, a każdy update trafia też do pliku CSV - dzięki temu możesz łatwo śledzić historię kursów.

## Szybki start

1. **Pobierz projekt**

   ```bash
   git clone https://github.com/Filip-Cieciwa/currency_monitor.git
   cd currency_monitor
   ```
2. **Stwórz wirtualne środowisko**

   * **Windows**:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * **macOS/Linux**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **Zainstaluj zależności**

   ```bash
   pip install -r requirements.txt
   ```


## Jak uruchomić aplikację

Z poziomu terminala (w aktywowanym venv) wpisz:

```bash
python -m currency_monitor.gui
```

Powinno pojawić się okienko z tabelą kursów i wykresem. Aby odświeżyć dane, kliknij przycisk **Odśwież** - nowe wartości zostaną pokazane natychmiast, a także dopisane do `currency_data.csv`.


## Testy

Chcesz sprawdzić, czy moduł pobierania kursów działa bez zarzutu? Uruchom:

```bash
python -m unittest discover -v
```

Testy używają `unittest.mock`, aby zasymulować odpowiedź API i zweryfikować, że filtrowanie i zapis do CSV działają poprawnie.


## Skąd bierzemy dane?

Kursy pobierane są z [NBP Web API](https://api.nbp.pl/):

```
https://api.nbp.pl/api/exchangerates/tables/A?format=json
```

---

© 2025 Currency Monitor
