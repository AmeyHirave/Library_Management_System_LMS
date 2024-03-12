import datetime
from django.db import models

# Create your models here. #models means database tables
#Reader page database
class reader(models.Model):
    # To return name of reader on db we used __str__. 
    #In Django, the __str__() method is a special method that provides a string representation of an object. It's called a "dunder" (double underscore) method or a "magic" method.
    def __str__(self): 
        return self.reader_name    
    reference_id  = models.CharField(max_length=200, default='0')
    reader_name = models.CharField(max_length=200, default='0')
    reader_contact = models.CharField(max_length=12, default='0')
    reader_address = models.TextField()
    active = models.BooleanField(default=True)

class BooksData(models.Model):
    def __str__(self):
        return self.book_name
    book_id = models.CharField(max_length = 100)
    book_name = models.CharField(max_length = 255)
    book_author_name = models.CharField(max_length = 100)
    cntOfBooks = models.IntegerField(default = 0)
    book_description = models.TextField()

    #Sorry This is logic not worked :( 
class myCartData(models.Model):
    def __str__(self):
        return self.book_name_in_cart
    book_id_in_cart = models.IntegerField(default = 0 )
    book_name_in_cart = models.CharField(max_length = 100)
    totalCount = models.IntegerField(default = 0 )

    #Sorry This is logic not worked :( 
class returnBooks(models.Model):
    def __str__(self):
        return self.readerName
    bookId = models.IntegerField(default = 0)
    bookName = models.CharField(max_length=250)
    readerId = models.IntegerField(default = 0)
    readerName = models.CharField(max_length=255)
    

# chatgpt for adding data from one table to another using foreign key
    #Sorry This is logic not worked :( 
class rentalBookData(models.Model):
    def __str__(self):
        return f"{self.book.book_name} - {self.reader.reader_name}"   
    book = models.ForeignKey(BooksData, on_delete=models.CASCADE)
    reader = models.ForeignKey(reader, on_delete=models.CASCADE)

class rentedBooksData(models.Model):
    def __str__(self):
        return self.reader_name
    reader_id = models.IntegerField()
    reader_name = models.CharField(max_length = 255)
    book_name = models.CharField(max_length = 255)
    readerContact = models.CharField(max_length = 12)
    rented_date = models.DateField()
    return_date = models.DateField()