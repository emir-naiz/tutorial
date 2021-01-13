from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from datetime import date
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
            today = date.today()
            for doc in queryset:
                if doc.date_unvaliable < today:
                    doc.delete()
            return queryset
        except IndexError:
            queryset = Document.objects.first()
            return queryset


