from django.shortcuts import render

# Create your views here.
def books_list(request):
    return render(request, 'book_lending/books_list.html', {})


def people_list(request):
    return render(request, 'book_lending/people_list.html', {})

