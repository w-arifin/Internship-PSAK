# import dari streamlit
import streamlit as st
from PIL import Image
# import dari google colab
import pandas as pd
import os
from datetime import datetime
import random
import matplotlib.pyplot as plt
import plotly.express as px
import datetime
import numpy as np
import plotly.graph_objects as go
import re
import itertools
import collections
import nltk
from nltk.corpus import stopwords
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import networkx as nx
from nltk import bigrams
from wordcloud import WordCloud
from textblob import TextBlob


st.set_page_config(
        page_title="Hello",
        page_icon="👋",)

st.title("Prototype Dashboard PSAK")
st.write("Data Preparation of PSAK || TETRIS BATCH 4 Internship in Xeratic - Group 19")

df = pd.read_excel('https://github.com/w-arifin/Internship-PSAK/raw/main/Mockup%20Group%2019%20Xeratic.xlsx')
df = df.rename(columns={'No PSAK' : 'no_psak',
                               'Nama PSAK' : 'nama_psak',
                               'Tgl Terbit' : 'tgl_terbit',
                               'Tgl Disahkan' : 'tgl_sah',
                               'Konten' : 'konten',
                               'File Konten' : 'file_konten',
                               'Kategori' : 'kategori',
                               'Jumlah Sub Konten' : 'jumlah_sub_konten'})

option_list = df['no_psak'].unique()

df['tgl_terbit'] = pd.to_datetime(df['tgl_terbit'])
df['tgl_sah'] = pd.to_datetime(df['tgl_sah'])

# Mengubah format tanggal menjadi '15 Desember 2009'
def format_date(date):
    months = {
        1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April',
        5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus',
        9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
    }
    return f"{date.day} {months[date.month]} {date.year}"

df['tgl_terbit'] = df['tgl_terbit'].apply(format_date)
df['tgl_sah'] = df['tgl_sah'].apply(format_date)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
  option = st.selectbox(
    "Pilih PSAK yang ingin dilihat:",
    (option_list))

selected_psak_data = df[df['no_psak'] == option]

st.subheader(f"{option} - {selected_psak_data['nama_psak'].values[0]}")
st.write(f"**Kategori** : *{selected_psak_data['kategori'].values[0]}*")

col1, col2 = st.columns(2)

with col1:
   st.write("Tanggal Terbit:", selected_psak_data['tgl_terbit'].values[0])

with col2:
   st.write(f"Tanggal Disahkan: {selected_psak_data['tgl_sah'].values[0]}")

container = st.container(border=True)
container.write(selected_psak_data['konten'].values[0])

with st.expander("File konten:"):
    st.write(f"{selected_psak_data['file_konten'].values[0]}")
       
st.write(f"Jumlah Sub Konten: {selected_psak_data['jumlah_sub_konten'].values[0]}")
