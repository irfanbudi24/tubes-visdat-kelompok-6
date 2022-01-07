from bokeh.plotting import figure, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models import Panel, Spinner, ColorPicker
from bokeh.layouts import column, row
import pandas as pd


def barplot(df):
    # Create ColumnDataSource from data frame
    source = ColumnDataSource(df)

    # List Wilayah
    list_wilayah = source.data['WilayahJawaBarat'].tolist()
    list_wilayah.reverse()

    # Add plot
    p1 = figure(
        y_range=list_wilayah,
        plot_width=1800,
        plot_height=1000,
        title='Tingkat Pengangguran di Wilayah Jawa Barat',
        x_axis_label='Jumlah Pengangguran (Persen)',
        y_axis_label='Wilayah',
        tools="zoom_in,zoom_out,save,reset",
        toolbar_location='above'
    )

    # Render glyph
    bar =  p1.hbar(
        y='WilayahJawaBarat',
        right='2018',
        left=0,
        height=0.6,
        fill_color='orange',
        color = 'black',
        fill_alpha=0.5,
        source=source,
    )


    # Add Tooltips
    hover = HoverTool()
    hover.tooltips = """
      <div>
        <h3>@WilayahJawaBarat</h3>
        <div><strong>Tahun: </strong>@2018</div>
        <div><strong>Wilayah: </strong>@WilayahJawaBarat</div>
      </div>
    """
    p1.add_tools(hover)

    #spinner bar height
    spinner1 = Spinner(title="Bar Height", low=0.1, high=1, step=0.1, value=0.6, width=100)
    spinner1.js_link('value', bar.glyph, 'height')

    #spinner bar fill alpha
    spinner2 = Spinner(title="Bar Fill Alpha", low=0.1, high=1, step=0.1, value=0.5, width=100)
    spinner2.js_link('value', bar.glyph, 'fill_alpha')

    #picker bar color
    picker = ColorPicker(title="Bar Color", width = 100)
    picker.js_link('color', bar.glyph, 'fill_color')

    widgets = column(spinner1, spinner2, picker)

    layout = row(widgets, p1)

    tab1 = Panel(child=layout, title="BAR PLOT")

    return tab1

