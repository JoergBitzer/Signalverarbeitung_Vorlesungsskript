import yfinance
import matplotlib
from matplotlib import pyplot
import pandas

matplotlib.style.use('sv1_style.mplstyle')

dax = yfinance.Ticker("DAX") # wähle Aktie aus
data = dax.history(period="1wk") # hole Kursdaten bis 1 Woche zurückliegend
close = data[["Close"]] # extrahiere den Stand am Ende des Tages
close.plot(marker='X', color='black') # und plotte ihn
pyplot.show()