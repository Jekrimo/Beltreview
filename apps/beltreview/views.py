from django.shortcuts import render, redirect
from . import models
from models import Users, Books, Reviews, Author

def index(request):
    return render(request, "beltreview/index.html")

def createuser(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passconf']:
            user = Users.createuser.register(name=request.POST['name'],alias=request.POST['alias'],email_address=request.POST['email'],create_password=request.POST['password'])
            if user[0] == True:
                print user[2]
                request.session['user'] = user[2].id
                return redirect('/books')
            else:
                context = {
                    'errors' : user[1]
                }
                return render(request, "beltreview/index.html", context)
        else:
            context={
                'errors': 'passwords dont match'
            }
            return render(request, "beltreview/index.html", context)
    else:
        return redirect("/")

def loginuser(request):
    return redirect("/books")

def show(request):
    context= {
        'books' : Books.objects.all(),
        'Users' : Users.objects.get(id=request.session['user'])
        }
    return render(request, "beltreview/show.html", context)

def addbook(request):
    context= {
            'authors' : Author.objects.all()
        }
    return render(request, "beltreview/bookcreate.html", context)

def createbook(request):
    if request.method == "POST":
        if request.POST['newauthor'] > "":
            author = Author.objects.create(name=request.POST['newauthor'])
            book = Books.objects.create(title =request.POST['title'], author=author)
            print book.id
            user = Users.objects.get(id=request.session['user'])
            Reviews.objects.create(book=book, review=request.POST['review'],rating=request.POST['rating'], user=user)
            return redirect('/books/'+ str(book.id))
        if request.POST['newauthor'] == "":
            author= Author.objects.get(name=request.POST['author'])
            user = Users.objects.get(id=request.session['user'])
            book = Books.objects.create(title =request.POST['title'], author=author)
            Reviews.objects.create(book=book, review=request.POST['review'],rating=request.POST['rating'], user=user)
            return redirect('/books/'+ str(book.id))

def showbook(request, id):
    book= Books.objects.get(id=id)
    context= {
            'user' : Users.objects.get(id=request.session['user']),
            'books' : Books.objects.get(id=id),
            'reviews' : Reviews.objects.filter(book=book),
        }
    return render(request, "beltreview/showbook.html", context)

def createreview(request, id):
    book= Books.objects.get(id=id)
    user = Users.objects.get(id=request.session['user'])
    Reviews.objects.create(book=book, review=request.POST['review'],rating=request.POST['rating'], user=user)
    return redirect('/books/'+ str(book.id))

def logout(request):
    request.session.clear()
    return redirect('/')
