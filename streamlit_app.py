import streamlit as st
import pickle

st.title("🎬 Movie Recommendation System")

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies['title'].values

selected_movie = st.selectbox("Select a movie", movie_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movie_indices:
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations

if st.button("Recommend"):
    results = recommend(selected_movie)
    for i in results:
        st.write("👉", i)