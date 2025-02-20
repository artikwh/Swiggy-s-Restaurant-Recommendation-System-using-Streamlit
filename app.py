import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

#load the data
data = pd.read_csv('cleaned.csv')
encoded_data = pd.read_csv('encoded_data.csv')

#st.set_page_config(layout = "wide", initial_sidebar_state = "expanded")
st.subheader('Swiggy Restaurant Recommendion App''🍕')
st.write('Enter the details to get the restaurant recommendation')
col1, col2 = st.columns([2,7])
with col1:    
    #st.header("user preferences")
    city = st.selectbox('Select the city', data['city'].unique())
    cuisine = st.selectbox('Select the cuisine', data['cuisine'].unique())
    cost = st.slider('Select the cost', 0, 4000, 200, 50)
    rating = st.slider('Select the rating', 0, 5, 1, 1)

with col2:
    #st.write('Recommended Restaurants:')
    #input data
    filtered_data = data[(data['city']==city) & (data['cuisine']==cuisine) & (data['cost']<=cost) & (data['rating']>=rating)]
    #st.dataframe(filtered_data)
    if not filtered_data.empty:
        index = filtered_data.index[0]
        # Compute the cosine similarity matrix
        similarity_matrix = cosine_similarity(encoded_data)
        similarity_score= similarity_matrix[index]
        top_list = sorted(enumerate(similarity_matrix[index]), key = lambda x: x[1], reverse=True)[0:10]
        recommend_indices = [i for i,v in top_list]
        recommend_restaurants = data.iloc[recommend_indices]
        for i, v in recommend_restaurants.iterrows():
            #st.write(f"**{v['name']}**")
            st.markdown(f"""
            <h3 style='font-size: 24px;'><b>{v['name']}</b></h3>
            """, unsafe_allow_html=True)
            st.write(f"City: {v["city"]}")
            st.write(f"Cuisine: {v['cuisine']}")
            st.write(f"cost: {v["cost"]} | Rating: {"⭐"*int(v["rating"])}")
            st.write(f"Rating Count: {v["rating_count"]}")
            st.markdown("--------")
        st.dataframe(recommend_restaurants, hide_index=True)        
    else:
        st.write("No restaurants found with the selected criteria.")

