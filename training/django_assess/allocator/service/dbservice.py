import json

from allocator.serialize.customDecoder import decode_book

books = {}
members = {}
issues = {}


def save_book(book):
    books[book.isbn] = book


def get_book(isbn):

    return books[isbn]


def delete_book(isbn):

    del books[isbn]


def list_books():
    return books.values()


def commit():
    with open("books.db.json", "w") as bookdata :
        json.dump(books,bookdata)


def load():
    global books
    with open("books.db.json", "r") as bookdata:
        books = json.load(bookdata, object_hook=decode_book)



#Members


def save_member(member):
    books[member.member_id] = member


def get_book(member_id):
    return members[member_id]


def delete_book(member_id):
    del members[member_id]


def list_members():
    return members.values()


def commit():
    with open("books.db.json", "w") as bookdata:
        json.dump(members, bookdata)


def commit():
    with open("members.db.json", "w") as memberdata :
        json.dump(members,memberdata)


def load():
    global members
    with open("members.db.json", "r") as memberdata:
        members = json.load(memberdata, object_hook=decode_book)



#Issues



def save_member():
    books[member.member_id] = member


def get_book(member_id):
    return members[member_id]


def delete_book(member_id):
    del members[member_id]


def list_members():
    return members.values()


