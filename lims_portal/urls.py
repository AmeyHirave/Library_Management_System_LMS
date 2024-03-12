from django.contrib import admin
from django.urls import path
from lims_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #Added manually
    # path('', views.index),
    path('', views.home),
    path('returnedBooks/', views.returnedBooks),
    path('readers/', views.add_reader),
    path('books/', views.books),
    # path('booksData/', views.displayBooksData),
    # path('save', views.save),
    path('Cart', views.Cart),
    path('readers/add', views.saveUserData), 
    path('addData', views.addBooks),
    path('returnBookAndReader', views.addRentedDataToDB),
    path('delete/<int:id>', views.delete),
    path('testCode/', views.testCodeHere),

]
