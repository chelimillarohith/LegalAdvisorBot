# LegalAdvisorBot: Streamlit App for IPC Section Matching + Past Case Lookup

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from bs4 import BeautifulSoup

# Load IPC Dataset
ipc_df = pd.read_csv("ipc_sections.csv")
ipc_df['combined_text'] = ipc_df['Description'].fillna('') + " " + ipc_df['Offense'].fillna('')

def match_ipc_sections(user_input, df, top_n=3):
    corpus = df['combined_text'].tolist() + [user_input]
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(corpus)
    cosine_sim = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
    top_indices = cosine_sim.argsort()[-top_n:][::-1]
    return df.iloc[top_indices][['Section', 'Description', 'Offense', 'Punishment']]

def search_past_cases(section_number):
    url = f"https://indiankanoon.org/search/?formInput=section%20{section_number}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for result in soup.select(".result_title")[:5]:
        anchor = result.find("a")
        if anchor and 'href' in anchor.attrs:
            title = anchor.text.strip()
            link = "https://indiankanoon.org" + anchor['href']
            results.append({'title': title, 'link': link})

    return results


# Streamlit UI
st.set_page_config(page_title="LegalAdvisorBot", layout="wide")
st.title("📘 LegalAdvisorBot – IPC Section & Case Matcher")
st.markdown("Provide your case description below to get matching IPC sections and related case references.")

user_input = st.text_area("📝 Enter Case Description:", height=200)

if st.button("Analyze Case") and user_input.strip():
    with st.spinner("Analyzing case and fetching legal references..."):
        ipc_matches = match_ipc_sections(user_input, ipc_df)

        for _, row in ipc_matches.iterrows():
            st.subheader(f"🔖 Section {row['Section']}")
            st.markdown(f"**Offense:** {row['Offense']}")
            st.markdown(f"**Description:** {row['Description']}")
            st.markdown(f"**Punishment:** {row['Punishment']}")

            past_cases = search_past_cases(row['Section'].replace("IPC_", ""))
            if past_cases:
                st.markdown("**🔗 Related Past Cases:**")
                for case in past_cases:
                    st.markdown(f"- [{case['title']}]({case['link']})")
            else:
                st.markdown("No past cases found for this section.")

else:
    st.info("Enter a legal case description and click 'Analyze Case' to begin.")
