import ollama

# Warm-up so later requests are faster
ollama.chat(
    model="llama3.2:3b-instruct-q4_0",
    messages=[{"role": "system", "content": "You are ready to process citation strings."}]
)

SYSTEM_PROMPT = """"
You are an academic citation parser.
Your only job is to read a given string and return:
<exact title from the string> ~ [comma-separated list of authors] ~ <exact journal from the string> ~ <exact year of publishing from the string>

Rules:
- Do not add extra words, commentary, or formatting.
- Do not guess missing data; if unknown, return \"N/A\" for each missing field.
- Fix any spelling and punctuation from the input.
- Output exactly in the format: <Title> ~ [Authors] ~ <Journal> ~ <Year>

Input: IOP Conference Series: Materials Science and Engineering PAPER • OPEN ACCESS Obstacle detection using ultrasonic sensor for a mobile robot To cite this article: Joseph Azeta et al 2019 IOP Conf. Ser.: Mater. Sci. Eng. 707 012012
Output: Obstacle detection using ultrasonic sensor for a mobile robot ~ [Joseph Azeta, et al] ~ IOP Conf. Ser.: Mater. Sci. Eng. ~ 2019

Input:  June 2014 Design of a Smart Firefighting Robot M. Kumar, P. Singh, and R. Sharma
Output: Design of a Smart Firefighting Robot ~ [M. Kumar, P. Singh, R. Sharma] ~ N/A ~ 2014

Input: IEEE Transactions on Robotics, Vol. 28, No. 5, Autonomous Navigation in Unknown Environments John Smith and Jane Doe
Output: Autonomous Navigation in Unknown Environments ~ [John Smith, Jane Doe] ~ IEEE Transactions on Robotics ~ N/A

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
    #print(reply)
    title, author, journal, year = reply.split('~')


    doc_params = {}
    doc_params.update({'title':title,'author':author,'journal':journal,'year':year})
    
    return doc_params

# Example usage
#citation_text = "Smith, J., & Doe, A. . Deep Learning for Image Recognition.(2020)."
#result = extract_title_and_authors(citation_text)
#print(result)
