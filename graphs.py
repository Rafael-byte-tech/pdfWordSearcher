import plotly.graph_objects as go
import plotly.express as px
import pathlib
import os

# Creates a plotly table using a dictionary and a list as argument
def make_table(data, keywords):
    header_values = list() # [header0, header1, header2, header3, ...]
    cells_values = list() # [[cell00, cell10, cell20], [cell01], [cell11], [cell21] ...]
    
    header_values.append("Termo")
    cells_values.append([keyword for keyword in keywords])
    
    for i in data:
        header_values.append(i)
        cells_values.append([j for j in data[i]])
    
    fig = go.Figure(
    data = [
        go.Table(
            columnorder = [i for i in range(len(data) + 1)],
            columnwidth = [1.8, 1],
            header = dict(
                values = header_values,
                line_color = 'darkgrey',
                fill_color = ['orange', 'mediumblue'],
                align = ['center'],
                font = dict(color = 'white', size = 15),
                height = 40),
            cells = dict(
                values = zero_to_apostrophe(cells_values),
                line_color = 'darkgrey',
                fill_color = ['cornflowerblue', 'beige'],
                align = ['center'],
                font = dict(color = 'black', size = 14),
                height = 30)
            )
        ]
    )
    fig.update_layout(width = 1950, height = 1900)
    #write_pdf(fig, 'relatório_tabela')
    #open_pdf('relatório_tabela')
    return (fig, 'tabela')

# Creates a pie chart using a dictionary and a list as argument
def pie_chart(data, keywords):
    values = list()
    for i in range(len(keywords)):
        values.append(sum([data[key][i] for key in data]))
    df = px.data.tips()
    fig = px.pie(df, values=values, names=keywords, title="Termos Procurados")
    fig.update_traces(textfont_size=15, marker=dict(line=dict(color='#000000', width=0.06)))
    #write_pdf(fig, 'relatório_gráfico')
    #open_pdf('relatório_gráfico')
    return (fig, 'gráfico')

# Converts the zeros in a list to an empty string
def zero_to_apostrophe(cells_values):
    for i in cells_values:
        for j in range (len(i)):
            if i[j] == 0:
                i[j] = ''
    return cells_values

def save(graph, path_extension):
    if not os.path.exists(r'{}\Relatório'.format(path_extension)):
        os.mkdir(r'{}\Relatório'.format(path_extension))
    graph[0].write_image(r'{}\Relatório\{}.pdf'.format(path_extension, graph[1])) # Writes pdf 
    return None
