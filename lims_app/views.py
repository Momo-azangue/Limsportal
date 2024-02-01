from django.db.models import Sum
from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from .models import *


# Create your views here.

def home(request):
    return render(request,"home.html",context={"current_tab": "home"})

def readers(request):
    return render(request,"readers.html",context={"current_tab": "readers"})

def books(request):
    return render(request,"books.html",context={"current_tab": "books"})



def books_tab(request):
    books = book.objects.all()
    return  render(request, "books.html", context={ "current_tab": "books", "books":books})






def mybag(request):
    return render(request,"mybag.html",context={"current_tab": "mybag"})

def returns(request):
    return render(request,"returns.html",context={"current_tab": "returns"})


def readers_tab(request):
    readers = reader.objects.all()
    return render(request,"readers.html",context={"current_tab": "readers", "readers":readers})

def save_reader(request):
    reader_item = reader(reference_id=request.POST['reader_ref_id'],
                         reader_name=request.POST['reader_name'],
                         reader_contact=request.POST['reader_conctact'],
                         reader_address=request.POST['reader_address'],
                         active=True,
                         )
    reader_item.save()
    return redirect('/readers')

def shopping(request):
    return HttpResponse("welcome to shopping")

def save_student(request):
    student_name=request.POST['student_name']
    return render("welcome.html",context={'student_name':student_name})


def save_book(request):
    book_item = book(titre=request.POST['titre'],
                     auteur=request.POST['auteur'],
                     annee_publication=request.POST['annee_publication'],
                     isbn=request.POST['isbn'],
                     categorie=request.POST['categorie'],
                     disponibilite=True,
                    nombre_exemplaires=request.POST['nombre_exemplaires'],
                     )
    book_item.save()
    return redirect('/books')

def save_book(request):
    book_item = book(titre=request.POST['titre'],
                     auteur=request.POST['auteur'],
                     annee_publication=request.POST['annee_publication'],
                     isbn=request.POST['isbn'],
                     categorie=request.POST['categorie'],
                     disponibilite=True,
                    nombre_exemplaires=request.POST['nombre_exemplaires'],
                     )
    book_item.save()
    return redirect('/books')



def search_results(request):
    query = request.GET.get('q')
    results = book.objects.filter(titre__icontains=query)
    return render(request, "books.html", {'results': results, 'query': query})


def add_to_bag(request, book_id):
    book_instance = book.objects.get(id=book_id)
    reader_instance = reader.objects.first()  # Vous devez déterminer quel lecteur est actuellement connecté
    reader_instance.mybag.add(book_instance)
    return redirect('mybag')

def remove_from_bag(request, book_id):
    book_instance = book.objects.get(id=book_id)
    reader_instance = reader.objects.first()  # Vous devez déterminer quel lecteur est actuellement connecté
    reader_instance.mybag.remove(book_instance)
    return redirect('mybag')

def mybag(request):
    reader_instance = reader.objects.first()  # Vous devez déterminer quel lecteur est actuellement connecté
    mybag_books = reader_instance.mybag.all()
    return render(request, 'mybag.html', {'mybag_books': mybag_books})