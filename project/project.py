#!/usr/bin/env python

class Project:

baseurl = "https://www.nodc.noaa.gov/archive/arc0023/0052765/1.1/data/0-data/NODC_2004-2006_Data_Archive/"
nut_2004_url = "Tijuana%20River/nutrient/data/tjrnut2004.txt"
nut_2005_url = "Tijuana%20River/nutrient/data/tjrnut2005.txt"
met_2004_url = "Tijuana%20River/meteorological/data/Tidal%20Linkage/tjrtlmet2004.txt"
met_2005_url = "Tijuana%20River/meteorological/data/Tidal%20Linkage/tjrtlmet2005.txt"
DEFAULT_TICKERS = ['CHLA_N', 'NH4F', 'TotPAR', 'ATemp', 'MaxTemp']

def nix(val, lst):
    return [x for x in lst if x != val]

def load_ticker(ticker):
    nut2004data = pd.read_table(baseurl+nut_2004_url,sep='\t',header=(0),parse_dates=['SMPLDATE'])
    nut2005data = pd.read_table(baseurl+nut_2005_url,sep='\t',header=(0),parse_dates=['SMPLDATE'])
    met2004data = pd.read_table(baseurl+met_2004_url,sep='\t',header=(0),parse_dates=['SMPLDATE'])
    met2005data = pd.read_table(baseurl+met_2004_url,sep='\t',header=(0),parse_dates=['SMPLDATE'])
    nut2004data = nut2004data.set_index(nut2004df.CHLA_N)
    nut2005data = nut2005data.set_index(nut2005df.CHLA_N)
    #met2004data = met2004data.set_index('SMPLDATE')
    #met2005data = met2005data.set_index('SMPLDATE')
    return pd.DataFrame({ticker: nut2004df.CHLA_N, ticker+'_returns': nut2004df.CHLA_N.diff()})

def get_data(y1, y2):
    df1 = load_ticker(y1)
    df2 = load_ticker(y2)
    data = pd.concat([df1, df2], axis=1)
    data = data.dropna()
    data['y1'] = data[y1]
    data['y2'] = data[y2]
    #data['t1_returns'] = data[nut2004df.CHLA_N]
    #data['t2_returns'] = data[nut2005df.CHLA_N]
    return data

# set up widgets


ticker1 = Select(value='CHLA_N', options=nix('NH4F', DEFAULT_TICKERS))
ticker2 = Select(value='NH4F', options=nix('CHLA_N', DEFAULT_TICKERS))

# set up plots

source = ColumnDataSource(data=dict(date=[], y1=[], y2=[], t1_returns=[], t2_returns=[]))
source_static = ColumnDataSource(data=dict(date=[], y1=[], y2=[], t1_returns=[], t2_returns=[]))
tools = 'pan,wheel_zoom,xbox_select,reset'

corr = figure(plot_width=350, plot_height=350,
              tools='pan,wheel_zoom,box_select,reset')
corr.circle('t1_returns', 't2_returns', size=2, source=source,
            selection_color="orange", alpha=0.6, nonselection_alpha=0.1, selection_alpha=0.4)

ys1 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='datetime', active_drag="xbox_select")
ys1.line('date', 'y1', source=source_static)
ys1.circle('date', 'y1', size=1, source=source, color=None, selection_color="orange")

ys2 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='datetime', active_drag="xbox_select")
ys2.x_range = ys1.x_range
ys2.line('date', 'y2', source=source_static)
ys2.circle('date', 'y2', size=1, source=source, color=None, selection_color="orange")

# set up callbacks

def ticker1_change(attrname, old, new):
    ticker2.options = nix(new, DEFAULT_TICKERS)
    update()

def ticker2_change(attrname, old, new):
    ticker1.options = nix(new, DEFAULT_TICKERS)
    update()

def update(selected=None):
    y1, y2 = ticker1.value, ticker2.value

    data = get_data(y1, y2)
    source.data = source.from_df(data[['y1', 'y2']])
    source_static.data = source.data

    corr.title.text = '%s returns vs. %s returns' % (y1, y2)
    ys1.title.text, ys2.title.text = y1, y2

ticker1.on_change('value', ticker1_change)
ticker2.on_change('value', ticker2_change)

def selection_change(attrname, old, new):
    y1, y2 = ticker1.value, ticker2.value
    data = get_data(y1, y2)
    selected = source.selected.indices
    if selected:
        data = data.iloc[selected, :]

source.on_change('selected', selection_change)

# set up layout
widgets = column(ticker1, ticker2)
main_row = row(corr, widgets)
series = column(ys1, ys2)
layout = column(main_row, series)

# initialize
update()

curdoc().add_root(layout)
curdoc().title = "Stocks"