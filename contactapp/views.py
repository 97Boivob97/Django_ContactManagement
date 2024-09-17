from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Info
from .forms import InfoForm

# Create your views here.

def homepage(request):
   infos = Info.objects.all()
   context = {"infos":infos}
   return render(request,'homepage.html',context)


def add(request):
   if request.method == "POST":
      form = InfoForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('homepage')
   else:
      form = InfoForm()

   context = {"form":form}
   return render(request,'add.html',context)

def update(request,pk):
    try:
        info = Info.objects.get(pk=pk)
        if request.method == "POST":
            form = InfoForm(request.POST,instance=info)
            if form.is_valid():
                form.save()
                return redirect('homepage')
            else:
                context = {
                    "form":form,
                }
                return render(request,'update.html',context)
        else:
            form = InfoForm(instance=info)
            context = {
             "form":form
            }
            return render(request,'update.html',context)
    except Info.DoesNotExist:
        return HttpResponse("Contact does not exists!")
    

def delete(request,pk):
   try:
      info = Info.objects.get(pk=pk)
      info.delete()
      return redirect('homepage')
   except Info.DoesNotExist:
      return HttpResponse("Contact Does Not Exists!")
   
def search(request):
    query = request.GET.get('q', '')
    if query:
        infos = Info.objects.filter(
            first_name__icontains=query
        ) | Info.objects.filter(
            last_name__icontains=query
        ) | Info.objects.filter(
            email__icontains=query
        ) | Info.objects.filter(
            phone_number__icontains=query
        ) | Info.objects.filter(
            address__icontains=query
        )
    else:
        infos = Info.objects.all()
    
    context = {"infos": infos, "query": query}
    return render(request, 'search.html', context)







