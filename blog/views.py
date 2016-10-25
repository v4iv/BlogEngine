from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Article
from blog.serializers import ContactSerializer, ArticleSerializer


# Create your views here.
class ArticleView(APIView):
    @staticmethod
    def get_object(slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        about = self.get_object(slug)
        serializer = ArticleSerializer(about)
        return Response(serializer.data)


class ContactView(APIView):
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
