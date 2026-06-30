# 🎬 Movie Recommendation System

A machine learning-based movie recommender that suggests similar movies and displays posters using the TMDB API. Built with Python and Streamlit.

---
## Project Preview

A smart movie recommendation system that suggests similar movies using machine learning and shows real posters using TMDB API.

👉 Try it live here: https://moviesystem-mnznjrkqmbj5pnfubpmnos.streamlit.app/
---

## 📌 Features
- 🎯 Content-based movie recommendations
- 🎬 Movie posters using TMDB API
- ⚡ Fast similarity-based engine
- 🌐 Streamlit web app
- 📊 ML similarity model

---

## 🧠 Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- TMDB API

---

## 📸 Screenshots

### Screenshot 1
![Screenshot 1](/screenshots/Screenshot%202026-06-29%20213829.png)

### Screenshot 2
![Screenshot 2](/screenshots/Screenshot%202026-06-29%20213938.png)

### Screenshot 3
![Screenshot 3](/screenshots/Screenshot%202026-06-29%20214137.png)

### Screenshot 4
![Screenshot 4](/screenshots/Screenshot%202026-06-30%20140436.png)

## 🧠 How It Works

1. Movies are converted into feature vectors using NLP techniques  
2. Cosine similarity is used to find similar movies  
3. Top matching movies are recommended  
4. Posters are fetched using TMDB API  
5. Results are displayed using Streamlit UI

## 📊 Machine Learning Approach

- Technique: Content-Based Filtering  
- Vectorization: CountVectorizer / TF-IDF (depending on your code)  
- Similarity Metric: Cosine Similarity 

## 📁 Project Structure
movie_system/
├── streamlit_app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md

---

## ⚙️ How to Run Locally
git clone https://github.com/pragya-shree/movie_system.git
cd movie_system
pip install -r requirements.txt
streamlit run streamlit_app.py

---

## 🔑 API Setup (TMDB)
Get API key: https://www.themoviedb.org/settings/api  
Add in streamlit_app.py:
api_key = "YOUR_TMDB_API_KEY"

--- 

## 🌐 Links
- Live App: https://moviesystem-mnznjrkqmbj5pnfubpmnos.streamlit.app/
- GitHub: https://github.com/pragya-shree/movie_system
- TMDB API: https://www.themoviedb.org/settings/api

---

## ✨ Future Improvements
- Netflix-style UI
- Search feature
- Faster recommendations
- Mobile optimization

---

## 👨‍💻 Author
Pragya Shree

---

⭐ If you like this project, give it a star!
