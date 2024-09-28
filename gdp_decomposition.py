import plotly.express as px
import plotly.graph_objects as go

# Figure with decade data

def figure_decade(decade_data,decade):
    df_graph = decade_data[decade_data['Decade']==decade].sort_values('GDP')

    fig = px.bar(df_graph,x='Country', template="seaborn", width=1000,
    title="<b>Decomposition of real GDP growth over the "+decade+"</b>",
    y=['Productivity', 'Average hours per employee','Employment rate','Participation rate','Population growth'])

    fig.add_trace(go.Scatter(x=df_graph['Country'],y=df_graph['GDP']*100,
                            mode='markers', showlegend=False, marker={'color':'black'}))

    fig.update_xaxes(gridcolor='rgb(197,204,211)',color='black',linecolor='black', title="", tickangle=70)
    fig.update_yaxes(gridcolor='rgb(115,115,115)',color='black',linecolor='black',ticksuffix="% ", title="")

    fig.update_layout(legend=dict(
        title="",
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0
    ))

    fig.add_annotation(x=-0.05, y=-0.6, xref="paper", yref="paper",
                text="Differences between actual growth rate (black) and sum of contributing factors due to rounding",
                showarrow=False,
                yshift=10)

    fig.update_layout(plot_bgcolor="rgb(197,204,211)", paper_bgcolor="rgb(207,214,221)")
    fig.update(layout=go.Layout(margin=dict(t=90, b=65, l=70, r=30)))

    return fig.to_html(full_html=False, config={'displayModeBar': False})

# Figure with annual data

def figure_annual(annual_data,c):
    years = annual_data[annual_data['Country']==c]['Year']
    df2_graph = annual_data[(annual_data['Country']==c) & (annual_data['Year'] > min(years))]

    fig = px.bar(df2_graph,x='Year', template="seaborn", width=1000,
        y=['Productivity', 'Average hours per employee','Employment rate','Participation rate','Population growth'],
        title="<b>Decomposition of real GDP growth in "+c+"</b>")
    fig.add_trace(go.Scatter(x=df2_graph['Year'],y=df2_graph['GDP']*100,
                            mode='markers', name='GDP growth rate', marker={'color':'black'}))
    # fig.add_trace(go.Scatter(x=df2_ger['Year'],y=df2_ger['check'],
    #                         mode='markers', name='Checke'))

    fig.update_xaxes(gridcolor='rgb(115,115,115)',color='black',linecolor='black', title="")
    fig.update_yaxes(gridcolor='rgb(115,115,115)',color='black',linecolor='black',ticksuffix="% ", title="")

    fig.update_layout(legend=dict(
        title="",
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="left",
        x=0
    ))

    fig.update_layout(plot_bgcolor="rgb(197,204,211)", paper_bgcolor="rgb(207,214,221)")
    fig.update(layout=go.Layout(margin=dict(t=90, b=65, l=70, r=30)))

    return fig.to_html(full_html=False, config={'displayModeBar': False})