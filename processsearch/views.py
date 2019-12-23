import datetime

import pytz
from django.http import HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Move, Process
from .serializers import MoveSerializer, ProcessSerializer
from .service import crawler_process



#Crud process view and crawler
class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    #Crawler the process and save in database
    @action(methods=['get'], detail=False)
    def crawler(self, request):
        process_number = request.query_params.get('process_number', None)
        
        if not process_number:
            return HttpResponseBadRequest("The field 'process_number' is required")

        #Filter by process by number in memory
        process = [p for p in Process.objects.all() if p.process_number == process_number]

        #both the datetime objects needs to be aware to compare them
        last_day = datetime.datetime.now() - datetime.timedelta(hours=24)

        #if it was crawled 24 hours later, then returns the database register
        if process and process[0].updated_at >= last_day:
            return Response(self.get_serializer(get_process_by_number(process_number)).data)
        else:
            #Delete the existing process
            if process:
                get_process_by_number(process_number).delete()
                crawler_process(process_number)
        
            return Response(self.get_serializer(get_process_by_number(process_number)).data)

#Search the process by number
def get_process_by_number(process_number):
    return Process.objects.get(process_number=process_number)

#Moves view
class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
