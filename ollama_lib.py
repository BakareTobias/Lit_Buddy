import ollama

# Warm-up so later requests are faster
ollama.chat(
    model="llama3.2:3b-instruct-q4_0",#mistral 7B
    messages=[{"role": "system", "content": "You are ready to process citation strings."}]
)

SYSTEM_PROMPT = """
You are an academic citation parser.
Your only job is to read a given string and return exactly four fields:

1. <Exact title from the string>  
2. [Comma-separated list of authors only — remove any affiliations, degrees, or extra descriptions]  
3. <Exact journal name from the string>  
4. <Exact year of publishing from the string>

Rules:
- Output exactly 4 lines in the exact order above.
- Do not include labels like "Title" or "Year" in the output.
- If a field is missing, write "N/A".
- Fix obvious spelling and punctuation errors.
- For authors: keep only personal names in the order found, separated by commas.
- Do NOT include affiliations, job titles, institutions, degrees, or locations.


Example:
Input: June 2014 Design of a Smart Firefighting Robot M. Kumar, P. Singh, and R. Sharma
Output:
Design of a Smart Firefighting Robot
[M. Kumar, P. Singh, R. Sharma]
N/A
2014

Example (what NOT to do):
❌ Disaster in Nigeria: A Public Health Perspective [Joshua, Istifaanus Anekoson, M.] Department of Community Medicine...
This is wrong because it includes affiliations. The correct output should only list names.

END OF RULES
"""





def extract_title_and_authors(citation: str):
    """ Function to use llm to verify extracted string """
    messages = [
    {'role': 'system','content':SYSTEM_PROMPT}
    ]
    messages.append({'role':'user','content':citation})



    response = ollama.chat(
        model="llama3.2:3b-instruct-q4_0",
        messages=messages
    )
    reply = response['message']['content']
    print(reply)
    title, author, journal, year = reply.split('\n')


    doc_params = {}
    doc_params.update({'title':title,'author':author,'journal':journal,'year':year})
    
    return doc_params

# Example usage
#citation_text = "Smith, J., & Doe, A. . Deep Learning for Image Recognition.(2020)."
#result = extract_title_and_authors(citation_text)
#print(result)
