from django.shortcuts import render
from.models import page,Slider_Images
# Create your views here.
def index(request):
    mod=page.objects.all()
    ton = Slider_Images.objects.all()
    context={
        'mod':mod,
        'ton':ton
    }
    return render(request,'index_html.html',context=context)

def detail(request,pk):
    mod=page.objects.get(pk=pk)
    context={
        'mod':mod

    }
    return render(request,'detail.html',context=context)

def banner(request):
    ton=Slider_Images.objects.all()

    context={
        'ton':ton
    }

    return render(request,'Slider.html',context=context)