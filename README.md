# Lit Buddy
A tool for extracting and formatting academic citations from unstructured PDFs using PDF processing libraries, regex, Natural Language Processing via spacy and Large Language Models. Hosted via streamlit to provide an easy to interact with GUI

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

## Features
- Extracts titles, authors, journal, and year from research papers in PDF form
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

## Results

![SharedScreenshot](https://github.com/user-attachments/assets/e0b77a6f-1200-420a-ac60-5c4405c11ede)

<img width="1917" height="996" alt="image" src="https://github.com/user-attachments/assets/292dbf7a-003a-4c17-b555-e57d6405de5e" />

<img width="1914" height="1001" alt="image" src="https://github.com/user-attachments/assets/724f52b9-e1b5-40b2-8f37-7091500b20e0" />

### Extraction of Title and other Key details
Pipeline can determine title of a PDF submitted with a ~60% accuracy, but proves inconsistent across wide variety of PDF formats.
In testing, llms have been optimized for consistent, accurate output via:
1. prompts that include how to handle examples and possible edge cases.
2. Temperature parameter being set to 0

Further optimization solutions, or use of a more powerful language model than the currently used 'mistral:7b' should improve accuracy.

### Sourcing Related Articles
The obtained title is split into noun chunks using spacy. A search query is then processed for each noun chunk using SerpAPI. Titles and links are provided for further research

