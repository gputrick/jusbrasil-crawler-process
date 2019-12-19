from .models import Process, Move
from .service import crawler_process
from rest_framework import viewsets
from .serializers import ProcessSerializer, MoveSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponseBadRequest
from django.utils import timezone
from datetime import timedelta

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    @action(methods=['get'], detail=False)
    def crawler(self, request):
        process_number = request.query_params.get('process_number', None)
        
        if not process_number:
            return HttpResponseBadRequest("The field 'process_number' is required")

        #Filtra os processos pelo número de pelos q foram gerados nas ultimas 24horas
        now = timezone.now().date()
        last_day = now - timedelta(days=1) 
        process = Process.objects.filter(process_number=process_number)
        valid_process = process.filter(updated_at__range=(last_day, now))

        #Se já foi crawleado nas ultimas 24 horas retorna ele mesmo
        if valid_process:
            return Response(self.get_serializer(valid_process, many=True))
        else:
            #Caso contrário deleta o processo existente e crawleia novamnete
            process_updated = crawler_process(process_number, process.first.id)
            return Response(self.get_serializer(process_updated, many=True))


class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

# class CrawlerProcess(generics.ListAPIView):
#     serializer_class = ProcessSerializer

#     def get_queryset(self):
        
#         queryset = Process.objects.all()
#         process = self.request.query_params.get('username', None)
#         if username is not None:
#             queryset = queryset.filter(purchaser__username=username)
#         return queryset