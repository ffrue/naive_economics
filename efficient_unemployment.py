import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def efficient_unemployment(data,country):
    graph = data[data['name']==country]

    fig = px.line(graph, x='time', y=['Vacancy Rate','Unemployment Rate','Efficient Unemployment'],
                 title="<b style='font-size:1.1rem';>Labor Market Slack in " + pd.unique(graph['name'])[0] + "</b>"
                  "<br><i style='font-size:0.8rem;'>Analysis following Michaillat & Saez 2022, Data from Eurostat</i>",
                  template="seaborn")

    fig.update_layout(showlegend=True)
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.98,
        xanchor="left",title="",
        x=0.2, bordercolor='black',
        orientation="h"
    ))

    fig.update_layout(title_x=0.5)

    fig.update_layout(xaxis_title="",
                      yaxis_title="")
    fig.update_xaxes(gridcolor='rgb(115,115,115)',color='black',linecolor='black')
    fig.update_yaxes(gridcolor='rgb(115,115,115)',color='black',linecolor='black',
                     zerolinecolor='rgb(115,115,115)',ticksuffix="% ", range=[-0.5,max(graph['Unemployment Rate']*1.2)])

    fig.layout.images = [dict(
        source="./static/thumbnail.png",
        xref="paper", yref="paper",
        x=0.96, y=1.04,
        sizex=0.1, sizey=0.18,
        xanchor="center", yanchor="bottom"
    )]

    fig.update_layout(plot_bgcolor="rgb(197,204,211)", paper_bgcolor="rgb(207,214,221)")
    fig.update(layout=go.Layout(margin=dict(t=90, b=65, l=70, r=30)))

    return fig.to_html(full_html=False, default_width='100%', config={'displayModeBar': False})