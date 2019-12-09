from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def zwn(request):
    return render(request,'zwn.html')

def lyj(request):
    return render(request,'lyj.html')