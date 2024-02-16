

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

from marshmallow import Schema, fields

class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()
    year_published = fields.Int()

book = Book(title="Sample Book", author="John Doe", year_published=2022)
print(book )
print(type(book))
print(book.author)
print("=========")

book_schema = BookSchema()
serialized_book = book_schema.dump(book)
print(serialized_book)
print(type(serialized_book))
print("============") 

json_data = '{"title": "Another Book", "author": "Jane Smith", "year_published": 2021}'
book_schema = BookSchema()
deserialized_book = book_schema.load(json_data)
print(deserialized_book)
print(type(deserialized_book))

