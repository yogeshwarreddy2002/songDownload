import streamlit as st
st.title("🎧⬇️Music Download")
cl,c2=st.columns(2)
with cl:
    st.title("🎬movie name")
    st.subheader("jersey")
    st.image("https://c.saavncdn.com/006/Jersey-Original-Background-Score--Telugu-2019-20190513155328-500x500.jpg",width=150)
    st.subheader("🚗F1")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQ2Nx_8NdsCMpxJWX4-HvMkGcfCUAe20INzWi5KzedTZR0gt_KLDhvpYRVZcuph23dHZUmaw&s=10",width=150)
with c2:
    st.title("🎵song name") 
    st.subheader(" Aarambhame Le")
    st.audio("Aarambhame Le.mp3")
    v=open("Aarambhame Le.mp3","rb")
    h=v.read()
    st.download_button(
              label="🎵Download audio",
              data=h, 
              file_name="Aarambhame Le.mp3",
              

     )
    st.subheader(" F1 Movie - Background Music")
    st.audio("F1 Movie - Background Music.mp3")
    v=open("F1 Movie - Background Music.mp3","rb")
    h=v.read()
    st.download_button(
                  label="🎵Download audio",
                  data=h, 
                  file_name="F1.mp3",
            )  

