import pandas as pd
import plotly.graph_objects as go
import os
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt  # Add this line for creating the table

# Read data from CSV file
def make_graph(data):
    df=data
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Create a Plotly figure
    fig = go.Figure()

    # Add candlestick trace
    fig.add_trace(go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Candlestick'
    ))

    # Define the layout with dropdown and buttons
    fig.update_layout(
        title='Bitcoin Price',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Price (USD)'),
        updatemenus=[
            dict(
                type='dropdown',
                direction='down',
                buttons=list([
                    dict(label='Candlestick', method='relayout', args=[{'type': 'candlestick'}]),
                ]),
                x=0.01,
                xanchor='left',
                y=1.1,
                yanchor='top',
            )
        ]
    )

    # Save the interactive graph as an HTML file
    fig.write_html(os.path.join('mlmodel','templates','graph.html'))
    
    
def make_future_graph(data):


    # Read data from CSV file
    df = data  # Update 'your_data.csv' with the path to your CSV file

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Create a candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                        open=df['Open'],
                                        high=df['High'],
                                        low=df['Low'],
                                        close=df['Close'])])

    # Customize the layout
    fig.update_layout(title='Bitcoin Candlestick Chart',
                    xaxis_title='Date',
                    yaxis_title='Price')

    # Save the candlestick graph as PNG
    graph_png_path=os.path.join('mlmodel','media','bitcoin_future10_graph.png')
    fig.write_image(graph_png_path)
    # Generate HTML table
    table_html = df.to_html(index=False)

    # Save the HTML table as PNG
    
    table_png_path = os.path.join('mlmodel','media','bitcoin_future10_table.png')
    if os.path.exists(table_png_path):
        os.remove(table_png_path)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    plt.savefig(table_png_path)
