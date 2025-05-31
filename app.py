import streamlit as st
from model import load_resumes, rank_resumes

st.title("AI Resume Ranker for Fair Hiring")
st.markdown("Upload resumes and a job description to rank candidates.")

job_desc = st.text_area("Paste Job Description here")

resumes_folder = "resumes"

if st.button("Rank Resumes"):
    resumes, filenames = load_resumes(resumes_folder)
    if job_desc and resumes:
        results = rank_resumes(job_desc, resumes, filenames)
        st.subheader("Top Matching Resumes:")
        for i, (filename, score) in enumerate(results):
            st.write(f"**{i+1}. {filename}** — Match Score: {score:.2f}")
    else:
        st.warning("Please provide a job description and at least one resume.")
