from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("""<h1>Hey I am a Django server</h1>
    #                     <p>Hey this is comming from django server""")
    
    data = [
        {'name': 'Suyash Kumar','age': 20},
        {'name': 'Arun Gupta','age': 19},
        {'name': 'Rohan','age': 17},
        {'name': 'Soumya Tiwari','age': 22},
        {'name': 'Om Tiwari','age': 21}
    ]
    
    text = """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos dolores et veniam illo sequi dolorem magni, ullam rem quo distinctio officia modi rerum expedita obcaecati cupiditate, ut similique molestiae ipsum!
    """
    
    vegetables = ['Pumpkin','ladyfinger','Potato','Tomato']
    
    return render(request , 'home/index.html', context={'data' : data , 'text': text,'vegetables': vegetables})  

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def success_page(response):
    print("Hello")
    return HttpResponse("<h1>This is a success page</h1>")