"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
    application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

    For further help with the Streamlit framework, see:

    https://docs.streamlit.io/en/latest/

"""

# Streamlit dependencies
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np


# Custom Libraries
from utils.data_loader import load_movie_titles



# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Solution Overview", "Explore Dataset", "About us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("EA Movie Recommender System")

        st.image('resources/imgs/Image_header.png',use_column_width=True)
        st.title("THE MOVIE RECOMMENDER SYSTEM")
        st.write("By leveraging both content-based and collaborative filtering techniques, our recommender app achieves unparalleled accuracy in understanding user preferences. Content-based analysis focuses on individual user behaviors and product attributes, while collaborative filtering taps into collective user data, fostering a comprehensive understanding. This dual approach ensures precision in generating recommendations, creating a powerful synergy that elevates user satisfaction and enhances business performance")
        st.write("So, it's like having a buddy who understands your taste in movies and shows, helping you discover content you'll likely enjoy. To achieve this, the app uses smart filters such as collaborative filtering, which considers your viewing history and preferences, and content-based filtering, focusing on specific features like genres and actors to tailor personalized recommendations just for you")
        st.title("OBJECTIVE")
        st.write("Our mission is to redefine personalized recommendations in the digital landscape through our advanced recommender app. We strive to enhance user satisfaction by employing state-of-the-art content-based and collaborative filtering techniques. Our goal is to empower businesses with a tool that not only boosts sales and customer loyalty but also sets new standards for precision and effectiveness in delivering tailored recommendations, thereby positioning us as industry leaders in this dynamic market")
        st.title("View raw data")
        st.title("RESOURCES")

    if page_selection == "Explore Dataset":
        st.title("Explore Dataset")
        st.write("Here you can explore the dataset used in the recommender system.")
        # Load the CSV file
        df = pd.read_csv(r'C:\Users\Kearabilwe\Desktop\Filters\resources\data\movies.csv')
        # Display the DataFrame as a table
        st.write('### Movies Data:')
        st.dataframe(df)
        df = pd.read_csv(r'C:\Users\Kearabilwe\Desktop\Filters\resources\data\ratings.csv')
        # Display the DataFrame as a table
        st.write('### Ratings')
        st.dataframe(df)
        st.title("About dataset")
        st.write("The recommender Streamlit app displays top-rated and popular movies, user ratings distribution, and personalized recommendations, allowing users to explore and discover movies based on their preferences and interactions")

    if page_selection == "About us":
        st.title("About us")
        local_image_path = "C:\\Users\\Kearabilwe\\Desktop\\Filters\\resources\\imgs\\M2C.jpeg"
        st.image(local_image_path, caption="M2C", use_column_width=True)
        st.write("Meet the team")
        st.markdown("""
            Welcome to our Streamlit App! We're a team of passionate individuals dedicated to making your experience delightful.
            Let us introduce ourselves:
        """)

        team_members = [
            {"name": "Eugene Sibanda", "role": "Technical Lead", "bio": "Turning caffeine into code since 20XX."},
            {"name": "Nonkanyiso Mabaso", "role": "Development/Project Lead", "bio": "Making projects smoother than a cup of hot cocoa."},
            {"name": "Kearabilwe Montshiwa", "role": "Backend Development","bio": "Transforming server requests into digital magic."},
            {"name": "Asiphe Nkome", "role": "Front-end Development", "bio": "Weaving pixels and code into beautiful experiences."},
            {"name": "Kaya Dumasi", "role": "Development/ScrumMaster","bio": "Guiding the team through the agile wilderness."}
        ]
        # Display team members
        for member in team_members:
            st.write(f"*{member['name']}*")
            st.write(f"Role: {member['role']}")
            st.write(f"Bio: {member['bio']}")
            st.write("---")  # Separator between team members

if __name__ == '__main__':
    main()
