from django.test import TestCase
from rest_framework.test import APIRequestFactory

from .models import Move, Process, RelatedPart, RelatedPeople
from .service import parse_process, parse_moves, parse_related_parts
from .views import ProcessViewSet
from bs4 import BeautifulSoup
import os

class CrawlerTestCase(TestCase):
    process_number = '0067154-55.2010.8.02.0001';
    process_file_name = os.path.join(os.path.dirname(__file__), 'templates/process_'+process_number+'.html')
    soup=None

    def setUp(self):

        with open(self.process_file_name, 'r') as file:
            process_html = file.read().replace('\n', '')

        self.soup = BeautifulSoup(process_html, "html.parser")
    
    def test_parse_process(self):
        process = parse_process(self.soup, self.process_number)
        self.assertIsNotNone(process)
        self.assertIsNotNone(process.id)
        assert process.process_number == "0067154-55.2010.8.02.0001"
        assert process.kind == "Ação Civil Pública"
        assert process.area == "Cível"
        assert process.subject == "Tratamento Médico-Hospitalar e/ou Fornecimento de Medicamentos"
        assert process.distribuition == "29/09/2010 às 15:57 - Sorteio"
        assert process.judge == "Antonio Emanuel Dória Ferreira"
        assert process.action_value == "510,00"
    
    def test_parse_related_parts(self):
        empty_process = Process()
        empty_process.save()

        related_parts = parse_related_parts(self.soup, empty_process)

        self.assertTrue(related_parts)

        for related_part in related_parts:
            self.assertIsNotNone(related_part.id)
            self.assertIsNotNone(related_part.description)
            self.assertIsNotNone(related_part.date)
            self.assertIsNotNone(related_part.process)

    def test_parse_related_parts(self):
        empty_process = Process()
        empty_process.save()

        related_parts = parse_related_parts(self.soup, empty_process)

        self.assertTrue(related_parts)

        for related_part in related_parts:
            self.assertIsNotNone(related_part.id)
            self.assertIsNotNone(related_part.description)
            self.assertIsNotNone(related_part.kind)
            self.assertIsNotNone(related_part.process)
            self.assertTrue(related_part.related_people)