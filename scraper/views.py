from django.shortcuts import render, HttpResponseRedirect
from django import forms
from .models import Link
import requests
from bs4 import BeautifulSoup

class ScrapeForm(forms.Form):
    site = forms.URLField()

def scrape(request):
    site = ""  # Initialize the variable outside the if block
    if request.method == "POST":
        form = ScrapeForm(request.POST)
        if form.is_valid():
            site = form.cleaned_data['site']
            try:
                page = requests.get(site)
                page.raise_for_status()  # Check for HTTP errors
                soup = BeautifulSoup(page.text, 'html.parser')

                for link in soup.find_all('a'):
                    link_address = link.get('href')
                    link_text = link.string
                    if link_address:
                        Link.objects.create(address=link_address, name=link_text)

                return HttpResponseRedirect('/')
            except requests.RequestException as e:
                # Handle the exception
                pass

    data = Link.objects.all()
    context = {'data': data, 'site': site}

    return render(request, 'scraper/result.html', context=context)


def clear(request):
    Link.objects.all().delete()
    return render(request, 'scraper/result.html')