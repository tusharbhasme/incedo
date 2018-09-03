from django.conf.urls import url


from allocator.views import add_book, add_member, issue_book, book_list, member_list, issue_list, del_books, del_member, \
    return_book

urlpatterns = [

    #adding the books

    url(r'^addbook/$',add_book, name='addbook'),
    url(r'^addmember/$', add_member, name='addmember'),
    url(r'^issue/$', issue_book, name='issue'),
    url(r'^booklist/$', book_list, name='booklist'),
    url(r'^memberlist/$', member_list, name='memberlist'),
    url(r'^issuelist/$', issue_list, name='issuelist'),
    url(r'^delbook/(?P<isbn>\d+)/$', del_books, name='delbook'),
    url(r'^delmember/(?P<member_id>\d+)/$', del_member, name='delmember'),
    url(r'^return/(?P<id>\d+)/$', return_book, name='returnbook'),

                ]