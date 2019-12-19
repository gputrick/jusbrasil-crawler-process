from .models import Process, Move
from .service import crawler_process
from rest_framework import viewsets
from .serializers import ProcessSerializer, MoveSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponseBadRequest
from datetime import timedelta
import datetime
import pytz

#View dos processos e do crawler
class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    #Crawler do processo
    @action(methods=['get'], detail=False)
    def crawler(self, request):
        process_number = request.query_params.get('process_number', None)
        
        if not process_number:
            return HttpResponseBadRequest("The field 'process_number' is required")

        #Filtra pelo número do processo
        process = [p for p in Process.objects.all() if p.process_number == process_number]
    
        #As duas datas precisam estar 'aware' para comparar
        last_day = pytz.UTC.localize(datetime.datetime.now() - datetime.timedelta(hours=24))
        
        #Se já foi crawleado nas ultimas 24 horas retorna ele mesmo
        if process and process[0].updated_at >= last_day:
            return Response(self.get_serializer(get_process_by_number(process_number)).data)
        else:
            #Caso contrário atualiza o processo
            process_id = (process[0].id if process else None)
            crawler_process(process_number, process_id)
        
            return Response(self.get_serializer(get_process_by_number(process_number)).data)

#Procura o processo pelo número
def get_process_by_number(process_number):
    return Process.objects.get(process_number=process_number)

#View das movimentações
class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer