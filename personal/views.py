from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'personal/home.html')
    
def contact(request):
    return render(request,'personal/basic.html',{'contacts':['Email me at : bjtamuly@gmail.com','Call at: 9916686072']})
#def contact(request):
    #return HttpResponse("<a><h3> Email me at :</a> bjtamuly@gmail.com</h3><br><h4><a>Call at: </h4></a> 9916686072<br>")
