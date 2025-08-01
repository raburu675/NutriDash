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
    df = pd.DataFrame(calorie_data)       

    # Create the Plotly bar chart
    fig = px.bar(df, x='day', y='calories',width=400 ,height=200, title='calorie overview')     
    # Reduce extra margins around the bars
    fig.update_layout(
        margin=dict(
            l=10,  # left margin
            r=20,  # right margin
            t=50,  # top margin (leave some space for title if present)
            b=10   # bottom margin (leave some space for x-axis labels)
        )                
    )    

    # Convert the Plotly figure to an HTML div string        
    plot_div = fig.to_html(full_html=False, include_plotlyjs='cdn')    
    context = {'plot_div':plot_div}

    # Render the home.html template, passing the context
    return render(request, 'myapp1/home.html', context)

def settings(request):
    #  Renders the settings page template located at templates/myapp1/settings.html.    
    return render(request, 'myapp1/settings.html', {})