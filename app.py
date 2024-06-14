from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Colleges Interactive Map", style={'textAlign':'center'}),
    html.Div(children='An Interactive Map of the Top 150 Colleges from US News over the years 1986-2024', 
            style={'textAlign':'center', 'marginBottom': '10px'}),
    dcc.Graph(id="output-graph",
            className="graph",
            style={
                'background-color': 'black',
                'margin-top': '10px',
                'font-family': 'Georgia',
                'width': '90%',
                'height': '90%',
                'align-self': 'center', 
                'justify-content': 'center',
                'margin': '0 auto'
            }),
    dcc.Dropdown(id = "dropdown", 
                className = "dropdown",
                style={
                    'width': '70%',
                    'border': '2px solid black',
                    'border-radius': '20px',
                    'margin-top': '10px',
                    'margin': '0 auto'
                },
                options=[
                    {'label': html.Span([
                        html.Img(src="./assets/images/acc.png", height=15),
                        html.Span(children="ACC", style={'font-size': 15, 'padding-left': 10, 'font-weight': 'bold'})],
                        style={'align-items': 'center', 'justify-content': 'center'}
                    ), 
                    'value': 'ACC'},
                    {'label': html.Span([
                        html.Img(src="./assets/images/big10.png", height=15),
                        html.Span(children="Big 10", style={'font-size': 15, 'padding-left': 10, 'font-weight': 'bold'})],
                        style={'align-items': 'center', 'justify-content': 'center'}
                    ),
                    'value': 'Big 10'},
                    {'label': html.Span([
                        html.Img(src="./assets/images/big12.png", height=20),
                        html.Span(children="Big 12", style={'font-size': 15, 'padding-left': 10, 'font-weight': 'bold'})],
                        style={'align-items': 'center', 'justify-content': 'center'}
                    ), 
                    'value': 'Big 12'},
                    {'label': html.Span([
                        html.Img(src="./assets/images/ivy.png", height=20),
                        html.Span(children="Ivy League", style={'font-size': 15, 'padding-left': 10, 'font-weight': 'bold'})],
                        style={'align-items': 'center', 'justify-content': 'center'}
                    ), 
                    'value': 'Ivy League'},
                    {'label': html.Span([
                        html.Img(src="./assets/images/sec.png", height=20),
                        html.Span(children="SEC", style={'font-size': 15, 'padding-left': 10, 'font-weight': 'bold'})],
                        style={'align-items': 'center', 'justify-content': 'center'}
                    ),
                    'value': 'SEC'},
                    {'label': html.Span([
                        html.Img(src="./assets/images/uaa.png", height=20),
                        html.Span(children="UAA", style={'font-size': 15, 'padding-left': 10, 'font-weight': 'bold'})],
                        style={'align-items': 'center', 'justify-content': 'center'}
                    ),
                    'value': 'UAA'}
                ],
                optionHeight=50,
                multi=True),
    
])

@callback(
    Output('output-graph', 'figure'),
    Input('dropdown', 'value')
)
def update_line_chart(selected_conferences):
    df = pd.read_csv('collegesformatted.csv')
    if selected_conferences:
        df = df[df['Conference'].isin(selected_conferences)]
    fig = px.line(df, x="Year", y="Rank", color="Name", markers=True)
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(
        plot_bgcolor='#3b3b3b',
        paper_bgcolor='#3b3b3b',
        font=dict(family="Georgia", size=12, color="white"),
        xaxis=dict(title="Year", titlefont=dict(family="Georgia", size=16, color="white")),
        yaxis=dict(title="Rank", titlefont=dict(family="Georgia", size=16, color="white")),
        legend=dict(font=dict(family="Georgia", size=12, color="white")),
        annotations=[
            dict(
                x=1, y=-0.1, xref='paper', yref='paper',
                text='Source: U.S. News & World Report',
                showarrow=False,
                font=dict(family="Georgia", size=12, color="white")
            )
        ],
        hoverlabel=dict(
            font_size=12,     # Font size of the hover label
            font_family="Georgia",  # Font family of the hover label
            font_weight='bold'
        )
    )
    return fig

# Don't change this
app.run_server(debug=True)