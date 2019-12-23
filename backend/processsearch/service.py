import requests
from bs4 import BeautifulSoup, NavigableString
import json
from .models import Process, Move, RelatedPart, RelatedPeople
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
            return (label.find_next_sibling('td').text.strip() if label_splited[1].strip() == '' else label_splited[1].strip())

#Crawler the process
def crawler_process(process_number):
    
    soup = get_html_parsed(process_number)

    rows = soup.select("table.secaoFormBody tr")

    process = Process(
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

    crawler_related_parts(soup, process)


#Crawler the moves list and save them
def crawler_moves(soup, process):

    rows = soup.select("tbody#tabelaTodasMovimentacoes tr")
    for row in rows:
        colums = row.select('td')
        move = Move(
            date=datetime.datetime.strptime(colums[0].text.strip(), "%d/%m/%Y").date(), #1º column
            description=colums[2].text.strip(), #3º column (2º blank)
            process=process
        )
        move.save()

#Crawler the related parts and save them
def crawler_related_parts(soup, process):

    rows = soup.select("table#tablePartesPrincipais tr")
    for row in rows:
        columns = row.select('td')

        related_part = RelatedPart(
            kind=columns[0].text.strip().replace(":", ""),
            description=columns[1].next_element.strip(),
            process=process,
        )
        related_part.save()
        crawler_related_people(columns[1], related_part)

#Crawler the related people from 2º column of related parts
def crawler_related_people(related_people_column, related_part):
    kinds = related_people_column.select('span')
    for kind in kinds:
        related_people = RelatedPeople(
            kind=kind.text.strip().replace(":", ""),
            name=kind.next_sibling.strip(),
            related_part=related_part
        )
        related_people.save()