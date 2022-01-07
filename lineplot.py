import pandas as pd
from bokeh.plotting import figure, output_file
from bokeh.models import Panel
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models import Spinner, ColorPicker
from bokeh.layouts import row, column

output_file('output.html')

def lineplot(df):
    source = ColumnDataSource(df)

    p3 = figure(
        plot_width=1500,
        plot_height=800,
        title='Tingkat Pengangguran di Wilayah Jawa Barat',
        x_axis_label='Kode Wilayah Jawa Barat',
        y_axis_label='Total Pengangguran dari 2018 sampai 2020',
    )

    # Add Tooltips
    hover = HoverTool()
    hover.tooltips = """
     <div>
        <h3>@WilayahJawaBarat</h3>
        <div><strong>Nama Wilayah: </strong>@WilayahJawaBarat</div>
        <div><strong>Tahun 2018: </strong>@2018</div>
        <div><strong>Tahun 2019: </strong>@2019</div>
        <div><strong>Tahun 2020: </strong>@2020</div>
      </div>
    """
    p3.add_tools(hover)

    line =  p3.line(x='ID', y='Total', line_width=3, source=source)

    #spinner line width
    spinner = Spinner(title="Line Width", low=1, high=20, step=1, value=3, width=100)
    spinner.js_link('value', line.glyph, 'line_width')

    #picker line color
    picker = ColorPicker(title="Line Color", width = 100)
    picker.js_link('color', line.glyph, 'line_color')

    widgets = column(spinner, picker)

    layout = row(widgets, p3)


    tab3 = Panel(child=layout, title="LINE PLOT")


    return tab3
