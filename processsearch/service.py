import requests
from bs4 import BeautifulSoup
import json
from .models import Process, Move
import datetime

search_url = "https://www2.tjal.jus.br/cpopg/search.do?cbPesquisa=NUMPROC&dadosConsulta.tipoNuProcesso=UNIFICADO&dadosConsulta.valorConsultaNuUnificado="

def get_html_parsed(process_number):
    response = requests.get(search_url + process_number)
    return BeautifulSoup(response.content)

def find_by_label(soup, labelText):
    rows = soup.select("table.secaoFormBody tr")
    for row in rows:
        label_column = row.find('td')
        if label_column.text.strip() == labelText:
            return label_column.find_next_sibling('td').text.strip()

def crawler_process(process_number, id=None):
    
    soup = get_html_parsed(process_number)


    process = Process(
        id=id, #If is already crawled, has to update the object
        process=find_by_label(soup, 'Processo:'),
        classe=find_by_label(soup, 'Classe:'),
        subject=find_by_label(soup, 'Assunto:'),
        distribuition=find_by_label(soup, 'Distribuição:'),
        control=find_by_label(soup, 'Controle:'),
        judge=find_by_label(soup, 'Juiz:'),
        action_value=find_by_label(soup, 'Valor da ação:'),
    )

    process.save()

    crawler_moves(soup, process)

def crawler_moves(soup, process):

    moves_rows = soup.select("tbody#tabelaTodasMovimentacoes tr")
    for row in moves_rows:
        colums = row.select('td')
        move = Move(
            date=datetime.datetime.strptime(colums[0].text.strip(), "%d/%m/%Y").date(), #1º coluna
            description=colums[2].text.strip(), #3º coluna (2º em branco)
        )
        move.save()
        process.moves.add(move)