from download_datasets import download_datasets
download_datasets()

import streamlit as st# app.py
import pickle

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity_movies = pickle.load(open('similarity.pkl', 'rb'))
shows = pickle.load(open('shows_list.pkl', 'rb'))
similarity_shows = pickle.load(open('similarity1.pkl', 'rb'))

# Recommender functions
def recommend_movie(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity_movies[idx])), reverse=True, key=lambda x: x[1])[1:11]
    recommended = [movies.iloc[i[0]].title for i in distances]
    return recommended

def recommend_show(show):
    idx = shows[shows['title'] == show].index[0]
    distances = sorted(list(enumerate(similarity_shows[idx])), reverse=True, key=lambda x: x[1])[1:11]
    recommended = [shows.iloc[i[0]].title for i in distances]
    return recommended

# Streamlit UI
st.title("Movies and Shows Recommendation System")

# Selection
option = st.radio("What would you like to get recommendations for?", ["Movies", "TV Shows"])

if option == "Movies":
    selected_movie = st.selectbox("Choose a Movie", movies['title'].values)
    if st.button("Recommend Movies"):
        recommendations = recommend_movie(selected_movie)
        st.subheader("Recommended Movies:")
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")

elif option == "TV Shows":
    selected_show = st.selectbox("Choose a TV Show", shows['title'].values)
    if st.button("Recommend Shows"):
        recommendations = recommend_show(selected_show)
        st.subheader("Recommended TV Shows:")
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")
