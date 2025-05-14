import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from currency_monitor.fetcher import fetch_exchange_rates

class CurrencyMonitorApp:
    def __init__(self, root):
        self.root = root
        root.title("Currency Monitor")
        root.geometry("400x400")

        # --- Tabela kursów (Treeview) ---
        self.tree = ttk.Treeview(root, columns=("currency", "rate"), show="headings")
        self.tree.heading("currency", text="Waluta")
        self.tree.heading("rate", text="Kurs (PLN)")
        self.tree.pack(pady=10)

        # --- Obszar na wykres matplotlib ---
        self.figure = plt.Figure(figsize=(4,3), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Aktualne kursy walut")
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()

        # --- Przycisk Odśwież ---
        self.button = tk.Button(root, text="Odśwież", command=self.refresh)
        self.button.pack(pady=10)

        # Pierwsze załadowanie danych
        self.refresh()

    def refresh(self):
        # Pobierz kursy walut
        rates = fetch_exchange_rates()

        # Uaktualnij tabelę: usuń poprzednie wiersze
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Wstaw nowe wiersze
        for code, rate in rates.items():
            self.tree.insert("", "end", values=(code, rate))

        # Uaktualnij wykres słupkowy
        self.ax.clear()
        currencies = list(rates.keys())
        values = list(rates.values())
        self.ax.bar(currencies, values, color='skyblue')
        self.ax.set_title("Aktualne kursy walut")
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyMonitorApp(root)
    root.mainloop()