import datetime

from django.db import models

# Create your models here.
class Book(models.Model):


    isbn = models.CharField(max_length=50,primary_key=True)
    book_name = models.CharField(max_length=50)
    publication = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stock = models.IntegerField()

    def __str__(self):
        return self.book_name


class Member(models.Model):

    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=50)
    mob_no = models.CharField(max_length=10)

    def __str__(self):
        return self.member_name


class Issue(models.Model):


    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now=True)
    return_date = models.DateField()

    def __unicode__(self):
        return self.isbn


