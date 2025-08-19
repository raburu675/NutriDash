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
    fig_pie = px.pie(df_pie , names='foodType' ,values='intake', hole=0.4)
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

    #dataframe to show daily calorie intake againsta target
    calorie_intake = {
        'days': ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
        'calories':  [2100,2300,1950,1700,1900,2250,2134]
    }
    df = pd.DataFrame(calorie_intake)

    #define the daily calorie target
    calorie_target = 2170
    df['calorie_target'] = calorie_target

    # use pd.melt() to change the data from a wide format to a long format and combine the charts on the y axis to show intake and target
    #This is useful when you have one or more columns that act as identifier variables (id_vars) and other columns that contain values you want to stack into a single column (value_vars).
    df_melted = pd.melt(df, id_vars=['days'], value_vars=['calories', 'calorie_target'], var_name='line_type' ,value_name='value')
    #create the plotly line using the px.line
    fig = px.line(
        df_melted,
        x='days', 
        y='value', 
        color='line_type', # Differentiate lines by color
        line_shape='spline', # Creates a smooth line for the trend    
        title='Weekly Calorie Intake vs. Target',
        color_discrete_map={
            'calories': '#4285F4',
            'calorie_target': '#DB4437'
            }
    )

    #Customize the layout
    fig.update_layout(
        width = 600,
        height = 450,
        title={
            'text': 'Weekly Calorie Intake vs. Target',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='Day of the Week',
        yaxis_title='Calories (kcal)',
        font=dict(
            family="Inter, sans-serif",
            size=12,
            color="#333"
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title=None
        )
    )

    #Data to show weight tracker
    weight = {
    'Months' : ['January','Feburary','March','April','May','June','JUly','August','September','October','November','December'],
    'weight_kg' : [74.5, 72.1, 65.3, 68, 69.8, 72.1, 70.5, 67.1, 71.3, 73.7, 73.8, 74.1]
    }

    weight_df = pd.DataFrame(weight)
    #create the area chart using px.area
    fig_weight = px.area(
        weight_df,
        x='Months',
        y='weight_kg',
        title='weight tracker',
        labels={'weight_kg': 'Weight (kg)', 'day': 'Day of the Week'},
        line_shape='spline'
    )
    fig_weight.update_yaxes(range=[55, 76])
    fig_weight.update_layout(
        width = 600,
        height = 450,
        margin=dict(l=20, r=20, t=40, b=20),
    )

    melted_chart_div = fig.to_html(full_html=False, include_plotlyjs='cdn')
    weight_div = fig_weight.to_html(full_html=False, include_plotlyjs='cdn')

    context = {
        'melted_chart_div' : melted_chart_div,
        'weight_div' : weight_div
    }

    return render(request,'myapp1/analytics.html', context)







def account(request):
    return render(request,'myapp1/account.html')

def login(request):
    return render(request, 'myapp1/login.html')

def signup(request):
    return render(request, 'myapp1/signup.html')

