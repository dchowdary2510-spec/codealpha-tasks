import streamlit as st
import google.generativeai as genai
import json
import os

from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- LOAD ENV ---------------- #

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Smart FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- LOAD FAQ ---------------- #

with open("faq.json", "r", encoding="utf-8") as file:
    faq_data = json.load(file)

faq_questions = list(faq_data.keys())

# ---------------- CSS ---------------- #

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.title("🤖 Smart FAQ Chatbot")
st.caption("FAQ Matching + Gemini AI")

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.header("📚 FAQ Questions")

    for q in faq_questions:
        st.write("•", q)

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- CHAT HISTORY ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- USER INPUT ---------------- #

prompt = st.chat_input("Ask a question...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # NLP PREPROCESSING USING TF-IDF

            all_text = faq_questions + [prompt]

            vectorizer = TfidfVectorizer()

            vectors = vectorizer.fit_transform(all_text)

            similarity_scores = cosine_similarity(
                vectors[-1],
                vectors[:-1]
            )

            best_match_index = similarity_scores.argmax()

            best_score = similarity_scores[0][best_match_index]

            # FAQ MATCH

            if best_score >= 0.4:

                matched_question = faq_questions[best_match_index]

                answer = (
                    f"📚 **FAQ Answer**\n\n"
                    f"{faq_data[matched_question]}"
                )

            # GEMINI FALLBACK

            else:

                response = model.generate_content(
                    f"""
                    You are a friendly AI assistant.

                    Rules:
                    - Give concise answers.
                    - Maximum 4 lines.
                    - Avoid unnecessary details.
                    - Be clear and simple.
                    - Give detailed answers only if requested.

                    Question:
                    {prompt}
                    """
                )

                answer = response.text

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )