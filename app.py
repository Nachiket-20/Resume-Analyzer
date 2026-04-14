import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get ATS score + suggestions")

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

    # Show file details
    st.write("Filename:", uploaded_file.name)
    st.write("File size:", uploaded_file.size, "bytes")