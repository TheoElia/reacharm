from django.shortcuts import render

# Create your views here.
def index(request):
    template="accounts/index.html"
    args = {}
    return render(request,template,args)