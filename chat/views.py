from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room


@login_required
def index(request):
    rooms = Room.objects.order_by("title")

    return render(request, "chat/rooms.html", {
        "rooms": rooms,
    })
