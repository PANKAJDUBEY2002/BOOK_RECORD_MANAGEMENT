
from BRMapp import views
from django.urls import path
from BRMapp import views
urlpatterns=[
path('view-books',views.viewBooks),
path('edit-book',views.editBook),
path('delete-book',views.deleteBook),
path('search-book',views.searchBook),
path('new-book',views.newBook),
path('add',views.add),
path('search',views.search),
path('edit',views.edit),
]
