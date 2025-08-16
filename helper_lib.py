#EXTRACT AND PREPROCESS PDF
import random
import time
import PyPDF2
import re
import serpapi
import spacy
from misc import get_project_settings

nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(pdf_file):

    reader = PyPDF2.PdfReader(pdf_file, strict=False)
    pdf_text = []

    for page in reader.pages:
        content  = str(page.extract_text())
        #print(content)
        pdf_text.append(content)

    return pdf_text
    
def re_formatting(extracted_text):
    #list, each page is an item in list
    post_format = []

    for string in (extracted_text):
        #pai n-\nful -> painful
        string = re.sub(r'\s*([a-z])\s*-\n\s*',r'\1',string)
        #complex \nsurgical procedures -> complex surgical procedures
        string = re.sub(r'(\w)\s*\n([a-z])',r'\1 \2',string)
        #Smaller incisions \n\uf0b7 Less pain -> Smaller incisions, Less pain
        string = re.sub(r'\n\uf0b7',r',',string)
        #cust sentence delimiter
        string = re.sub(r'\s+\n\s+',r'~',string)
        string = re.sub(r'\.\s*\n\s*',r'~',string )
        string = re.sub(r'\s*\n\s*([A-Z]*\d*)',r'~\1',string)
        string = re.sub(r'·','~',string)

        #string = string.replace('~','\u200B')
        #miniature tools, \ndoctors
        string = re.sub(r'\s*\n([a-z]*)\d*',r'\1 ',string)
        #\xa0
        string =re.sub(r'\xa0*\x00*','',string)
        #\n\uf344\uf5ef\uf472\uf5b3\uf618
        string = re.sub(r'\uf344*\uf5ef*\uf472*\uf5b3*\uf618*','',string)
        #
        string = string.replace('','')
        #emojis and such
        """ emoji_patterns = re.compile(
        "["
        u"\U0001F600-\U0001F64F" # emoticons
        u"\U0001F300-\U0001F5FF" # symbols & pictographs
        u"\U0001F680-\U0001F6FF" # transport & map symbols
        u"\U0001F1E0-\U0001F1FF" # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", 
        flags=re.UNICODE
        )
    
        string =  emoji_patterns.sub(r'', string)
 """
        
        post_format.append(string)

    final_post_format = ''
    for string in post_format:
        final_post_format += string

    return (final_post_format)


def concatenate_stop_word_endings(doc):
    sentences = list(doc.sents)
    merged_sentences = []
    i = 0
    
    while i < len(sentences):
        current_sent = sentences[i]
        current_text = current_sent.text.strip()
        
        # Check if current sentence ends with a stop word
        last_token = None
        for token in reversed(list(current_sent)):
            if token.is_alpha:  # Get last alphabetic token
                last_token = token
                break
        
        # If ends with stop word, concatenate with next sentence
        if (last_token and last_token.is_stop and 
            i + 1 < len(sentences)):
            
            next_sent = sentences[i + 1]
            merged_text = current_text + " " + next_sent.text.strip()
            merged_sentences.append(merged_text)
            i += 2  # Skip the next sentence since we merged it
        else:
            merged_sentences.append(current_text)
            i += 1
    
    final_post_format = ''
    for string in merged_sentences:
        final_post_format += string

    return (final_post_format)

#EXTRACT TITLE
def extract_title(final_post_format):

    #FINDING TITLE SENTENCE
    #title will typically be in the first 5 lines of the doc
    #title will typically have no names/dates/percentages/ in it
    #title will typically omit certain words associated with journals
    #title will typically be under 20 words
    #title will not have initials in it

    sents = list(final_post_format.sents)
    sub_sents = sents[0:4]

    #flagged_words = ['journal','conference','doi','ieee','issn','vol','department','university','article','manuscript','faculty','license','author','authors','mr']
    #flagged_ent_types = ['PERCENT','DATE',]

    
    flagged_words = ['introduction','abstract']
 

    """ for sent in sub_sents_copy:
        #print(sent[3])
        
        for token in sent:
            word = token.text.lower().strip()
            #print(f'{repr(token.text)}->{token.ent_type_}->{spacy.explain(token.ent_type_)}')
             if (token.ent_type_ in flagged_ent_types) or (word in flagged_words) or (token.like_url) or (token.like_email) or (len(sent)>20) or bool(re.search(r'[A-Z]\.\s*[A-Z]*',token.text)): 
            if word in flagged_words:
                #print(len(sent))
                sub_sents.remove(sent)
                break """

    #print(sub_sents_copy)

    #title = ' '.join(str(sent) for sent in sub_sents_copy).replace('~','')
    return #(title)

def extract_key_string(final_post_format):

    #FINDING TITLE SENTENCE
    #title will typically be in the first 5 lines of the doc
    #title will typically have no names/dates/percentages/ in it
    #title will typically omit certain words associated with journals
    #title will typically be under 20 words
    #title will not have initials in it

    sents = list(final_post_format.sents)
    sub_sents = sents[0:4]

    
    # flagged_words = ['journal','conference','doi','ieee','issn','vol','department','university','article','manuscript','faculty','license','author','authors','mr']
    flagged_ent_types = ['PERCENT','DATE',]
    flagged_words =     ['abstract',]
    sub_sents_copy = sents[0:4]
    

    
 
    for sent in sub_sents_copy:
        for token in sent:
            word = token.text.lower().strip()
            #print(f'{repr(token.text)}->{token.ent_type_}->{spacy.explain(token.ent_type_)}')
            if  (word in flagged_words)  or  (len(sent)>40): 
                #print(len(sent),sent[0])
                sub_sents.remove(sent)
                break

    #print(sub_sents[1])

    key_string = ' '.join(str(sent) for sent in sub_sents)
    return (key_string)

def form_citations(doc_params):
    title = doc_params['title']
    author_str = doc_params['author']
    year    = doc_params['year']
    journal = doc_params['journal']

    for key in doc_params:
        if doc_params[key] in ('N/A', '[N/A]', ['N/A']):
            return None,None
    author_str = list(author_str)
    author_str.remove('[')
    author_str.remove(']')
    authors = ''.join(x for x in author_str)
    #Pull out first name
    for i, letter in  enumerate(author_str):
        if letter == ' ' or letter == ',':
            first_name = author_str[:i]
            first_name = ''.join(letter for letter in first_name)
            break

    #print(first_name)

    #APA CITATIONS
    in_text = f'{first_name}({year})'
    references = f'{authors}. ({year}). {title}. {journal}'

    APA = {}
    APA.update({'in_text':in_text,'references':references})

    in_text = f'[x]'
    references = f'[x] {authors}. ({year}). {title}. {journal}'

    IEEE = {}
    IEEE.update({'in_text':in_text,'references':references})
    return APA, IEEE

def find_related_papers(title):
    if title in ('N/A', '[N/A]', ['N/A']):
        return None
    RESULTS = {}
    #initialize serp api scraper
    project_settings = get_project_settings("serp_key.json")
    api_key = project_settings['API_KEY']
    client = serpapi.Client(api_key=api_key)

    doc = nlp(title)
    noun_chunks = list(doc.noun_chunks)
    for chunk in noun_chunks:
        result = client.search(
        q = f'{chunk}',
        engine = "google_scholar",
        location = "Lagos, Nigeria",
        hl = "en",
        num = "4"
        )


        for i,item in enumerate(result['organic_results']):
            RESULTS.update({f'{chunk}_{i}_title':item["title"],f'{chunk}_{i}_link':item['link']})

        
    
    return RESULTS

#find_related_papers('Firefighting Robot')

""" project_settings = get_project_settings("serp_key.json")

api_key = project_settings['API_KEY']
client = serpapi.Client(api_key=api_key)

result = client.search(
q = f'coffee',
engine = "google_scholar",
location = "Lagos, Nigeria",
hl = "en",
num = "3"
)

#print(result['organic_results'])

for item in result['organic_results']:
    print(item["title"])
    print(item['link'])
    print(item['snippet'])
    print('------------------') 

results = find_related_papers('Internet of Things Autonomous Firefighting Robot')
print(results)"""