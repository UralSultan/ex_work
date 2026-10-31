from django.shortcuts import render
from .models import Guestbook

def guest_list(request):
    guests = Guestbook.objects.filter(status="active").order_by("-created_at")
    return render(request, "guest_book/guest_list.html", {"guests": guests})
