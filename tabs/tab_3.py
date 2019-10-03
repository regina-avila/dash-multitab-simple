import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_3_layout = html.Div([
    html.H1('How Hungry Are You?'),
    html.Div([
        html.Div([
            html.H6('Select one:'),
            dcc.Slider(
                id='page-3-slider',
                min=0,
                max=100,
                step=50,
                marks={
        0: {'label': 'I could eat', 'style': {'color': '#32CD32', 'textAlign' : 'right'}},
        50: {'label': 'Peckish', 'style': {'color': '#FFA500'}},
        100: {'label': 'FEED ME NOW', 'style': {'color': '#FF0000'}}
    },
                value=0,
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-3-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')
