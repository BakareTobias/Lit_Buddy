import streamlit as st
from helper_lib import extract_text_from_pdf,re_formatting,concatenate_stop_word_endings,extract_key_string,form_citations,find_related_papers
from streamlit_helper import display_with_copy
from ollama_lib import extract_title_and_authors

import spacy
nlp = spacy.load("en_core_web_lg")

config = {"punct_chars": ['~'],'overwrite':True}
nlp.add_pipe("sentencizer",config=config)

# Construction from class
from spacy.pipeline import Sentencizer
sentencizer = Sentencizer()


st.title("Welcome to Lit-Buddy")
st.write("""
            Lit-Buddy is a tool that helps you with writing your literature reviews
            by helping you generate citations for your research papers.
            \nUse on research articles in PDF form for best results
            \nTry it out below
        """)

pdf = st.file_uploader("Upload your paper here",type=['pdf'])
if pdf:
    st.write("Processing file...")
    extracted_text = extract_text_from_pdf(pdf)
    st.write("Formatting...")
    post_format = re_formatting(extracted_text)
    #try:
    doc = nlp(post_format)
    final_post_format = concatenate_stop_word_endings(doc)
    doc = nlp(final_post_format)
    st.write("Extracting title...")
    key_string = extract_key_string(doc)
    if key_string != '':
        #print(key_string)
        doc_params = extract_title_and_authors(key_string)
        #print(doc_params)
        title = doc_params['title']
        authors = doc_params['author']
        year    = doc_params['year']
        journal = doc_params['journal']
        st.write(f'Your title is: {title}')
        st.write(f'Published by {authors} in the year {year} in the journal {journal}')

        APA,IEEE = form_citations(doc_params)
        if APA != None:
            col1, col2 = st.columns(2)
            with col1: 
                st.write("**APA Citation**")
                st.write(f'In-text -> {APA["in_text"]}')
                st.write(f'References -> {APA["references"]}')

            with col2:
                st.write("**IEEE Citation**")
                st.write(f'In-text -> {IEEE["in_text"]}')
                st.write(f'References -> {IEEE["references"]}')
        else:
            st.write("Unable to generate citations with incomplete data")

        related_papers = find_related_papers(title)
        if related_papers != None:
            st.write("Possibly Related articles:")
            for key in related_papers:
                st.write(related_papers[key])

    else:
        st.write(f'We are currently unable to generate title for this document. Apologies')

    #except ValueError as e :
    #    st.write(e)
    #    st.write("Your document is too long for SpaCy's processor. Please try something else")


    #print(extracted_text)
    #print(final_post_format)
    
