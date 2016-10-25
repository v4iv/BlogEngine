from rest_framework import serializers

from blog.models import Contact, Article, Category, Social, About


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'slug')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id', 'title', 'slug', 'subtitle', 'category', 'image', 'content', 'featured', 'meta', 'published_date'
        )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('fullname', 'email', 'message')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('__all__')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('id', 'icon', 'title', 'url')
