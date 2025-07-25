https://legaladvisorbot-ypaagwc8dkhuvf8n5uc6mr.streamlit.app/

Title: LegalAdvisorBot – AI-Powered Legal Case Analyzer
The title "LegalAdvisorBot" effectively reflects the primary objective of the project, which is to provide AI-powered assistance in understanding legal scenarios and mapping them to relevant Indian Penal Code (IPC) sections. In a country where access to legal counsel is limited for many due to cost, complexity, or lack of awareness, this application bridges the gap by using Natural Language Processing (NLP) to provide preliminary legal guidance. Users can describe their problem in simple language, and the bot will return relevant IPC sections, offenses, punishments, and even similar past case links from Indian Kanoon. The name conveys both the legal focus and the AI-driven conversational nature of the solution.
________________________________________
Aim and Scope of the Project
Objective:
1.	To build an AI-powered chatbot that interprets user-input legal situations and returns relevant IPC sections.
2.	To enhance legal awareness and accessibility by simplifying complex legal information.
3.	To fetch and display real past Indian case references using keywords or IPC sections.
4.	To provide a foundational legal advisory tool for education, awareness, and early-stage dispute understanding.
Scope:
1.	Use Streamlit to build an interactive web application interface.
2.	Use NLP (TF-IDF + cosine similarity) to match input with IPC descriptions.
3.	Integrate Indian Kanoon web scraping for related past case references.
4.	Extendable in future for regional languages, voice input, or document-based extraction.
5.	Deploy using platforms like Streamlit Cloud, and host datasets securely.
________________________________________
Basic Concepts Related to the Project
•	NLP Techniques: TF-IDF Vectorizer and Cosine Similarity are used to compare user input with legal descriptions.
•	IPC Dataset: CSV file containing IPC section numbers, offense titles, descriptions, and punishments.
•	Streamlit: A Python framework to build simple and interactive web apps quickly.
•	BeautifulSoup & Requests: Used for scraping case data from Indian Kanoon based on IPC sections.
•	Data Matching: User's description is matched with legal text to suggest top IPCs.
•	Past Case Integration: Indian Kanoon is searched for relevant case judgments, and top links are presented to the user.
________________________________________
Analysis and Explanation of the Identified Problem
The Problem:
Legal guidance in India is often expensive, delayed, or inaccessible to the common man. Many people are unaware of their legal rights or the relevant laws that apply to their situations. Minor legal issues go unreported or mishandled due to lack of understanding. There's also a need for tools that bridge legal information and real-world case references in a simple, conversational format.
Challenges Identified:
•	Lack of accessible and understandable legal information.
•	Legal jargon is too complex for the common public.
•	No platform to match natural language to IPC sections.
•	Public cannot easily access or understand past legal judgments.
Proposed Solution:
•	An NLP-based chatbot that accepts user queries in plain English.
•	Matches case details with IPC sections and gives structured results.
•	Pulls similar Indian Kanoon case links for user reference.
•	Friendly and quick frontend built using Streamlit.
