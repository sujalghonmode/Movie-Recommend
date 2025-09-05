import streamlit as st
import pickle
import pandas as pd
import requests

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)



def fetch_posters(movie_id):
    # response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0b0a99091379790ab0f26695c0400c33&language=en-US'.format(movie_id))
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjBhOTkwOTEzNzk3OTBhYjBmMjY2OTVjMDQwMGMzMyIsIm5iZiI6MTcyMDk0NDU1Mi4yMDUsInN1YiI6IjY2OTM4N2E4YjE4MDc2NGQ2ZDFjYzQ3NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dQJk7gSjh6oMLp7Hv6Kp27MxMlBgsvtQASrso-KzObY"
    }

    response = requests.get(url, headers=headers)
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']


similarity=pickle.load(open('similarity.pkl','rb'))


def recommended(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movie_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_posters(movie_id))

    return recommended_movies,recommended_movie_posters

st.title('Movie Recommender')
selected_name = st.selectbox(
    "Select a Movie you like:",
    movies['title'].values,
    index=None,
    placeholder="Select Movie Title"
)

if st.button("Recommend"):
    names,posters=recommended(selected_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:
        st.image(posters[3])
        st.text(names[3])
    with col5:
        st.image(posters[4])
        st.text(names[4])
