import streamlit as st
from helper_lib import extract_text_from_pdf,re_formatting,concatenate_stop_word_endings,extract_key_string,form_citations,find_and_sort_related_papers
from ollama_lib import extract_title_and_authors

import spacy
nlp = spacy.load("en_core_web_md")

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
        with st.status("Searching similar papers...", expanded=False ) as status:
            related_papers = find_and_sort_related_papers(title)

            if related_papers != None:
                status.update(label="Search successfull!", state="complete", expanded=False)

            else:
                status.update(label="Search failed", state="error", expanded=False)
                
        if related_papers != None:
            st.write("Related articles:")
            count = 1
            for i,key in enumerate(related_papers):
                #Title
                st.write(f'[{count}] **{related_papers[key][0]}**')
                if related_papers[key][-1] > 0.65:
                    st.badge("Strongly related",  color="green")
                elif 0.4 <= related_papers[key][-1] <= 0.65:
                    st.badge("Maybe related", color="grey")
                elif 0.4 > related_papers[key][-1]:
                    st.badge("Weak/No relation", color="orange")
                st.write(f'**Abstract**: {related_papers[key][1]}')
                st.write(f'**DOI**: {related_papers[key][2]}')
                st.link_button("View paper", f"{related_papers[key][3]}")
                st.divider()
                count +=1
            