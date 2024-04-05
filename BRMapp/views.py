from django.shortcuts import render
from BRMapp.forms import NewBookForm
# Create your views here.


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
