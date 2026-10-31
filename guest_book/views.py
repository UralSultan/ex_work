from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Guestbook
from .forms import GuestSearchForm, GuestBookAddForm
from django.urls import reverse

def guest_list(request):
    search_form = GuestSearchForm(request.GET or None)
    guests = Guestbook.objects.filter(status="active").order_by("-created_at")
    if search_form.is_valid():
        name = search_form.cleaned_data["name"]
        if name:
            normalized_name = name.casefold()
            guests = [
                guest for guest in guests
                if guest.author_name.casefold() == normalized_name
            ]

    return render(request, "guest_book/guest_list.html", {
        "guests": guests,
        "search_form": search_form,
    })

def guest_add(request):
    if request.method == 'GET':
            form = GuestBookAddForm()
            return render(request, "guest_book/guest_create.html", {'form': form})
    elif request.method == 'POST':
        form = GuestBookAddForm(data=request.POST)
        if form.is_valid():
            guest = Guestbook.objects.create(
                author_name=form.cleaned_data.get('author_name', ''),
                author_email=form.cleaned_data.get('author_email', ''),
                content=form.cleaned_data.get('content', ''),
            )
            return HttpResponseRedirect(reverse('guest_list'))
        else:
            return render(request, "guest_book/guest_create.html", {'form': form})

def guest_update(request, pk):
    guest = get_object_or_404(Guestbook, pk=pk)
    if request.method == 'GET':
        form = GuestBookAddForm(initial={'author_name': guest.author_name, 'content': guest.content, 'author_email': guest.author_email})
        return render(request, 'guest_book/guest_update.html', {'guest': guest, 'form': form})
    elif request.method == 'POST':
        form = GuestBookAddForm(data=request.POST)
        if form.is_valid():
            guest.author_name = form.cleaned_data.get('author_name')
            guest.author_email = form.cleaned_data.get('author_email')
            guest.content = form.cleaned_data.get('content')
            guest.save()
            return HttpResponseRedirect(reverse('guest_list'))
        else:
            return render(request, 'guest_book/guest_update.html', {'guest': guest, 'form': form})