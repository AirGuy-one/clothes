from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ClothesSerializer
from store.models import ClothsData


class Custom_pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20


class ClothesListCreate(generics.ListCreateAPIView):
    queryset = ClothsData.objects.all()
    serializer_class = ClothesSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Custom_pagination


class ClothesDelete(generics.DestroyAPIView):
    queryset = ClothsData.objects.all()
    serializer_class = ClothesSerializer
    permission_classes = [IsAdminUser]


class ClothsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClothsData.objects.all()
    lookup_field = 'pk'
    serializer_class = ClothesSerializer
    permission_classes = [IsAdminUser]

