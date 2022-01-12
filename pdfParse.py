import pdfplumber
from nltk import word_tokenize
from nltk.corpus import stopwords
from os import listdir
import os.path
from alive_progress import alive_bar
from time import sleep

# Extracts text from pdf 
def get_text(path):
    file = pdfplumber.open(path)
    text = str()
    for page in file.pages:
        text += page.extract_text(x_tolerance=2, y_tolerance=2)
    return text 

# Returns list containing tokenized words from a text 
def tokenize(text):
    tokenizer = word_tokenize(text, language='english',preserve_line=False)
    stop_words = stopwords.words('english')                                           
    tokens = [w.upper() for w in tokenizer if not w.lower() in stop_words and (w.isalpha() or '-' in w[:-1])]
    return tokens # [token1, token2, token3, ...]

# Returns a dictionary using a token as a key and its frequency as a value
def find_keywords(tokens, keywords):
    found = dict() # {word : freq}
    matches = [t for t in tokens if t in [k.upper() for k in keywords]] # [keywordA, keywordB, ...]
    for match in matches:
        if match in found:
            found[match] += 1
        else:
            found[match] = 1
    return found # {word : freq}

# Returns a dictinary containing the keywords´ frequencies in each pdf
def directory_search(path_extension, keywords):
    rawPath_extension = repr(path_extension)[1:-1]
    data = dict() # {pdf1 : [freq1, freq2, freq3, ...], pdf2 : [freq1, freq2, freq3, ...], ...}
    pdf_frequencies = list() # [pdfN, freq1, freq2, freq3, ...]
    pdf_name = str()
    i = int(0)
    with alive_bar(len(listdir(rawPath_extension))) as bar: # just a progress bar
        
        for path in listdir(rawPath_extension):
            full_path = os.path.join(rawPath_extension, path)
            if os.path.isfile(full_path) and os.path.splitext(path)[1].lower() == ".pdf":            
                text = get_text(full_path)
                found = find_keywords(tokenize(text), keywords) # {word : freq}
                pdf_name = "pdf{}".format(i + 1)
                i += 1
                for keyword in keywords:
                    if keyword.upper() in found:
                        pdf_frequencies.append(found[keyword.upper()])
                    else:
                        pdf_frequencies.append(0)
                data[pdf_name] = pdf_frequencies
                pdf_frequencies = []
                
            bar()
            sleep(0.03)
    return data  # {pdf1 : [freq1, freq2, freq3, ...], pdf2 : [freq1, freq2, freq3, ...], ...}