import datetime

import pytz
from django.http import HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Move, Process
from .serializers import MoveSerializer, ProcessSerializer
from .service import crawler_process


# Crud process view and crawler
class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    # Crawler the process and save in database
    @action(methods=['get'], detail=False)
    def crawler(self, request):
        process_number = request.query_params.get('process_number', None)

        if not process_number:
            return HttpResponseBadRequest("The query param 'process_number' is required")

        process = crawler_process(process_number)
        serialized_process = self.get_serializer(process).data

        return Response(serialized_process)
