from django.shortcuts import render
from django.http import HttpResponse
import plotly.express as px
import pandas as pd
from plotly.offline import plot # Import plot from plotly.offline


def home(request):
    # code for the bar chart
    calorie_data = {
        'day' : ['Mon','Tue','Wed','Thurs','Fri','Sat','Sun'],
        'calories' : [2000,3200,1800,2500,2100,3000,1990]
    }
    df = pd.DataFrame(calorie_data)       

    # Create the Plotly bar chart
    fig = px.bar(df, x='day', y='calories',width=450 ,height=450, title='daily calorie overview')     
    # Reduce extra margins around the bars
    fig.update_layout(
        margin=dict(
            l=60,  # left margin
            r=60,  # right margin
            t=40,  # top margin (leave some space for title if present)
            b=10   # bottom margin (leave some space for x-axis labels)
        ),
        paper_bgcolor='rgba(0,0,0,0)', # Set the paper background to transparent                
    )    

    # Convert the Plotly figure to an HTML div string        
    plot_div = fig.to_html(full_html=False, include_plotlyjs='cdn')        


    


    # code for the pie chart-
    #dataframe to hold the data
    dailyIntake_data = ({
        'foodType' : ['calories','proteins','carbs'],
        'intake' : [1200,2300,1100]
    })
    df_pie = pd.DataFrame(dailyIntake_data)

    #create a pie chart figure to display the proportions of the daily food intake
    fig_pie = px.pie(df_pie , names='foodType' ,values='intake', hole=0.6)
    # Use update_layout to set a smaller width and height for the chart
    fig_pie.update_layout(
        width=350,  # Set the width to 400 pixels
        height=200, # Set the height to 400 pixels
        margin=dict(t=30, b=20, l=10, r=10), # Reduce the top, bottom, left, and right margins
        paper_bgcolor='rgba(0,0,0,0)', # Set the paper background to transparent
        title={'x':0.5, 'xanchor': 'center'} # Center the title
    )
    #update the traces to display lables and percentages
    fig_pie.update_traces(textposition='inside' , textinfo='label+percent+value')

    # Convert the pie chart to an HTML div
    pie_chart_div = fig_pie.to_html(full_html=False, include_plotlyjs='cdn')

    context = {
        'plot_div':plot_div,
        'pie_chart_div': pie_chart_div
        }

    # Render the home.html template, passing the context
    return render(request, 'myapp1/home.html', context)    



def settings(request):
    #  Renders the settings page template located at templates/myapp1/settings.html.    
    return render(request, 'myapp1/settings.html', {})   

def analytics(request):
    return render(request,'myapp1/analytics.html',{})

def account(request):
    return render(request,'myapp1/account.html')

def login(request):
    return render(request, 'myapp1/login.html')

def signup(request):
    return render(request, 'myapp1/signup.html')

