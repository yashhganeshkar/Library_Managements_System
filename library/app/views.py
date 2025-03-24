
from .models import Books
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateNewBook, UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from .serializers import BooksSerializer

#student View
def book_list(request):
    books = Books.objects.all().order_by('-publish_date')
    return render(request,'books_list.html', {'books': books})

# #book details View
def book_details(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    return render(request, 'book_details.html', {"book": book})


#create View
@login_required
def book_create(request):
    if request.method == 'POST':
        form = CreateNewBook(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = CreateNewBook()
    return render(request, 'create_new_entry.html', {'form':form})

#Edit View
@login_required
def book_edit(request, book_id):
    book = get_object_or_404(Books, pk=book_id, added_by = request.user)
    if request.method == 'POST':
        form = CreateNewBook(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = CreateNewBook(instance=book)
    return render(request, 'create_new_entry.html', {'form':form})

#Delete View
@login_required
def book_delete(request, book_id):
    book = get_object_or_404(Books, pk=book_id, added_by = request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book':book})

#Register New Admin
def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('book_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form':form})
