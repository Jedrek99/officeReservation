from datetime import datetime, date

from django.shortcuts import render, redirect
from django.views import View

from officeRes.models import Room, Reservation


# Create your views here.
def index(request):
    return render(request, 'base.html')


class Home(View):
    def get(self, request):
        rooms = Room.objects.all()
        rooms = rooms.order_by('name')
        reserved_today = Reservation.objects.filter(date=date.today())
        res = []
        for room in reserved_today:
            res.append(room.room_id)
        return render(request, 'home.html', {'rooms': rooms, 'res': res})
    def post(self, request):
        name = request.POST.get('name', '')
        room_capacity = request.POST.get('capacity', '')
        projector = request.POST.get('projector') == 'on'
        rooms = Room.objects.all()
        if projector:
            rooms = rooms.filter(projector=True)
        else:
            rooms = rooms.filter(projector=False)
        return render(request, 'home.html', {'rooms': rooms, 'capacity': room_capacity, 'projector': projector})
class Add_room(View):
    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):
        name = request.POST.get('name')
        try:
            capacity = int(request.POST.get('capacity'))
        except ValueError:
            capacity = 0
        projector = request.POST.get("projector") == "on"
        if capacity > 0:
            try:
                Room.objects.create(name=name, capacity=capacity, projector=projector)
                return redirect('/home/')
            except:
                return render(request, 'add_room.html')
        else:
            return render(request, 'add_room.html')

class Delete_room(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        room.delete()
        return redirect('/home')

class Modify_room(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, 'modify_room.html', {'room': room})

    def post(self, request, id):
        room = Room.objects.get(id=id)
        room.name = request.POST.get('name')
        room.projector = request.POST.get("projector") == "on"
        try:
            capacity = int(request.POST.get('capacity'))
        except ValueError:
            capacity = 0
        if capacity > 0:
            try:
                room.capacity = capacity
                room.save()
                return redirect('/home/')
            except:
                return render(request, 'add_room.html')
        else:
            return render(request, 'add_room.html')

class Reverve_room(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        reservations = Reservation.objects.filter(room_id=id)
        reservations = reservations.order_by('date')
        return render(request, 'reserve_room.html', {"room": room, 'reservations':reservations})
    def post(self, request, id):
        room = Room.objects.get(id=id)
        res_date = request.POST.get('date')
        comment = request.POST.get('comment')
        if Reservation.objects.filter(room_id=room, date=res_date).exists():
            return render(request, 'reserve_room.html', {"room": room})
        if res_date < str(date.today()):
            return render(request, 'reserve_room.html', {"room": room})
        Reservation.objects.create(room_id=room, date=res_date, comment=comment)
        return redirect('/home/')

class Room_detail(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        reservations = Reservation.objects.filter(room_id=id)
        reservations = reservations.order_by('date')
        return render(request, 'room_detail.html', {'room':room, 'reservations':reservations})

