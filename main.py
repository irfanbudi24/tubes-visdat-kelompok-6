from bokeh.io import curdoc, show
from bokeh.models.widgets import Tabs
from bokeh.plotting import output_file


from os.path import dirname, join
import pandas as pd


from kodingan.barplot import barplot
from kodingan.marker_map import marker_map
from kodingan.lineplot import lineplot
from kodingan.table import table

output_file('TUBES.html')

df = pd.read_csv(r'C:\Users\Irfan Budi Prakoso\OneDrive - Telkom University\Documents\TUBES\TUBES\PLE.csv')
curdoc().theme = 'dark_minimal'

tab1 = barplot(df)
# tab2 = marker_map(df)
tab3 = lineplot(df)
tab4 = table(df)

tabs = Tabs(tabs=[tab1, tab3, tab4])
# tab2,tab3,tab4])

show(tabs)