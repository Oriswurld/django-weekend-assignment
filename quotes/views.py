from django.shortcuts import render
from .models import Quote
import random

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quote-list.html', {'quotes': quotes})

def random_quote(request):
    quotes = Quote.objects.all()
    random_quote = random.choice(quotes) if quotes else None
    return render(request, 'random-quote.html', {'quote': random_quote})

