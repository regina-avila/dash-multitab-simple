import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_3_layout = html.Div([
    html.H1('Page 3'),
    html.Div([
        html.Div([
            html.H6('Select one:'),
            dcc.Slider(
                id='page-3-slider',
                min=1,
                max=100,
                step=10,
                marks=marks={
        0: {'label': 'Just ate', 'style': {'color': green}},
        50: {'label': 'I could eat', 'style': {'color': yellow}},
        100: {'label': 'FEED ME NOW', 'style': {'color': 'red'}}
    },
                value=0,
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-3-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')
