from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = Blogform(request.POST,request.FILES)
            if form.is_valid():
                p = form.save(commit=False)
                p.created_by = request.user
                p.save()
                return HttpResponseRedirect('/')
        else:
            form = Blogform()

        obj = Blogdata.objects.order_by('-Date_created')
        return render(request,'blog.html',{'form':form,'obj':obj})
    else:
        return HttpResponseRedirect('/')
def delete(request):
    # n=Blogdata.objects.get(id=d)
    # n.delete()
    return HttpResponseRedirect('/')

def delajax(request):
    iddel = request.GET.get('id', None)
    data = {
        'is_del':Blogdata.objects.get(id=iddel).delete()
    }
    return JsonResponse(data)

def search(request):
    if request.method == "POST":
        s = request.POST['search']
        obj = Blogdata.objects.filter(comment__contains=s)
        #obj = Blogdata.objects.filter(Q(comment__contains=s) | Q(title__contains=s) | Q(created_by__contains=s))
        return render(request, 'search.html',{'obj': obj})



