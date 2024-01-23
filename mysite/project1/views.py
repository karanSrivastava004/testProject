from django.shortcuts import render

# Create your views here.
def Home(request):
    d="Vaibhav"
    context={"data":d}
    return render(request,"index.html",context)
def login(request):
    # print(request)
    pass
