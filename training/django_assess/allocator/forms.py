from django import forms

from .models import Book, Member, Issue


class addBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'


class addMember(forms.ModelForm):

    class Meta:
        model = Member
        fields = '__all__'


class issueBook(forms.ModelForm):

    class Meta:
        model = Issue
        fields = '__all__'

