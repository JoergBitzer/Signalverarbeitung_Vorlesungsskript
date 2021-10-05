import yfinance
import matplotlib
from matplotlib import pyplot
import pandas

matplotlib.style.use('sv1_style.mplstyle')

dax = yfinance.Ticker("DAX") # chooses the DAX stock
data = dax.history(period="1wk") # gets course data as pandas Dataframe
close = data[["Close"]] # selects the Close coulumn in the Dataframe
close.plot(marker='X', color='black')
pyplot.show()