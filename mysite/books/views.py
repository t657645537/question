# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response
from models import Book
from models import test

def search(request):
    query = request.GET.get('q','')
    if query:
        qset = (
                Q(username__icontains=query) |
                Q(password__icontains=query)
            )

        results = test.objects.filter(qset).distinct()
    else:
        results = []

    return render_to_response("search.html",{
            "results":results,
            "query":query,
			"test":"aaa"
        })
