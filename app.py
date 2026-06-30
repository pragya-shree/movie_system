import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# 🔥 Safe Poster Fetch
# ---------------------------
@st.cache_data
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url, timeout=5).json()

        poster_path = data.get('poster_path')

        if not poster_path:
            return "https://via.placeholder.com/500x750?text=No+Image"

        return "https://image.tmdb.org/t/p/w500/" + poster_path

    except:
        return "https://via.placeholder.com/500x750?text=Error"


# ---------------------------
# 🎯 Recommendation Logic
# ---------------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# ---------------------------
# 📦 Load Data
# ---------------------------
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


# ---------------------------
# 🎬 HERO SECTION (TOP)
# ---------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #E50914; font-size: 42px;'>
        MOVIE RECOMMENDER
    </h1>
    <p style='text-align: center; color: #bbbbbb; font-size: 16px;'>
        Discover movies based on your taste using Machine Learning
    </p>
    <hr style="border: 1px solid #333;">
    """,
    unsafe_allow_html=True
)


# ---------------------------
# 🔍 INPUT SECTION
# ---------------------------
st.markdown("### 🎥 Search Movie")
selected_movie_name = st.selectbox(
    "🎥 Select a movie",
    movies['title'].values,
    label_visibility="collapsed"
)


# ---------------------------
# 🎯 BUTTON + OUTPUT
# ---------------------------
if st.button('🎬 Show Recommendations'):

    with st.spinner("Fetching best recommendations... 🎯"):
        names, posters = recommend(selected_movie_name)

    st.markdown("## 🍿 Recommended for You")

    cols = st.columns(5)

    for i in range(len(names)):
        with cols[i]:
            st.markdown(
                """
                <div style="
                    background-color: #1a1a1a;
                    padding: 10px;
                    border-radius: 12px;
                    text-align: center;
                    height: 100%;
                ">
                """,
                unsafe_allow_html=True
            )

            st.image(posters[i], width="stretch")

            st.markdown(
                f"""
                <p style="
                    color: white;
                    font-size: 14px;
                    font-weight: 600;
                    margin-top: 8px;
                ">
                {names[i]}
                </p>
                """,
                unsafe_allow_html=True
            )

            st.markdown("</div>", unsafe_allow_html=True)