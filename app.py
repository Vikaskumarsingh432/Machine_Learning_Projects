import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies_list['title'].iloc[i[0]])

    return recommended_movies

movies_list = pickle.load(open('movies.pkl', 'rb'))
#movies_list = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')
Selected_movie_name = st.selectbox('How would you like to be connected', movies_list['title'])

if st.button('Recommend'):
    recommendation = recommend(Selected_movie_name)
    for i in recommendation:
        st.write(i)

# To run this in terminal write streamlit run app.py


