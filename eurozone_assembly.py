import plotly.express as px
import plotly.graph_objects as go

def eurozone_assembly_sunburst(data):
    fig = px.sunburst(data, path=['Region','Party', 'Country'], values='Seats',color='Party',
                color_discrete_map={'LEFT':'HotPink','Greens/EFA':'ForestGreen','S&D':'Crimson','RE':'Gold',
                                   'EPP':'RoyalBlue','ECR':'Navy','ID':'Black','Other':'DarkGray',
                                    '(?)':'LightGray'}, height=750, width=820,
                      title="<b style='font-size:1.5rem';>Balance of Power in an Eurozone Assembly</a>"
                      "<br><i style='font-size:1.1rem'>Seats in the committee allocated to national parties per<br>population size and national parliaments' seat distribution </i>", template="seaborn")
    fig.update_traces(hovertemplate='%{value} Seats')

    fig.layout.images = [dict(
        source="./static/thumbnail.png",
        xref="paper", yref="paper",
        x=0.92, y=1.034,
        sizex=0.1, sizey=0.18,
        xanchor="center", yanchor="bottom"
    )]

    fig.add_annotation(x=0.5, y=-0.1,
            text="<span style='font-size:1rem'>Note: Distribution as of 10/2022; Italy's M5S sorted into Greens/EFA</span>",
            showarrow=False,
            xref="paper", yref="paper")

    fig.update_layout(plot_bgcolor="rgb(197,204,211)", paper_bgcolor="rgb(207,214,221)")
    fig.update(layout=go.Layout(margin=dict(t=120, b=95, l=0, r=0)))

    return fig.to_html(full_html=False, config={'displayModeBar': False})