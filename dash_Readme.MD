# Dashboard Code

This repository contains a Python script for creating a dashboard using Dash and Plotly. The dashboard displays various graphs and visualizations based on data from a CSV file.

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3 (https://www.python.org/downloads/)
- Dash (https://dash.plotly.com/installation)
- Plotly (https://plotly.com/python/getting-started/)

## Getting Started


1. Install the required dependencies by running the following command:

   ```
   pip install dash plotly pandas
   ```

2. Place your data file in the same directory as the `app_dash.py` file. The data file should be in CSV format.

3. Run the following command to start the dashboard:

   ```
   python dashboard.py
   ```

4. Enter the filename

5. Open your web browser and go to [http://127.0.0.1:8050/](http://127.0.0.1:8050/) to view the dashboard.

## Updating the Data

To update the data displayed in the dashboard, follow these steps:

1. Replace the `merged_file.csv` file with your updated data file. Make sure the file has the same structure (columns) as the original file.

2. Click the "Update Data" button in the dashboard. This will trigger the graphs to update based on the new data.





