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


st.title("Lit-Buddy")
st.subheader("Smart Literature Review Assistant")
st.write("""
            Lit-Buddy is a tool that helps you with writing your literature reviews
            by helping you generate citations for your research papers.
            \nTip: Upload well-formatted PDFs (journal versions work best)
            \nTry it out below
        """)

pdf = st.file_uploader("Upload your paper here",type=['pdf'])
if pdf:
    with st.status("Processing file...", expanded=True ) as status:
        st.write("Parsing file...")
        extracted_text = extract_text_from_pdf(pdf)
        st.write("Applying regex...")
        post_format = re_formatting(extracted_text)
        doc = nlp(post_format)
        final_post_format = concatenate_stop_word_endings(doc)
        doc = nlp(final_post_format)
        st.write("Extracting key info...")
        key_string = extract_key_string(doc)

       
        if key_string != '':
            doc_params = extract_title_and_authors(key_string)
            status.update(label="Processing complete!", state="complete", expanded=False)

        else:
            status.update(label="Processing failed", state="error", expanded=False)
            st.write(f'We are currently unable to generate title for this document. Apologies')
    if key_string != '':
        title = doc_params['title']
        authors = doc_params['author']
        year    = doc_params['year']
        journal = doc_params['journal']

        st.write(f'**Title:**   {title}')
        st.write(f'**Authors:** {authors}')
        st.write(f'**Journal:** {journal}')
        st.write(f'**Year:**    {year}')

        APA,IEEE = form_citations(doc_params)
        if APA != None:
            col1, col2 = st.columns(2)
            with col1: 
                st.write("**APA Citation**")
                st.write(f'**In-text:**     {APA["in_text"]}')
                st.write(f'**References:**  {APA["references"]}')

            with col2:
                st.write("**IEEE Citation**")
                st.write(f'**In-text:**     {IEEE["in_text"]}')
                st.write(f'**References:**  {IEEE["references"]}')
        else:
            st.write("Unable to generate citations with incomplete data")

        related_papers = find_related_papers(title)
        if related_papers != None:
            st.write("Related articles:")
            for i,key in enumerate(related_papers):
                if '_title' in str(key):
                    st.write(f'[{int(i/2)}] {related_papers[key]}')
                else:
                    st.link_button("View paper", f"{related_papers[key]}")

            

    #except ValueError as e :
    #    st.write(e)
    #    st.write("Your document is too long for SpaCy's processor. Please try something else")


    #print(extracted_text)
    #print(final_post_format)
    
