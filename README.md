# Lit Buddy
A tool for extracting and formatting academic citations from unstructured PDFs using PDF processing libraries, regex, Natural Language Processing via spacy and Large Language Models. Hosted via streamlit to provide an easy to interact with GUI

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [ScholarSift](#scholarsift)
- [Examples](#examples)
- [Results](#results)

## Features 
- Extracts title, authors, journal, and year of publication from research papers in PDF form
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
#### Downloading the LLM
Use this link to download the exe file and then run it - https://ollama.com/download 
More details here - https://medium.com/@sridevi17j/step-by-step-guide-setting-up-and-running-ollama-in-windows-macos-linux-a00f21164bf3


## Usage
Within the Lit_buddy directory, run the following command in your terminal: ```streamlit run Lit_Buddy.py``` and click the link.
Follow the instructions provided on the webpage.

## Examples

### Landing page/file upload

### Example results

### ScholarSift




## Results
### Extraction of Title and other Key details
1. Pipeline parses a pdf into readable text using PyPDF2,
2. then cleans the ouptut using Regular Expression.
3. Spacy is then used to extract the sentences most likely to contain the key string*.
4. An LLM is used to extract the title, author, journal, and year of publishing from the key string.

<u> Notes </u>
* The parsing and regex work well for formatting 95% of PDF formats tested. 
* In spacy, a custom sentence delimiter is used, but there are situations in which spacy does not acknowledge it. The llm determines the title of a PDF submitted with a ~60% accuracy, but proves inconsistent across wide variety of PDF formats when extracting the other data points.
* In testing,  the llms used for extracting the key info have been optimized for consistent, accurate output by:
  * using prompts that include examples and how to handle possible edge cases.
  * setting the temperature parameter to 0 to eliminate randomness in model output

### Abstract Ranking (ScholarSift)
* The pipeline splits a given title into noun chunks
* For each noun chunk it runs a query of a SpringerNature API for meta data of articles and their abstracts
* For each returned abstract
  * The keyphrases are extracted using keyBERT
  * The abstracts are scored according to their keyphrases aas follows:
    * keyphrases that appear in the topic are given a +1
    * keyphrases are also scored according to their semantic similarity to the topic
    * Scores from both categories are aggregated and normalized to prevent bias towards abstracts with more keyphrases
* The articles are rearranged according to their abstract score
* Scores higher than 0.64 are labeled as 'strongly related', 0.64-0.4 as 'maybe related', below 0.4 are labeled 'weak/no relation'
  

Further optimization solutions, or use of a more powerful language model than the currently used 'mistral:7b' should improve accuracy.

*key string is a string obtained from the PDF using regex and SpaCy, that has a very high probability of containing the title, author, journal, and year of publishing.
### Sourcing Related Articles
The obtained title is split into noun chunks using spacy. A search query is then processed for each noun chunk using SerpAPI. Titles and links are provided for further research

