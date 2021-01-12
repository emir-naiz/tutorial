from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
# Create your views here.

class DocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        try:
            groups = []
            group = self.request.user.groups.all()
            for mark in group:
                groups.append(mark.name)
            print(groups)
            queryset = Document.objects.filter(mark__in=groups)
            return queryset
        except IndexError:
            queryset = Document.objects.first()
            return queryset


        # if group == 'private':
        #     queryset = Document.objects.filter(mark=group)
        #     return queryset
        # elif group == 'lieutenant':
        #     queryset = Document.objects.filter(mark=group)
        #     return queryset