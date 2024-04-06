from django.shortcuts import render
from BRMapp.forms import NewBookForm
from BRMapp import models
from django.http import HttpResponse
# Create your views here.
def editBook(request):
    book=models.Book.objects.get(id=request.get['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRMapp/edit_book.html',{'form':form,'book':book})
    return res


def edit(request):
    form=NewBookForm(request.post)
    book=models.Book()
    book.id=request.POST['bookid']
    book.title=form.data['title']
    book.price=form.data['price']
    book.author=form.data['author']
    book.pubisher=form.data['publisher']
    book.save()
    return HttpResponseRedirect('/BRMapp/view_book.html')

def viewBooks(request):
    books=models.Book.objects.all()
    res=render(request,'BRMapp/view_book.html',{'books':books})
    return res
def newBook(request):
    form=NewBookForm()
    res=render(request,'BRMapp/new_book.html',{'form':form})
    return res

def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
        s="Record Stored<br><a href='/BRMapp/view-books'>View all Books </a>"
        retuurn HttpResponse(s)
