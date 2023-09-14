# Import required libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Load and preprocess the data
# Reading the CSV data file into a pandas DataFrame
filename = input("enter the .csv file:")
data = pd.read_csv(str(filename)+".csv")
# data = pd.read_csv("merged_file.csv")

# Converting the 'Datetime' column to datetime format for easier manipulation
data['Datetime'] = pd.to_datetime(data['Datetime'])

# Define the layout of the Dash app
# The layout consists of a title, an 'Update Data' button, and several sections each with a graph
app.layout = html.Div(style={'backgroundColor': '#f5f5f5'}, children=[
    # App title
    html.H1("DashBoard", style={'textAlign': 'center', 'paddingTop': '20px'}),

    # 'Update Data' button
    # When clicked, this button will trigger all the graphs to update
    html.Div(
        style={'width': '100%', 'textAlign': 'center'},
        children=[
            html.Button('Update Data', 
                        id='update-button', 
                        n_clicks=0, 
                        style={
                            'backgroundColor': 'transparent',
                            'backgroundImage': 'linear-gradient(45deg, #d74771, #9438a6)',
                            'border': 'none',
                            'color': 'white',
                            'padding': '10px 30px',
                            'textAlign': 'center',
                            'textDecoration': 'none',
                            'display': 'inline-block',
                            'fontSize': '16px',
                            'margin': '4px 2px',
                            'cursor': 'pointer',
                            'borderRadius': '10px'
                        })
        ]
    ),

    # Section 1: Average and Peak People Count
    html.H2('Average and Peak People Count', style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id='average-peak-graph'),
    ]),

    # Section 2: Department-wise People Count
    html.H2('Department-wise People Count', style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id='department-count-graph'),
    ]),

    # Section 3: Top 5 Desks with Most Consistent Occupancy
    html.H2('Top 5 Desks with Most Consistent Occupancy', style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id='top-desks-graph'),
    ]),

    # Section 4: Overall People Count Trends over Day of Week
    html.H2('Overall People Count Trends over Day of Week', style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id='count-by-day-graph'),
    ]),

    # Section 5: Overall People Count Trends over Time
    html.H2('Overall People Count Trends over Time', style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id='count-over-time-graph'),
    ]),

    # Section 6: Outliers
    html.H2('Outliers', style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id='outliers-graph'),
    ]),
])


# Define the callback for updating the 'average-peak-graph'
# This callback is triggered when the 'Update Data' button is clicked
# It calculates the average and peak people count and plots them as a bar chart
@app.callback(
    Output('average-peak-graph', 'figure'),
    [Input('update-button', 'n_clicks')]
)
def update_average_peak_graph(n_clicks):
    # Calculate the average and peak people count
    average_people_count = data['peopleCount'].mean()
    peak_people_count = data['peopleCount'].max()

    # Create the bar chart
    fig = px.bar(x=['Average People Count', 'Peak People Count'], 
                 y=[average_people_count, peak_people_count],
                 color=['Average People Count', 'Peak People Count'],
                 labels={'x': '', 'y': 'Count'},
                 color_discrete_map={
                    "Average People Count": "#1f77b4",
                    "Peak People Count": "#ff7f0e"
                },
                 title='Average and Peak People Count')
    fig.update_layout(template="plotly_white")
    return fig

# Define the callback for updating the 'department-count-graph'
# This callback is triggered when the 'Update Data' button is clicked
# It calculates the total people count by department and plots it as a bar chart
@app.callback(
    Output('department-count-graph', 'figure'),
    [Input('update-button', 'n_clicks')]
)
def update_department_count_graph(n_clicks):
    # Calculate the total people count by department
    department_counts = data.groupby('department')['peopleCount'].sum().reset_index()

    # Create the bar chart
    fig = px.bar(department_counts, 
                 x='department', 
                 y='peopleCount', 
                 color='department',
                 labels={'department': '', 'peopleCount': 'People Count'},
                 title='Department-wise People Count')
    fig.update_layout(template="plotly_white")
    return fig

# Define the callback for updating the 'top-desks-graph'
# This callback is triggered when the 'Update Data' button is clicked
# It calculates the occupancy rate for each desk and plots the top 5 desks as a bar chart
@app.callback(
    Output('top-desks-graph', 'figure'),
    [Input('update-button', 'n_clicks')]
)
def update_top_desks_graph(n_clicks):
    # Calculate the total people count and total capacity by desk
    total_people_count = data.groupby('name')['peopleCount'].sum()
    total_capacity = data.groupby('name')['capacity'].sum()

    # Calculate the occupancy rate for each desk
    desk_occupancy = (total_people_count / total_capacity) * 100
    # Get the top 5 desks with highest occupancy rate
    top_desks = desk_occupancy.sort_values(ascending=False).head(5)

    # Create the bar chart
    fig = px.bar(x=top_desks.index, 
                 y=top_desks.values, 
                 color=top_desks.index,
                 labels={'x': 'Desk', 'y': 'Occupancy Rate (%)'},
                 title='Top 5 Desks with Highest Occupancy Rates')
    fig.update_layout(template="plotly_white")
    return fig

# Define the callback for updating the 'count-by-day-graph'
# This callback is triggered when the 'Update Data' button is clicked
# It calculates the average people count by day of week and plots it as a line chart
@app.callback(
    Output('count-by-day-graph', 'figure'),
    [Input('update-button', 'n_clicks')]
)
def update_count_by_day_graph(n_clicks):
    # Calculate the average people count by day of week
    count_by_day = data.groupby(data['Datetime'].dt.dayofweek)['peopleCount'].mean()

    # Map the day of week index to the corresponding day name
    days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    count_by_day.index = count_by_day.index.map(days)

    # Create the line chart
    fig = px.line(x=count_by_day.index, 
                  y=count_by_day.values, 
                  labels={'x': 'Day of Week', 'y': 'Average People Count'},
                  title='Overall People Count Trends by Day of the Week')
    fig.update_layout(template="plotly_white")
    return fig

# Define the callback for updating the 'count-over-time-graph'
# This callback is triggered when the 'Update Data' button is clicked
# It calculates the average people count by time of day and plots it as a line chart
@app.callback(
    Output('count-over-time-graph', 'figure'),
    [Input('update-button', 'n_clicks')]
)
def update_count_over_time_graph(n_clicks):
    # Calculate the average people count by time of day
    count_over_time = data.groupby(data['Datetime'].dt.time)['peopleCount'].mean()
    count_over_time.index = count_over_time.index.astype(str)

    # Create the line chart
    fig = px.line(x=count_over_time.index, 
                  y=count_over_time.values, 
                  labels={'x': 'Time', 'y': 'People Count'},
                  title='Overall People Count Trends over Time')
    fig.update_layout(template="plotly_white")
    return fig

# Define the callback for updating the 'outliers-graph'
# This callback is triggered when the 'Update Data' button is clicked
# It plots the outliers in the 'posY' variable as a box plot
@app.callback(
    Output('outliers-graph', 'figure'),
    [Input('update-button', 'n_clicks')]
)
def update_outliers_graph(n_clicks):
    # Create the box plot
    fig = go.Figure()
    fig.add_trace(go.Box(y=data['posY'], boxmean=True, boxpoints='outliers', name='Outliers in posY',
                         marker_color='#3D9970'))
    fig.update_layout(template="plotly_white", title='Outliers in posY')
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
    # http://127.0.0.1:8050/