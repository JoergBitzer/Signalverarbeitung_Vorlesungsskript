import yfinance
import matplotlib
from matplotlib import pyplot

try: 
    if get_ipython().__class__.__name__ == 'ZMQInteractiveShell':
        prefix = ''
except:
    prefix = '../../'

matplotlib.style.use(f'{prefix}sv.mplstyle')

dax = yfinance.Ticker("DAX") # chooses the DAX stock
data = dax.history(period="1wk") # gets course data as pandas Dataframe
close = data[["Close"]] # selects the Close coulumn in the Dataframe
close.plot(marker='X', color='black')

# glue this figure to paste it later (no effect outside of MyST NB)
from myst_nb import glue
glue("daxkurs", pyplot.gcf(), display=False)

pyplot.show()