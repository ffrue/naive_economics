import plotly.express as px
import plotly.graph_objs as go

def mu_diagram(data,selected, measure):
    data.loc[data['Country'].isin(selected), 'selected'] = 1
    data.loc[data['Partner'].isin(selected), 'selected_partner'] = 1
    data_selected = data.groupby(['Country', 'Year', 'selected_partner']).sum().reset_index()[
        ['Country', 'Year', 'selected_partner', 'Share of Exports']]
    data_selected = data_selected.loc[data_selected['Country'].isin(selected)]
    data_selected = data_selected.loc[data_selected['selected_partner'] == 1]
    data_selected.loc[data_selected['Share of Exports'] == 0, 'Share of Exports'] = None
    data_selected['Decade'] = '1980s'
    data_selected.loc[(data_selected['Year'] > 1990) & (data_selected['Year'] < 2000), 'Decade'] = '1990s'
    data_selected.loc[(data_selected['Year'] > 2000) & (data_selected['Year'] < 2010), 'Decade'] = '2000s'
    data_selected.loc[(data_selected['Year'] > 2010) & (data_selected['Year'] < 2020), 'Decade'] = '2010s'
    data_selected1 = data_selected.groupby(['Country', 'Decade']).mean().reset_index()[
        ['Country', 'Decade', 'Share of Exports']]

    data_selected = data.loc[data['Country'].isin(selected)][
        ['Country', 'Year', 'Decade', 'gap_trend', 'gap_potential']]
    data_selected['gap_mean'] = data_selected['gap_trend'].groupby(data_selected['Year']).transform('mean')
    data_selected = data_selected.groupby(['Country', 'Decade']).corr().reset_index()
    data_selected2 = data_selected[data_selected['level_2'] == measure][['Country', 'Decade', 'Year']]
    data_selected2.rename({'Year': 'BC Correlation'}, axis=1, inplace=True)

    data_graph = data_selected1.merge(data_selected2).round(2)
    if len(selected) > 12:
        row1 = selected[0:11]
        row2 = selected[11:25]
        fig = px.line(data_graph.sort_values(by=['Decade', 'Share of Exports']), x='Share of Exports', y='BC Correlation',
                      color='Decade', hover_name='Country', template = 'seaborn',
                      title=str('<b style="font-size:1.1rem;">Would these Countries form a good Monetary Union?</b>'
                                '<br style="line-height:15px;"><i style="font-size:0.85rem;">' + ', '.join(row1) + '</i>'
                                '<br style="line-height:15px;"><i style="font-size:0.85rem;">' + ', '.join(row2) + '</i>'))
    else:
        fig = px.line(data_graph.sort_values(by=['Decade', 'Share of Exports']), x='Share of Exports', y='BC Correlation',
                      color='Decade', hover_name='Country', template = 'seaborn',
                      title=str('<b style="font-size:1.1rem;">Would these Countries form a good Monetary Union?</b>'
                                '<br style="line-height: 15px;"><i style="font-size:0.85rem;">' + ', '.join(selected) + '</i>'))
    fig.update_layout(xaxis_title="Share of Exports to MU (in %)", yaxis_title="BC Correlation with MU")
    fig.update_xaxes(range=[0, 100],gridcolor='rgb(115,115,115)',color='black',linecolor='black')
    fig.update_yaxes(range=[-1,1], gridcolor='rgb(115,115,115)',color='black',linecolor='black',zerolinecolor='rgb(115,115,115)')
    fig.layout.images = [dict(
        source="./static/thumbnail.png",
        xref="paper", yref="paper",
        x=1.09, y=1.1,
        sizex=0.15, sizey=0.2,
        xanchor="center", yanchor="bottom"
    )]
    fig.update_layout(plot_bgcolor="rgb(197,204,211)", paper_bgcolor="rgb(207,214,221)")
    fig.update(layout=go.Layout(margin=dict(t=120, b=70, l=110, r=120)))
    return fig.to_html(full_html=False, config={'displayModeBar': False})

#def mu_map(data,selected):
#    data.loc[data['Country'].isin(selected),'selected'] = 1
#
#    fig = px.choropleth(data, locations="Country Code", color="selected", hover_name="Country", scope="europe",
#                   color_continuous_scale="Teal", width=350, title="Selected Countries")
#    fig.update_layout(
#        margin=dict(l=0,r=0,b=0,t=0),
#        paper_bgcolor="white"
#        )
#    fig.update_layout(coloraxis_showscale=False, title_x=0.5)
#    fig.write_html('./templates/mu_map.html', full_html=False)