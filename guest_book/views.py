from django.shortcuts import render
from .models import Guestbook
from .forms import GuestSearchForm

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
