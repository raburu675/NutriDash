from django.shortcuts import render
from django.http import HttpResponse
import plotly.express as px
import pandas as pd
from plotly.offline import plot # Import plot from plotly.offline


def home(request):
    # Your data for the chart
    calorie_data = {
        'day' : ['Mon','Tue','Wed','Thurs','Fri','Sat','Sun'],
        'calories' : [2000,3200,1800,2500,2100,3000,1990]
    }
    # Create a Pandas DataFrame from your data
    df = pd.DataFrame(calorie_data)
    # --- Debugging: Print DataFrame to console ---
    print("debugging dataframe content")
    print(df)
    print("------------------------------------")
    

    # Create the Plotly bar chart
    fig = px.bar(df, x='day', y='calories',width=400 ,height=200)
     # Update the layout for height and width
    # --- Add this part to reduce margins ---
    fig.update_layout(
        margin=dict(
            l=10,  # left margin
            r=20,  # right margin
            t=20,  # top margin (leave some space for title if present)
            b=10   # bottom margin (leave some space for x-axis labels)
        )                
    )    

    # Convert the Plotly figure to an HTML div string    
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)# include_plotlyjs=False is important if you load Plotly.js globally in your base template
    # Prepare the context dictionary to pass data to the template
    # --- Debugging: Print a snippet of plot_div to console ---
    print("\n--- Debugging: plot_div (first 500 chars) ---")
    print(plot_div[:500]) # Print only the beginning to avoid cluttering the console
    print("---------------------------------------------")
    context = {
        'plot_div':plot_div
    }

    # Render the home.html template, passing the context
    return render(request, 'myapp1/home.html', context)

def settings(request):
    #  Renders the settings page template located at templates/myapp1/settings.html.    
    return render(request, 'myapp1/settings.html', {})