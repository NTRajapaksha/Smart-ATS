import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Generative AI API with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate a response


def get_gemini_response(input_prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    return response.text

# Function to extract text from PDF


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# Streamlit app
st.title("Smart ATS")
st.subheader("Optimize Your Resume for Success")

# Job Description input
jd = st.text_area("Paste the Job Description",
                  help="Enter the job description for the role you are applying for.")

# File uploader for the resume
uploaded_file = st.file_uploader(
    "Upload Your Resume", type="pdf", help="Please upload your resume in PDF format.")

# Experience level selection
experience_level = st.radio(
    "Select Your Experience Level",
    ('Undergraduate', 'Fresh Graduate', 'Experienced Candidate'),
    help="Choose your experience level to tailor the resume analysis."
)

# Button declarations
submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("How Can I Improve My Skills")
submit2 = st.button("Percentage Match")
submit4 = st.button("Fix the Resume")
submit5 = st.button("Generate a Sample Cover Letter")

# Prompt templates based on experience level
input_prompt1 = f"""
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
Job Description: {{jd}}
Resume: {{resume_text}}
Experience Level: {experience_level}
"""

input_prompt2 = f"""
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
Your task is to evaluate the resume against the provided job description according to the experience level. Provide the percentage of match if the resume matches
the job description. The output should include the percentage match, missing keywords, and final thoughts.
Job Description: {{jd}}
Resume: {{resume_text}}
Experience Level: {experience_level}
"""

input_prompt3 = f"""
You are an experienced career coach with expertise in software engineering, data science, and related fields. Your task is to evaluate the provided resume against the job description and suggest ways the candidate can improve their skills to better align with the role.
Job Description: {{jd}}
Resume: {{resume_text}}
Experience Level: {experience_level}
"""

input_prompt4 = f"""
You are a highly experienced professional in [specific field, e.g., software engineering, data science, etc.] with extensive knowledge in resume optimization and ATS (Applicant Tracking System) compatibility. Your task is to review the provided resume and rewrite it to reflect the level of expertise expected from someone with relevent experience or no experience(undergraduate) in this field. Ensure that the resume is fully optimized with the best practices in formatting, keyword usage, and content structure. The revised resume should highlight the candidate's skills, accomplishments, and qualifications in a way that makes it stand out in a competitive job market, ensuring maximum compatibility with ATS.
Job Description: {{jd}}
Resume: {{resume_text}}
Experience Level: {experience_level}
"""

input_prompt5 = f"""
You are an experienced Technical Hiring Manager. Your task is to review the provided resume in comparison with the job description and use your professional judgment to craft a compelling and tailored cover letter that effectively highlights the candidate's qualifications and aligns with the expectations of a seasoned professional in the field.
Job Description: {{jd}}
Resume: {{resume_text}}
Experience Level: {experience_level}
"""

# Handling button clicks
if submit1:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        input_prompt = input_prompt1.format(jd=jd, resume_text=resume_text)
        response = get_gemini_response(input_prompt)
        st.subheader("Evaluation Report")
        st.write(response)
    else:
        st.warning("Please upload your resume.")

elif submit2:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        input_prompt = input_prompt2.format(jd=jd, resume_text=resume_text)
        response = get_gemini_response(input_prompt)
        st.subheader("ATS Percentage Match")
        st.write(response)
    else:
        st.warning("Please upload your resume.")

elif submit3:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        input_prompt = input_prompt3.format(jd=jd, resume_text=resume_text)
        response = get_gemini_response(input_prompt)
        st.subheader("Skills Improvement Suggestions")
        st.write(response)
    else:
        st.warning("Please upload your resume.")

elif submit4:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        input_prompt = input_prompt4.format(jd=jd, resume_text=resume_text)
        response = get_gemini_response(input_prompt)
        st.subheader("Revised Resume")
        st.write(response)
    else:
        st.warning("Please upload your resume.")

elif submit5:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        input_prompt = input_prompt5.format(jd=jd, resume_text=resume_text)
        response = get_gemini_response(input_prompt)
        st.subheader("Generated Cover Letter")
        st.write(response)
    else:
        st.warning("Please upload your resume.")
