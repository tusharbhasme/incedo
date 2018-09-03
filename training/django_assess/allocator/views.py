from django.contrib import messages
from django.core import serializers
from django.core.serializers import json
from django.shortcuts import render, redirect, get_object_or_404

from allocator.models import Book, Member, Issue
from .forms import addBook, addMember, issueBook


# Create your views here.


#Adding the books
def add_book(request):

    form = addBook(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()


    context = {
        'form': form,
    }

    return render(request,"allocator/add_book.html",context)


#Removing the books

def add_member(request):

    form1 = addMember(request.POST or None)
    if form1.is_valid():
        instance = form1.save(commit=False)
        instance.save()
    context = {
            'form': form1
    }
    return render(request, "allocator/add_member.html", context)


def issue_book(request):

    form2 = issueBook(request.POST or None)
    if form2.is_valid():
        instance = form2.save(commit=False)
        instance.save()

    context = {
            'form': form2
        }

    return render(request, "allocator/issue_book.html",context)


#Retreiving the data

def book_list(request):

    queryset = Book.objects.all()

    context = {
        'book_list': queryset,
        'title': 'List'

    }

    return render(request, "allocator/book_list.html", context)


def member_list(request):

    queryset = Member.objects.all()

    context = {
        'member_list': queryset,
        'title': 'Members'

    }

    return render(request, "allocator/member_list.html", context)


def issue_list(request):

    queryset = Issue.objects.all()

    context = {
        'issue_list': queryset,
        'title': 'Issued books'

    }

    return render(request, "allocator/issue_list.html", context)


#Deleting the records

def del_books(request, isbn):

    book = get_object_or_404(Book, isbn=isbn).delete()
    messages.success(request, "deleted successfully")
    return redirect(book_list)


def del_member(request, member_id):

    member = get_object_or_404(Member, member_id=member_id).delete()
    messages.success(request, "deleted successfully")
    return redirect(member_list)


def return_book(request, id):

    book = get_object_or_404(Issue, id=id).delete()
    messages.success(request, "deleted successfully")
    return redirect(issue_list)