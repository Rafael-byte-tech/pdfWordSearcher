import json
from pdfParse import directory_search
from graphs import make_table, pie_chart, save
import tkinter
from tkinter import filedialog
from interface import message, end_message

def search_word():
    tkinter.Tk().withdraw()
    message('Selecione um arquivo .json contendo uma lista de palavras chave para sua pesquisa. Aperte Enter.')
    file_path = filedialog.askopenfilenames() # searches file in the os file explorer, returns a tuple containing the file´s path extension
    f = open(repr(file_path[0])[1:-1]) 
    j = json.load(f) # dictionary extracted from .json file
    keywords = [j[k] for k in j][0] # list of keywords extracted from the dictionary
    
    message('Selecione o diretório com os arquivos pdf.')
    folder_path = filedialog.askdirectory() # searches directory in the os file explorer
    path_extension = repr(folder_path)[1:-1] # directory´s path extension
    
    data = directory_search(path_extension, keywords)
    table = make_table(data, keywords)
    chart = pie_chart(data, keywords)
    
    message('Selecione uma pasta para salvar o arquivo (Images.pdf) com a tabela e o gráfico.')
    path_extension = repr(filedialog.askdirectory())[1:-1]
    save(table, path_extension) 
    save(chart, path_extension)
    end_message('completo', 'Processamento completo.')
search_word()   