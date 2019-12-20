import requests
from bs4 import BeautifulSoup
import json
from .models import Process, Move
import datetime

#Const search url, used by prefix for process number
search_url = "https://www2.tjal.jus.br/cpopg/search.do?cbPesquisa=NUMPROC&dadosConsulta.tipoNuProcesso=UNIFICADO&dadosConsulta.valorConsultaNuUnificado="

#Creates the beautiful soup instance with the html response
def get_html_parsed(process_number):
    response = requests.get(search_url + process_number)
    return BeautifulSoup(response.content, "html.parser")

#Find the column with data, by the label column
def find_by_label(rows, labelText):
    for row in rows:
        label = row.find('td')
        label_splited = label.text.strip().split(':')
        if label_splited[0] == labelText:
            return (label.find_next_sibling('td').text.strip() if label_splited[1] == '' else label_splited[1])

#Crawler the process if already exisits update it
def crawler_process(process_number, id=None):
    
    soup = get_html_parsed(process_number)

    rows = soup.select("table.secaoFormBody tr")

    process = Process(
        id=id, #If is already crawled, has to update the object
        process_number=process_number,
        kind=find_by_label(rows, 'Classe'),
        area=find_by_label(rows, 'Área'),
        subject=find_by_label(rows, 'Assunto'),
        distribuition=find_by_label(rows, 'Distribuição'),
        judge=find_by_label(rows, 'Juiz'),
        action_value=find_by_label(rows, 'Valor da ação'),
    )

    process.save()

    crawler_moves(soup, process)

#Crawler the moves list and save them
def crawler_moves(soup, process):

    moves_rows = soup.select("tbody#tabelaTodasMovimentacoes tr")
    for row in moves_rows:
        colums = row.select('td')
        move = Move(
            date=datetime.datetime.strptime(colums[0].text.strip(), "%d/%m/%Y").date(), #1º column
            description=colums[2].text.strip(), #3º column (2º blank)
        )
        move.save()
        process.moves.add(move)