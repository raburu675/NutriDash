from django.shortcuts import render
from django.http import HttpResponse
import plotly.express as px
import pandas as pd
from plotly.offline import plot # Import plot from plotly.offline


def home(request):
    # Your data for the chart
    calorie_data = {
        'day' : ['Mon','Tue','Wed','Thurs','Fri','Sat','Sun'],
        'calories' : [2000,2200,1800,2500,2100,3000,1990]
    }
    # Create a Pandas DataFrame from your data
    df = pd.DataFrame(calorie_data)
    

    # Create the Plotly bar chart
    fig = px.bar(df, x='day', y='calories', height=200, width=300)
     # Update the layout for height and width
    # --- Add this part to reduce margins ---
    fig.update_layout(
        margin=dict(
            l=10,  # left margin
            r=20,  # right margin
            t=10,  # top margin (leave some space for title if present)
            b=10   # bottom margin (leave some space for x-axis labels)
        ),
        bargap=0.8        
    )   

    # Convert the Plotly figure to an HTML div string    
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)# include_plotlyjs=False is important if you load Plotly.js globally in your base template
    # Prepare the context dictionary to pass data to the template
    context = {
        'plot_div':plot_div
    }

    # Render the home.html template, passing the context
    return render(request, 'myapp1/home.html', context)

def settings(request):
    #  Renders the settings page template located at templates/myapp1/settings.html.    
    return render(request, 'myapp1/settings.html', {})