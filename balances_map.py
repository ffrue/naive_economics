import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def balances_map(data,countries,year):
    if len(countries) > 1:
        graph = data[(data['Year']==year) & (data['Name'].isin(countries))]
        imax = max(max(abs(graph['Trade Balance'])),max(abs(graph['Fiscal Balance'])))*1.1
        text = ["        " + i for i in graph['Country']]

        fig = px.scatter(graph, x='Trade Balance',y='Fiscal Balance',text=text,
                     title="<b style='font-size:1.1rem';>Sector Balances Map in " + str(year) + "</b>"
                      "<br><i style='font-size:0.8rem'>Data from Eurostat</i>", template="seaborn")

        fig.update_layout(showlegend=True, xaxis_title="Trade Balance", yaxis_title="Fiscal Balance")
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.95,
            xanchor="left",
            x=0.03, bordercolor='black'
        ))

        fig.add_trace(go.Scatter(x=[-imax,-imax,imax,-imax], y=[-imax,imax,imax,-imax], name="Private Sector Deficit",
                                 fillcolor="orange", fill="toself", opacity=0.1,mode='markers',hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=[-imax,imax,imax,-imax], y=[-imax,imax,-imax,-imax], name="Private Sector Surplus",
                                 fillcolor="green", fill="toself", opacity=0.1,mode='markers',hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=graph['Trade Balance'], y=graph['Fiscal Balance'],name="",
                         mode='markers',hovertext=graph['Name'],showlegend=False,marker=dict(color="#387ca0")))

        fig.update_xaxes(gridcolor='rgb(115,115,115)',color='black',linecolor='black',ticksuffix="% ",range=[-imax,imax],
                         zeroline=True, zerolinewidth=2, zerolinecolor='#e37166')
        fig.update_yaxes(gridcolor='rgb(115,115,115)',color='black',linecolor='black',ticksuffix="% ",range=[-imax,imax],
                         zeroline=True, zerolinewidth=2, zerolinecolor='#e37166')

        fig.layout.images = [dict(
            source="./static/thumbnail.png",
            xref="paper", yref="paper",
            x=0.96, y=1.034,
            sizex=0.1, sizey=0.18,
            xanchor="center", yanchor="bottom"
        )]

        fig.update_layout(plot_bgcolor="rgb(197,204,211)", paper_bgcolor="rgb(207,214,221)")
        fig.update(layout=go.Layout(margin=dict(t=90, b=60, l=90, r=40)))

        return fig.to_html(full_html=False, config={'displayModeBar': False})
    else:
        graph = data[data['Name']==countries[0]]
        imax = max(max(abs(graph['Trade Balance'])),max(abs(graph['Fiscal Balance'])))*1.1
        text =  ["          " + str(min(graph['Year']))] + [" "]*(len(graph['Year'])-2) + ["          " + str(max(graph['Year']))]

        fig = px.line(graph, x='Trade Balance',y='Fiscal Balance',text=text,
                     title="<b style='font-size:1.1rem';>Sector Balances Map for " + pd.unique(graph['Name'])[0] + "</b>"
                      "<br><i style='font-size:0.8rem'>Data from Eurostat</i>", template="seaborn")

        fig.update_layout(showlegend=True, xaxis_title="Trade Balance", yaxis_title="Fiscal Balance")
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.95,
            xanchor="left",
            x=0.03, bordercolor='black'
        ))

        fig.add_trace(go.Scatter(x=[-imax,-imax,imax,-imax], y=[-imax,imax,imax,-imax], name="Private Sector Deficit",
                                 fillcolor="orange", fill="toself", opacity=0.1,mode='markers',hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=[-imax,imax,imax,-imax], y=[-imax,imax,-imax,-imax], name="Private Sector Surplus",
                                 fillcolor="green", fill="toself", opacity=0.1,mode='markers',hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=graph['Trade Balance'], y=graph['Fiscal Balance'],name="",
                         mode='markers',hovertext=graph['Name'],showlegend=False,marker=dict(color="#387ca0")))

        fig.update_xaxes(gridcolor='rgb(115,115,115)',color='black',linecolor='black',ticksuffix="% ",range=[-imax,imax],
                         zeroline=True, zerolinewidth=2, zerolinecolor='#e37166')
        fig.update_yaxes(gridcolor='rgb(115,115,115)',color='black',linecolor='black',ticksuffix="% ",range=[-imax,imax],
                         zeroline=True, zerolinewidth=2, zerolinecolor='#e37166')

        fig.layout.images = [dict(
            source="./static/thumbnail.png",
            xref="paper", yref="paper",
            x=0.96, y=1.034,
            sizex=0.1, sizey=0.18,
            xanchor="center", yanchor="bottom"
        )]

        fig.update_layout(plot_bgcolor="rgb(197,204,211)", paper_bgcolor="rgb(207,214,221)")
        fig.update(layout=go.Layout(margin=dict(t=90, b=60, l=90, r=40)))

        return fig.to_html(full_html=False, config={'displayModeBar': False})