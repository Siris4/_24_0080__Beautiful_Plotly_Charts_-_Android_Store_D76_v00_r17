import pandas as pd
import plotly.graph_objects as go

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0080__Day76_Beautiful_Plotly_Charts_&_Android_Store__240820\NewProject\r00-r09 START\r00_env_START\apps.csv'
df = pd.read_csv(file_path)

# Clean the 'Installs' column by removing commas and plus signs, then convert to integer
df['Installs'] = df['Installs'].str.replace(',', '').str.replace('+', '').astype(int)

# Create a DataFrame with the total number of apps and the number of installs per category
category_summary = df.groupby('Category').agg({
    'App': 'count',   # Count the number of apps
    'Installs': 'sum' # Sum the number of installs
}).rename(columns={'App': 'Total_Apps', 'Installs': 'Total_Installs'})

# Sort the DataFrame by 'Total_Installs' in descending order
category_summary_sorted = category_summary.sort_values(by='Total_Installs', ascending=False)

# Adjust the size of the markers by scaling them down
scaled_size = category_summary_sorted['Total_Apps'] / 25  # Scale down the marker size

# Create a scatter plot with Plotly
fig = go.Figure(data=go.Scatter(
    x=category_summary_sorted['Total_Apps'],        # x-axis: Total number of apps
    y=category_summary_sorted['Total_Installs'],    # y-axis: Total number of installs
    mode='markers',
    marker=dict(
        size=scaled_size, # Scaled marker size
        color=category_summary_sorted['Total_Installs'], # Color based on total installs
        showscale=True   # Show the color scale
    ),
    text=category_summary_sorted.index  # Display category names on hover
))

# Update the layout to add titles and labels
fig.update_layout(
    title="Total Installs vs. Total Apps by Category",
    xaxis_title="Total Number of Apps",
    yaxis_title="Total Number of Installs",
    hovermode="closest"
)

# Show the plot
fig.show()
