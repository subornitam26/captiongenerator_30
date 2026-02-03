import streamlit as st
import google.generativeai as genai

genai.configure(api_key = "GOOGLE_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Social Media Caption Generator")

description = st.text_input("Product/Service description")
tone = st.selectbox("Choose a tone :",["Witty", "Professional"])

if tone and description:
        prompt = f"Write 3 social media captions under 30 words,tone:{tone}, about:{description}"
        
        with st.spinner("Generating captions with Gemini..."):
            response = model.generate_content(prompt)
            caption = response.text

        st.subheader("Generated captions:")
        st.markdown(caption)
