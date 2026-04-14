import streamlit as st 
import nltk
import sklearn
import pandas as pd
import pickle
import joblib


st.title('Movie Recommendation system')


with open('movies.pickle','rb') as m:
    movies = pickle.load(m)

top_similarities = joblib.load('top_similarities.joblib')

movies_names = movies['title'].values

def recommend(name_movie):
    movie_index = movies[movies['title'] == name_movie].index[0]
    movie_list = top_similarities[movie_index]

    recommended_movies = []

    for i in movie_list[:5]:
        recommended_movies.append(movies.iloc[i].title)
    
    return recommended_movies

name_movie = st.selectbox('Enter the Movie Name',movies_names)

if st.button('Recommend'):
    r = recommend(name_movie)
    st.write('The Recommended Movies are :')

    for i in r:
        st.write(i)