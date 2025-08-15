# Lit Buddy
A tool for extracting and formatting academic citations from unstructured PDFs using PDF processing libraries, regex, Natural Language Processing via spacy and Large Language Models. Hosted via streamlit to provide an easy to interact with GUI

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Results](#results)

## Features 
- Extracts title, authors, journal, and year from research papers in PDF form
- Supports APA & IEEE citation formats
- Cleans author lists and removes affiliations automatically
- Works with multiple LLM backends (LLaMA, Mistral, GPT)
- Uses NLP and SerpAPI to provide links that may be related to your paper

## Installation
```bash
git clone https://github.com/BakareTobias/Lit_buddy.git
cd Lit_buddy
pip install -r requirements.txt
```
## Usage
Within the Lit_buddy directory, run the following command in your terminal: ```streamlit run main.py``` and click the link.
Follow the instructions provided on the webpage.

## Examples


<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/292dbf7a-003a-4c17-b555-e57d6405de5e" />

![SharedScreenshot](https://github.com/user-attachments/assets/311da0f8-ff63-46ef-959d-36394ca71cde)


## Results
### Extraction of Title and other Key details
Pipeline parses a pdf into readable text using PyPDF2, then cleans the ouptut using Regular Expression. Spacy is then used to extract the sentences most likely to contain the key string*. An
llm is used to extract the title, author, journal, and year of publishing from the key string.
The parsing and regex work well for formatting 95% of PDF formats tested. 
In spacy, a custom sentence delimiter is used, but there are situations in which spacy does not acknowledge it. The llm determines the title of a PDF submitted with a ~60% accuracy, but proves inconsistent across wide variety of PDF formats when extracting the other data points.
In testing,  the llms used for extracting the key info have been optimized for consistent, accurate output by:
1. using prompts that include how to handle examples and possible edge cases.
2. setting the emperature parameter being set to 0 to eliminate randomness in model output

Further optimization solutions, or use of a more powerful language model than the currently used 'mistral:7b' should improve accuracy.

* *key string is a string obtained from the PDF, that has a very high probability of containing the title, author, journal, and year of publishing.*
### Sourcing Related Articles
The obtained title is split into noun chunks using spacy. A search query is then processed for each noun chunk using SerpAPI. Titles and links are provided for further research

