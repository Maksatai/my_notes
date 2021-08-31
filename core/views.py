
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from core.models import Notes
from core.forms import Form_for_notes

def homepage(request):
    form_object=Notes.objects.filter(author__username=request.user)
    return render(request, 'home.html',{"forms":form_object})

def add_todo(request):
    form = Form_for_notes()
    if request.method == 'POST':
        form =Form_for_notes(request.POST, request.FILES)
        if form.is_valid():
            if 'image' in request.FILES:
                form.image = request.FILES['image']
            note = form.save(commit=False)
            note.author = request.user
            note.save() 
        else:
            print(form.errors)
        return redirect(homepage)
    
    form = Form_for_notes()
    return render(request, 'add_todo.html', {'form':form})


def mark_todo(request,id):
    todo=Notes.objects.get(id=id)
    todo.is_favorite=not todo.is_favorite
    todo.save()
    return redirect(homepage)

def delete_todo(request,id):
    todo=Notes.objects.get(id=id)
    todo.delete()
    return redirect(homepage)

def notes_detail(request,id):
    todo_object=Notes.objects.filter(id=id)
    return render(request, 'detail.html',{"forms":todo_object})

def edit(request, id):
    todo = Notes.objects.get(id=id)

    if request.method == 'POST':
        form = Form_for_notes(request.POST,request.FILES,instance=todo)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect(notes_detail, id=id)

    form = Form_for_notes(instance=todo)
    return render(request, 'add_todo.html', {'form': form})

class ProfileView(TemplateView):
    template_name = "profile.html"