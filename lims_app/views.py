from django.shortcuts import render
from .models import reader,BooksData, rentalBookData, rentedBooksData
# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpRequest("hello")

def returnedBooks(request):
    rentedData = rentedBooksData.objects.all()  

    if request.method == "GET":
        username = request.GET.get('reader_name') 
        bookName = request.GET.get('reader_name') 
        
        if username != None or bookName != None:
            rentedData = rentedBooksData.objects.filter( reader_name__icontains = username)
            rentedData = rentedBooksData.objects.filter( book_name__icontains = bookName)
    sendRentedData = {
        'rentedData' : rentedData
    }
    return render(request, 'returnBooks.html', sendRentedData) #unchanged 

def add_reader(request):
    readerData = reader.objects.all()
    count = readerData.count()
    # Check if a search query is submitted
    if request.method == "GET":
        st = request.GET.get('searchBar')
        if st != None:
            readerData = reader.objects.filter(reader_name__icontains = st)
    dataSend = {
        'readerData': readerData,
        'Count' : count
    }
    return render(request, 'reader.html', dataSend)

def books(request):
    booksData = BooksData.objects.all()   
    countofBooks = booksData.count()
    if request.method == "GET":
        bookName = request.GET.get('book_name')
        if bookName != None:
            booksData = BooksData.objects.filter(book_name__icontains = bookName)
    sendBooksData = {
        'booksDataPrint' : booksData,
        'countofBooks' : countofBooks,
    }
    return render(request, 'books.html', sendBooksData)

def Cart(request):
    return render(request, 'myCart.html') #unchanged

# To manage  get direct information from user rather than going to admin page manually:
#  To add data from form of reader page to database
def saveUserData(request):
     if request.method == "POST":
        name = request.POST.get('reader_name')  # Corrected from reader.POST to request.POST
        ref_id = request.POST.get('reference_id')
        contact = request.POST.get('reader_contact')
        address = request.POST.get('reader_address')
        addData = reader(reader_name=name, reference_id=ref_id, reader_contact=contact,reader_address=address)  
        addData.save()
     return render(request, 'reader.html')

# Add books from user to DB:
def addBooks(request):
    if request.method == "POST":
        bookId = request.POST.get('book_id')
        bookName = request.POST.get('book_name')
        bookAuthor = request.POST.get('author_name')
        bookDesc = request.POST.get('book_description')
        totalCntofBooks = request.POST.get('total_Count')
        addBookData = BooksData(book_id = bookId, book_name = bookName, book_author_name = bookAuthor, book_description = bookDesc, cntOfBooks = totalCntofBooks)
        addBookData.save()
    return render(request, 'books.html')

# To display data directly
def return_book(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        reader_id = request.POST.get('reader_id')
        if book_id and reader_id:
            try:
                book_data = BooksData.objects.filter(book_id=book_id)
                reader_data = reader.objects.filter(reference_id=reader_id)
                rentalBookData.objects.create(
                    book=book_data,
                    reader=reader_data
                )
                return render(request, 'returnBooks.html')  # Redirect to the return_books page after saving
            except (BooksData.DoesNotExist, reader.DoesNotExist):
                pass  # Ignore invalid book or reader ID
    return render(request, 'returnBooks.html')

def addRentedDataToDB(request):
    if request.method == "POST":
        readerId = request.POST.get('reader_id')
        readerName = request.POST.get('reader_name')
        bookName = request.POST.get('book_name')
        contact = request.POST.get('phone_number')
        rentedData = request.POST.get('rented_date')
        returnDate = request.POST.get('return_date')
        addRentedData = rentedBooksData(reader_id = readerId, reader_name = readerName, book_name = bookName, readerContact = contact, rented_date = rentedData, return_date = returnDate)
        addRentedData.save()
    return render(request, 'returnBooks.html')

# For Delete the data
def delete(request, id):
  member = rentedBooksData.objects.get(reader_id=id)
  member.delete()
  return render(request, 'returnBooks.html')

# For Testing code 
def testCodeHere(request):
    return render(request, 'testCode.html')