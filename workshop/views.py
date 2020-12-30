from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .filters import WorkshopFilter

def home(request):
    category = Category.objects.all()
    context = {'category': category}

    return render(request, 'workshop/home.html', context)


def workshoplist(request, pk):

    workshop = Workshop.objects.filter(Category__in=pk)
    myFilter = WorkshopFilter()
    context ={'workshop': workshop, 'myFilter':myFilter}

    return render(request, 'workshop/workshoplist.html', context)


@login_required
def workshop_create(request):
    form = WorkShopForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}

    return render(request, "workshop/workshopForm.html", context)

@login_required
def category_create(request):
    form = NewCategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}

    return render(request, "workshop/workshopForm.html", context)

def workshop_detail(request, pk):
    workshop = Workshop.objects.filter(id=pk)
    comment = Comment.objects.all()

    forma = CommentForm(request.POST or None)
    if forma.is_valid():
        forma.save()
        return redirect('/')

    formb = TaskForm(request.POST or None)
    if formb.is_valid():
        formb.save()
        return redirect('/')

    context = {'forma': forma,'formb': formb, 'workshop': workshop, 'comment':comment}

    return render(request, "workshop/workshopDetail.html", context)

def register(request):

    if request. method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, now you can login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'workshop/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'workshop/profile.html')
