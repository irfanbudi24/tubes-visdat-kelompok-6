import pandas as pd

from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import TableColumn, DataTable

def table(df):
        source = ColumnDataSource(df)

	    # Columns of table
        columns = [
					 TableColumn(field='WilayahJawaBarat', title='Wilayah Jawa Barat'),
					 TableColumn(field='2018', title='Tahun 2018'),
					 TableColumn(field='2019', title='Tahun 2019'),
					 TableColumn(field='2020', title='Tahun 2020'),
					 TableColumn(field='Total', title='Total'),
                                         TableColumn(field='ID', title='ID'),
                     ]

        data_table = DataTable(source=source, columns=columns, width=1000, height=700)
        tab4 = Panel(child = data_table, title = 'TABLE')

        return tab4