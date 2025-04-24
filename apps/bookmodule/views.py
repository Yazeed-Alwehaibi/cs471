from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Address, department, Student2,card,course
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .forms import bookForm


def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def links(request):
    return render(request, "bookmodule/html5.html")

def formatting(request):
    return render(request, "bookmodule/formatting.html")

def listing(request):
    return render(request, "bookmodule/listing.html")

def tables(request):
    return render(request, "bookmodule/tables.html")

def search(request):
    return render(request, "bookmodule/search.html")





def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True

            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, "bookmodule/search.html")



def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull =
    False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

# lab 8
def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/task1.html', {'books': books})



def task2(request):
    books = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/task2.html', {'books': books})


def task3(request):
    books = Book.objects.filter(~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/task3.html', {'books': books})


def task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})


def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def task7(request):
    student_count = Address.objects.annotate(num_students=Count('student'))
    return render(request, 'bookmodule/task7.html', {'student_count': student_count})



# lab 9
def number_of_students_department(request):
    num_of_students = department.objects.annotate(num_students=Count('student2'))
    return render(request, 'bookmodule/l9t1.html', {'number_of_students': num_of_students})


def number_of_students_course(request): 
    num_of_students = course.objects.annotate(num_students=Count('student2'))
    return render(request, 'bookmodule/l9t2.html', {'number_of_students': num_of_students})



def oldest(request):
    departments = department.objects.annotate(oldest_student_id=Min('student2__id'))
    
    department_with_oldest_student = []
    for dept in departments:
        oldest_student = Student2.objects.get(id=dept.oldest_student_id)
        department_with_oldest_student.append({
            'department': dept,
            'oldest_student': oldest_student
        })
    
    return render(request, 'bookmodule/l9t3.html', {'department_with_oldest_student': department_with_oldest_student})

def descending(request):
    departments = department.objects.annotate(num_students=Count('student2')).filter(num_students__gt=2).order_by('-num_students')
    return render(request, 'bookmodule/l9t4.html', {'departments': departments})




# lab 10 part 1
def list_books_part1(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks.html', {
        'books': books,
        'add_url': 'add_book_part1',
        'edit_url': 'edit_book_part1',
        'delete_url': 'delete_book_part1',
    })


def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
    return render(request, 'bookmodule/addbook.html')


def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
    return render(request, 'bookmodule/editbook.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('listbooks')



# lab 10 part 2

def list_books_part2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks_part2.html', {'books': books})


def add_book_part2(request):
    if request.method == "POST":
        form = bookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listbooks_part2')
    else:
        form = bookForm()
    return render(request, 'bookmodule/addbook_part2.html', {'form': form})
    

def edit_book_part2(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = bookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('listbooks_part2')
    else:
        form = bookForm(instance=book)

    return render(request, 'bookmodule/editbook_part2.html', {'form': form})


def delete_book_part2(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('listbooks_part2')

    