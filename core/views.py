from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import TemplateView
from core.models import Notes
from core.forms import Form_for_notes

class AddTodoView(TemplateView):
    template_name = "add_todo.html"

def homepage(request):
    form_object=Notes.objects.all()
    return render(request, 'home.html',{"forms":form_object})

def add_todo(request):
    form = Form_for_notes()
    if request.method == 'POST':
        form =Form_for_notes(request.POST, request.FILES)
        if form.is_valid():
            if 'image' in request.FILES:
                form.image = request.FILES['image']
            form.save()
        else:
            print(form.errors)
        return redirect(homepage)
    
    form = Form_for_notes()
    return render(request, 'add_todo.html', {'form':form})