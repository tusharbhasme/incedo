from rest_framework.serializers import ModelSerializer

from .models import Book, Member, Issue


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
