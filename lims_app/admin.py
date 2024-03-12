from django.contrib import admin
from .models import *
# Register your models here.
#to use reader or any class in db we have to register it here
# class readerAdmin(admin.ModelAdmin):
    # list_display=('reader_name', 'reader_id', 'reader_address', 'reader_contact')
admin.site.register(reader) #current working
admin.site.register(BooksData)  #current working
admin.site.register(myCartData)
admin.site.register(returnBooks)
admin.site.register(rentalBookData)
admin.site.register(rentedBooksData) #current working