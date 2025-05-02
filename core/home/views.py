from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return HttpResponse("""<h1>Hey I am a Django server</h1>
                        <p>Hey this is comming from django server""")

def success_page(response):
    return HttpResponse("<h1>This is a success page</h1>")