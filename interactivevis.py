# Your Name Brandon Sapp
# si649f20 altair transforms 2

# imports we will use
import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
import pprint


#Title
st.title("Does Size Really Matter")
st.write("Norway, the seemingly inconspicuoius country, actually crushed the  2018 Winter Olympics! Despite it's size, Norway is consistently a top contender in the Olympics exceeding even the largest and most competitive nation. Bellow, we'll talk about some of Norway's other leading qualities and what really matters when it comes to Olympic success.")
#Import data
datasetURL="https://raw.githubusercontent.com/brandonUMSI/si649/main/static.csv" 
com_data=pd.read_csv(datasetURL,encoding="latin-1")
alt.themes.enable('fivethirtyeight')


#Sidebar
side_options = ['page1', 'page2']
side_select = st.sidebar.selectbox(label="Select a Visualization to Display!", options = side_options)

###### Making of all the charts


########Vis 1
hover_selection = alt.selection_single(on='mouseover', empty='none')
opacity_condition = alt.condition(hover_selection, alt.value(1.0), alt.value(0.6))

input_dropdown = alt.binding_select(options=['Gold','Silver','Bronze'],name='Medal Type ')
selection = alt.selection_single(fields=['medalty'], bind=input_dropdown, name='Medal Type')

brush_selection = alt.selection_interval()

color = alt.condition(selection,
                      alt.Color('medalty:N',title = "Medal Type",legend=None,
                      scale=alt.Scale(
            domain=['Gold', 'Silver', 'Bronze'],
            range=['gold','lightslategray','chocolate'])),
                      alt.value('lightgray'))

vis1chart=alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_bar(height=15).encode(
    y = alt.Y('Rank:O',axis=None,sort=alt.EncodingSortField(field='Rank', order='ascending')),
    x = alt.X('medalam:Q',title="Medals Won"),
    color = color,
    tooltip=['Country',alt.Tooltip('Rank', title='2018 Olympic Rank'),'Gold','Silver','Bronze',alt.Tooltip('Total', title='Medals Won')],
    opacity=opacity_condition
).add_selection(hover_selection,selection).transform_filter(brush_selection)


vis1text = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_text().encode(
    text=alt.Text('Country:N'),
    y = alt.Y('Rank:O',axis=None,sort=alt.EncodingSortField(field='Rank', order='ascending')),
    opacity=opacity_condition
).add_selection(hover_selection, brush_selection).properties(width=20)


vis1_rule = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).transform_filter(

    alt.datum.Rank <= 1).mark_text(color='red').encode(
    text=alt.Text('Country:N'),
    y='Rank:O',
)


nicon = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).transform_filter(

    alt.datum.Rank <= 1).mark_image(
    width=25,
    height=25,
    align='left',
    baseline='middle',
    dx=3,
).encode(
    y = alt.Y('Rank:O',axis=None,sort=alt.EncodingSortField(field='Rank', order='ascending')),
    
    url='Background'
)
all_text = vis1text + vis1_rule 
vis1 = (all_text|vis1chart + nicon)



vis2_hover = alt.selection_single(on='mouseover', empty='none', encodings=['x'])
vis2_hoverNear = alt.selection_single(on='mouseover', empty='none', nearest=True, encodings=['x'])
vis2_zoom = alt.selection_interval(bind='scales', encodings=['x'])
vis2_opacityCondition = alt.condition(vis2_hoverNear, alt.value(1.0), alt.value(0))

#Gold
vis2_rule = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_rule(size=4, color='lightgray').encode(
    x='Gold:Q',
    opacity=vis2_opacityCondition
).add_selection(vis2_hoverNear)

vis2_dot = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_circle(size=70, color='black').encode(
    x=alt.X('Gold:Q'),
    y=alt.Y('Country:N',sort=alt.EncodingSortField(field='Rank', order='ascending')),
    tooltip=["Country","Gold",alt.Tooltip('Rank', title='2018 Olympic Ranking')],
    opacity=vis2_opacityCondition
).add_selection(vis2_hover)

vis2_line = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_line(size=2.5,color="gold").encode(
    x=alt.X('Gold:Q', title='',axis=None),
    y=alt.Y('Country:N', axis=None, title='',sort=alt.EncodingSortField(field='Rank', order='ascending')),
    
).add_selection(vis2_zoom)


#Silver
vis2_ruleb = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_rule(size=4, color='lightgray').encode(
    x='Silver:Q',
    opacity=vis2_opacityCondition
).add_selection(vis2_hoverNear)

vis2_dotb = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_circle(size=70, color='black').encode(
    x=alt.X('Silver:Q'),
    y=alt.Y('Country:N',sort=alt.EncodingSortField(field='Rank', order='ascending')),
    tooltip=["Country","Silver",alt.Tooltip('Rank', title='2018 Olympic Ranking')],
    opacity=vis2_opacityCondition
).add_selection(vis2_hover)

vis2_lineb = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_line(size=2.5,color="lightslategray").encode(
    x=alt.X('Silver:Q', title='',axis=None),
    y=alt.Y('Country:N', axis=None, title='',sort=alt.EncodingSortField(field='Rank', order='ascending')),
    
).add_selection(vis2_zoom)


#bronze
vis2_rulec = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_rule(size=4, color='lightgray').encode(
    x='Bronze:Q',
    opacity=vis2_opacityCondition
).add_selection(vis2_hoverNear)

vis2_dotc = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_circle(size=70, color='black').encode(
    x=alt.X('Bronze:Q'),
    y=alt.Y('Country:N',sort=alt.EncodingSortField(field='Rank', order='ascending')),
    tooltip=["Country","Bronze",alt.Tooltip('Rank', title='2018 Olympic Ranking')],
    opacity=vis2_opacityCondition
).add_selection(vis2_hover)

vis2_linec = alt.Chart(com_data).transform_fold(
    ["Gold","Silver","Bronze"],
    as_=["medalty","medalam"]).mark_line(size=2.5,color="chocolate").encode(
    x=alt.X('Bronze:Q', title='',axis=None),
    y=alt.Y('Country:N', axis=None, title='',sort=alt.EncodingSortField(field='Rank', order='ascending')),
    
).add_selection(vis2_zoom)






vis2 = (vis2_line+vis2_rule+vis2_dot).resolve_scale().properties(
    title = "Gold",
    width=150,
    height=150 
)

vis2b = (vis2_lineb+vis2_ruleb+vis2_dotb).resolve_scale().properties(
    title = "Silver",
    width=150,
    height=150 
)


vis2c = (vis2_linec+vis2_rulec+vis2_dotc).resolve_scale().properties(
    title = "Bronze",
    width=150,
    height=150 
)

btmvis = (vis2b & vis2 & vis2c).properties(
    title="",
)


page1 = (vis1 | btmvis).properties(title="2018 Winter Olympics").configure_view(strokeWidth=0)


########Vis 2

chart1 = alt.Chart(com_data).mark_point().encode(
    y = alt.Y('Happiness Rank National:O',title="Happiness Rank"),
    x = alt.X('Total:Q',title="Total Medals Won"),   
).properties(
    title="Happiness",
)

chart2 = alt.Chart(com_data).mark_point().encode(
    y = alt.Y('GNI:O',title="GNI Per Capita",sort=alt.EncodingSortField(field='GNI', order='descending')),
    x = alt.X('Total:Q',title="Total Medals Won"),   
).properties(
    title="Income",
)

chart3 = alt.Chart(com_data).mark_point().encode(
    y = alt.Y('GINI:O',title="GINI (lower is better)"),
    x = alt.X('Total:Q',title="Total Medals Won"),      
).properties(
    title="Wealth Equality",
)

chart4 = alt.Chart(com_data).mark_point().encode(
    y = alt.Y('Life Expectancy:O',title="Life Expectancy",sort=alt.EncodingSortField(field='Life Expectancy', order='descending')),
    x = alt.X('Total:Q',title="Total Medals Won"),
      
).properties(
    title="Life Expectancy",
)

HDI_min = com_data["HDI_INT"].min()
HDI_max = com_data["HDI_INT"].max()

Rank_min = com_data["Rank"].min()
Rank_max = com_data["Rank"].max()


slider = alt.binding_range(
    min = HDI_min,
    max = HDI_max,
    step = 1,
    name = "HDI"
)

selector = alt.selection_single(
    bind = slider,
    fields = ["HDI"],
    init = {"HDI":HDI_max}
)

slider2 = alt.binding_range(
    min = Rank_min,
    max = Rank_max,
    step = 1,
    name = "OlympicRanking"
)

selector2 = alt.selection_single(
    bind = slider2,
    fields = ["OlympicRanking"],
    init = {"OlympicRanking":Rank_max}
)


c1 = chart1.encode(
    size=alt.condition(alt.datum.HDI_INT <= selector.HDI,alt.SizeValue(300),alt.SizeValue(10)),
    color=alt.condition(alt.datum.Rank <= selector2.OlympicRanking,alt.Color("HDI_INT:Q",title="HDI"),alt.value("gray")),
    tooltip=['Country', alt.Tooltip('Happiness Rank National', title='Universal Happiness Rank'),alt.Tooltip('Rank', title='2018 Olympic Ranking'),'Gold','Silver','Bronze']
).add_selection(selector,selector2).properties(
    width=200,
    height=200
).interactive()

c2 = chart2.encode(
    size=alt.condition(alt.datum.HDI_INT <= selector.HDI,alt.SizeValue(300),alt.SizeValue(10)),
    color=alt.condition(alt.datum.Rank <= selector2.OlympicRanking,alt.Color("HDI_INT:Q",title="HDI"),alt.value("gray")),
    tooltip=['Country', alt.Tooltip('GNI', title='Gross National Income Per Capita'),alt.Tooltip('Rank', title='2018 Olympic Ranking'),'Gold','Silver','Bronze']
).add_selection(selector,selector2).properties(
    width=200,
    height=200
).interactive()

c3 = chart3.encode(
    size=alt.condition(alt.datum.HDI_INT <= selector.HDI,alt.SizeValue(300),alt.SizeValue(10)),
    color=alt.condition(alt.datum.Rank <= selector2.OlympicRanking,alt.Color("HDI_INT:Q",title="HDI"),alt.value("gray")),
    tooltip=['Country', alt.Tooltip('GINI', title='GINI Coeffecient'),alt.Tooltip('Rank', title='2018 Olympic Ranking'),'Gold','Silver','Bronze']
).add_selection(selector,selector2).properties(
    width=200,
    height=200
).interactive()

c4 = chart4.encode(
    size=alt.condition(alt.datum.HDI_INT <= selector.HDI,alt.SizeValue(300),alt.SizeValue(10)),
    color=alt.condition(alt.datum.Rank <= selector2.OlympicRanking,alt.Color("HDI_INT:Q",title="HDI"),alt.value("gray")),
    tooltip=['Country', 'Life Expectancy',alt.Tooltip('Rank', title='2018 Olympic Ranking'),'Gold','Silver','Bronze']
).add_selection(selector,selector2).properties(
    width=200,
    height=200
).interactive()

page2=((c1 | c2) & (c3 | c4)).properties(title="Quality Life, Quality Score",)



##### Display graphs

if side_select == 'page1':
    page1
    st.write("Use the side options to select the next visualizations")

elif side_select == 'page2':
    st.write("Use the side options to select the next visualizations")
   
    page2



