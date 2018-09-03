from allocator.models import Book


def decode_book(o):
    if '__Book__' in o:

        a = Book()

        a.__dict__.update(o['__Book__'])
        return a
    return o


