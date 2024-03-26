import pandas as pd
import streamlit as st

TRAIN = "https://www.dropbox.com/scl/fi/5zy935lqpaqr9lat76ung/music_genre_train.csv?rlkey=ccovu9ml8pfi9whk1ba26zdda&dl=1"
TEST = "https://www.dropbox.com/scl/fi/o6mvsowpp9r3k2lejuegt/music_genre_test.csv?rlkey=ac14ydue0rzlh880jwj3ebum4&dl=1"

df1 = pd.read_csv(TRAIN)
df2 = pd.read_csv(TEST)
st.title('Rock-n-Code')
st.write(df1)
st.write(df2)
