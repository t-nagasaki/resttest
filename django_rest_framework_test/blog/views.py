from django.shortcuts import render
# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer, UserEntriesSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class UserEntriesViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserEntriesSerializer
