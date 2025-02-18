import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QPushButton, QLabel, QComboBox, 
                           QLineEdit, QTableWidget, QTableWidgetItem, QTabWidget,
                           QFileDialog, QMessageBox, QSpinBox, QDateEdit)
from PyQt5.QtCore import Qt, QDateTime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import backtrader as bt
import datetime
import pandas as pd
import yfinance as yf

class TradingGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backtrader Trading Platform")
        self.setGeometry(100, 100, 1200, 800)
        
        # Hauptwidget und Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Tabs erstellen
        tabs = QTabWidget()
        layout.addWidget(tabs)
        
        # Strategy Tab
        strategy_tab = QWidget()
        strategy_layout = QVBoxLayout(strategy_tab)
        
        # Strategie-Auswahl
        strategy_selection = QHBoxLayout()
        strategy_label = QLabel("Strategie:")
        self.strategy_combo = QComboBox()
        self.strategy_combo.addItems(["SMA Crossover", "RSI Strategy", "MACD Strategy"])
        strategy_selection.addWidget(strategy_label)
        strategy_selection.addWidget(self.strategy_combo)
        strategy_layout.addLayout(strategy_selection)
        
        # Parameter-Einstellungen
        params_layout = QHBoxLayout()
        
        # SMA Parameter
        self.sma1_spin = QSpinBox()
        self.sma1_spin.setRange(1, 200)
        self.sma1_spin.setValue(20)
        self.sma2_spin = QSpinBox()
        self.sma2_spin.setRange(1, 200)
        self.sma2_spin.setValue(50)
        
        params_layout.addWidget(QLabel("SMA1 Period:"))
        params_layout.addWidget(self.sma1_spin)
        params_layout.addWidget(QLabel("SMA2 Period:"))
        params_layout.addWidget(self.sma2_spin)
        strategy_layout.addLayout(params_layout)
        
        # Datum-Auswahl
        date_layout = QHBoxLayout()
        self.start_date = QDateEdit()
        self.start_date.setDateTime(QDateTime.currentDateTime().addYears(-1))
        self.end_date = QDateEdit()
        self.end_date.setDateTime(QDateTime.currentDateTime())
        
        date_layout.addWidget(QLabel("Start Datum:"))
        date_layout.addWidget(self.start_date)
        date_layout.addWidget(QLabel("End Datum:"))
        date_layout.addWidget(self.end_date)
        strategy_layout.addLayout(date_layout)
        
        # Symbol-Eingabe
        symbol_layout = QHBoxLayout()
        self.symbol_input = QLineEdit()
        self.symbol_input.setPlaceholderText("z.B. AAPL")
        symbol_layout.addWidget(QLabel("Symbol:"))
        symbol_layout.addWidget(self.symbol_input)
        strategy_layout.addLayout(symbol_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.run_button = QPushButton("Strategie ausführen")
        self.run_button.clicked.connect(self.run_strategy)
        button_layout.addWidget(self.run_button)
        strategy_layout.addLayout(button_layout)
        
        # Chart-Bereich
        self.figure = Figure(figsize=(15, 6))
        self.canvas = FigureCanvas(self.figure)
        strategy_layout.addWidget(self.canvas)
        
        # Ergebnis-Tabelle
        self.result_table = QTableWidget()
        self.result_table.setColumnCount(4)
        self.result_table.setHorizontalHeaderLabels(
            ["Datum", "Aktion", "Preis", "Position"])
        strategy_layout.addWidget(self.result_table)
        
        tabs.addTab(strategy_tab, "Strategie")
        
        # Data Tab
        data_tab = QWidget()
        data_layout = QVBoxLayout(data_tab)
        
        # Daten-Import Buttons
        import_layout = QHBoxLayout()
        self.import_csv_button = QPushButton("CSV importieren")
        self.import_csv_button.clicked.connect(self.import_csv)
        import_layout.addWidget(self.import_csv_button)
        
        self.download_data_button = QPushButton("Daten herunterladen")
        self.download_data_button.clicked.connect(self.download_data)
        import_layout.addWidget(self.download_data_button)
        
        data_layout.addLayout(import_layout)
        
        tabs.addTab(data_tab, "Daten")
        
        # Settings Tab
        settings_tab = QWidget()
        settings_layout = QVBoxLayout(settings_tab)
        
        # Broker-Einstellungen
        broker_layout = QHBoxLayout()
        self.cash_input = QSpinBox()
        self.cash_input.setRange(1000, 1000000)
        self.cash_input.setValue(100000)
        self.cash_input.setSingleStep(1000)
        
        broker_layout.addWidget(QLabel("Start-Kapital:"))
        broker_layout.addWidget(self.cash_input)
        settings_layout.addLayout(broker_layout)
        
        # Commission-Einstellungen
        commission_layout = QHBoxLayout()
        self.commission_input = QLineEdit()
        self.commission_input.setText("0.001")
        
        commission_layout.addWidget(QLabel("Kommission:"))
        commission_layout.addWidget(self.commission_input)
        settings_layout.addLayout(commission_layout)
        
        tabs.addTab(settings_tab, "Einstellungen")
        
        self.cerebro = None
        self.data = None

    def run_strategy(self):
        if not self.symbol_input.text():
            QMessageBox.warning(self, "Fehler", "Bitte geben Sie ein Symbol ein!")
            return
            
        try:
            # Cerebro-Instanz erstellen
            self.cerebro = bt.Cerebro()
            
            # Daten herunterladen
            data = self.download_data()
            if data is None:
                return
                
            self.cerebro.adddata(data)
            
            # Strategie basierend auf Auswahl hinzufügen
            if self.strategy_combo.currentText() == "SMA Crossover":
                class SmaCross(bt.Strategy):
                    params = dict(
                        pfast=20,
                        pslow=50
                    )

                    def __init__(self):
                        sma1 = bt.indicators.SMA(period=self.p.pfast)
                        sma2 = bt.indicators.SMA(period=self.p.pslow)
                        self.crossover = bt.indicators.CrossOver(sma1, sma2)

                    def next(self):
                        if not self.position:
                            if self.crossover > 0:
                                self.buy()
                        elif self.crossover < 0:
                            self.sell()
                
                self.cerebro.addstrategy(SmaCross, 
                                       pfast=self.sma1_spin.value(),
                                       pslow=self.sma2_spin.value())
            
            # Broker-Einstellungen
            self.cerebro.broker.setcash(self.cash_input.value())
            self.cerebro.broker.setcommission(
                commission=float(self.commission_input.text())
            )
            
            # Strategie ausführen
            results = self.cerebro.run()
            
            # Chart erstellen
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            
            # Portfolio-Wert plotten
            portfolio_value = [v for v in results[0].observers.broker]
            ax.plot(portfolio_value)
            ax.set_title('Portfolio Wert')
            self.canvas.draw()
            
            # Ergebnistabelle aktualisieren
            self.update_result_table(results[0])
            
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Ausführen der Strategie: {str(e)}")

    def update_result_table(self, strategy):
        self.result_table.setRowCount(0)
        # Hier würden wir die Trades in die Tabelle einfügen
        # Dies ist ein vereinfachtes Beispiel
        for i, trade in enumerate(strategy.trades):
            self.result_table.insertRow(i)
            self.result_table.setItem(i, 0, QTableWidgetItem(str(trade.data.datetime.date())))
            self.result_table.setItem(i, 1, QTableWidgetItem("BUY" if trade.size > 0 else "SELL"))
            self.result_table.setItem(i, 2, QTableWidgetItem(f"{trade.price:.2f}"))
            self.result_table.setItem(i, 3, QTableWidgetItem(f"{trade.size}"))

    def import_csv(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "CSV-Datei öffnen", "", "CSV Files (*.csv)")
        if filename:
            try:
                # CSV-Datei einlesen und in Backtrader-Format konvertieren
                df = pd.read_csv(filename)
                # Hier würden wir die Daten verarbeiten
                QMessageBox.information(self, "Erfolg", "CSV-Datei erfolgreich importiert!")
            except Exception as e:
                QMessageBox.critical(self, "Fehler", f"Fehler beim Importieren: {str(e)}")

    def download_data(self):
        symbol = self.symbol_input.text()
        if not symbol:
            QMessageBox.warning(self, "Fehler", "Bitte geben Sie ein Symbol ein!")
            return
            
        try:
            # Daten von Yahoo Finance herunterladen
            start_date = self.start_date.date().toPyDate()
            end_date = self.end_date.date().toPyDate()
            
            ticker = yf.Ticker(symbol)
            df = ticker.history(start=start_date, end=end_date)
            
            # Daten in Backtrader-Format konvertieren
            data = bt.feeds.PandasData(
                dataname=df,
                datetime=None,  # Verwende den Index
                open='Open',
                high='High',
                low='Low',
                close='Close',
                volume='Volume',
                openinterest=-1  # Nicht verwendet
            )
            
            QMessageBox.information(self, "Erfolg", f"Daten für {symbol} erfolgreich heruntergeladen!")
            return data
            
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Herunterladen: {str(e)}")
            return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = TradingGUI()
    gui.show()
    sys.exit(app.exec())
