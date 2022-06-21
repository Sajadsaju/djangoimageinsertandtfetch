from django.shortcuts import render
from .models import ImgModel
from .form import ImgForm

# Create your views here.
def home(request):
    form=ImgForm()
    if request.method=='POST':
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            img_objects=form.instance
            return render(request,"index.html",{'form':form,'img_objects':img_objects})
