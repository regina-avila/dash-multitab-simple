import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
#importing my own scripts tab_1.py, tab_2.py, tab_3.py
#could also from tab_1 import function...
from tabs import tab_1
from tabs import tab_2
from tabs import tab_3

########### Define your variables ######

myheading1 = 'Bobb\'s Burger Order Form'
tabtitle = 'Burger Order Form'
sourceurl = 'https://dash.plot.ly/dash-core-components/tabs'
githublink = 'https://github.com/regina-avila/dash-multitab-simple'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle
app.config['suppress_callback_exceptions'] = True


########### Set up the layout

app.layout = html.Div([
    html.H1(myheading1),
    dcc.Tabs(id="tabs-example", value='tab-1-example',
            children=[
                dcc.Tab(label='Burger Type', value='tab-1-example'),
                dcc.Tab(label='Burger Temp', value='tab-2-example'),
                #dcc.Tab(label='R U Hungry', value='tab-3-example'),
                #each of the dcc.tabs children is dcc.tab (singular, which must be tied into a callback
    ]),
    html.Div([
        html.Div(id='tabs-content-example'),
    ], className='twelve columns',
        style={'marginBottom': 50, 'marginTop': 25}),
    html.Div([
        html.A('Code on Github', href=githublink),
        html.Br(),
        html.A("Data Source", href=sourceurl),
    ], className='twelve columns',
        style={'textAlign':'right',
                'fontColor':'#FFFFFF',
               #this is the style for the footer. must be outside the bracket contents of the div?
                'backgroundColor':'#D3D3D3',})
])

@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab_1.tab_1_layout
    #this is defined in the script for the tab
    elif tab == 'tab-2-example':
        return tab_2.tab_2_layout
    elif tab == 'tab-3-example':
        return tab_3.tab_3_layout

# Tab 1 callback
@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              #page-1-content is the second callback, that exists in the tab_1.py the callback lives here in app.py
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    #return 'You have selected "{}"'.format(value)
    burger_you_chose=f'{value}.jpeg'
    return html.Img(src=app.get_asset_url(burger_you_chose), style={'width': 'auto', 'height': 'auto'}),

# Tab 2 callback
@app.callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])
def page_2_radios(value):
    #return 'You have selected "{}"'.format(value)
    temp_you_chose=f'{value}.jpeg'
#Display image of burger with temp selected
    return html.Img(src=app.get_asset_url(temp_you_chose), style={'width': 'auto', 'height': 'auto'}),

'''
# Tab 3 callback
@app.callback(Output('page-3-content', 'children'),
              [Input('page-3-slider', 'value')])
def page_3_slider(value):
    #how do i turn these into string??
    return f'You have selected "{str(value)}"'
'''

############ Deploy
if __name__ == '__main__':
#the above is there to specify - only run the server if the main of this script is== the system variable main
#will prevent wrong one from fire accidentally when being imported (like 'secondary')
    app.run_server(debug=True)
    

