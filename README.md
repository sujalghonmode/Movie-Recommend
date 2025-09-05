# Movie Recommender System

This project is a content-based movie recommender system built with Python and Streamlit. It uses movie metadata from TMDB and recommends similar movies based on user selection.

## Features
- Content-based recommendations using movie metadata
- Interactive web app with Streamlit
- Movie poster display using TMDB API

## How to Run
1. Clone the repository:
   ```
   git clone https://github.com/sujalghonmode/Movie-Recommend.git
   cd Movie-Recommend-Clean
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Files
- `movie-recommender.ipynb`: Jupyter notebook for data processing and model creation
- `app.py`: Streamlit web app for movie recommendations
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation

## Note
- Large files like `similarity.pkl` are ignored in version control via `.gitignore`.
- You need a valid TMDB API key for fetching movie posters.
