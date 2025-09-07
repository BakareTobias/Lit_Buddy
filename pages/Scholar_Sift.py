import streamlit as st
from helper_lib import find_and_sort_related_papers

st.title("ScholarSift")
st.subheader("Helping you research better")
st.write("""
            ScholarSift can help you find and sort related research papers
            by their similarity to your abstract/topic.
            \nTip: Upload an abstract or a research topic 
            \nTry it out below
        """)

with st.form("Topic/Abstract"):
    user_input = st.text_area("Enter your topic/abstract:")
    submitted = st.form_submit_button("Submit")
    
    if submitted and user_input:
        st.success(f"Submitted!")
        with st.status("Searching similar papers...", expanded=False ) as status:
            related_papers = find_and_sort_related_papers(user_input)

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