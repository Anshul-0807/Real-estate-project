import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")

st.markdown("<h1 style='text-decoration: underline; font-family: Georgia, serif; '>Analytics</h1>", unsafe_allow_html=True)

new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl','rb'))


# group_df = new_df.groupby('sector').mean()[['price','price_per_sqft','built_up_area','latitude','longitude']]
numeric_columns = ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
group_df = new_df.groupby('sector')[numeric_columns].mean()

st.markdown("<h3 style='text-decoration: underline; color: #2E8B57; font-family: Georgia, serif;'>Sector Price per Sqft Geomap</h3>", unsafe_allow_html=True)
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)


st.plotly_chart(fig,use_container_width=True)

st.markdown("<h3 style='text-decoration: underline; font-family: Georgia, sans-serif; color: #FF5733;'>Features Wordcloud</h3>", unsafe_allow_html=True)

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size=10).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig)



# st.header("Area Vs Price")
st.markdown("<h3 style='text-decoration: underline; font-family: Georgia, serif; color: #6A5ACD;'>Area Vs Price</h3>", unsafe_allow_html=True)

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)

# st.header('BHK Pie Chart')
st.markdown("<h3 style='text-decoration: underline; font-family: Georgia, serif; color: #20B2AA;'>BHK Pie Chart</h3>", unsafe_allow_html=True)


sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)

# st.header('Side by Side BHK price comparison')
st.markdown("<h3 style='text-decoration: underline; font-family: Georgia, serif; color: #4682B4;'>Side by Side BHK price comparison</h3>", unsafe_allow_html=True)


fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


# st.header('Side by Side Distplot for property type')
st.markdown("<h3 style='text-decoration: underline; font-family: Georgia, serif; color: #FFD700;'>Side by Side Distplot for property type</h3>", unsafe_allow_html=True)


fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)
