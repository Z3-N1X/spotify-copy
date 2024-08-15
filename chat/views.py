from django.shortcuts import render, redirect
from chat.models import Room, Message, Player
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def account(request,room):
    return render(request, 'login.html', {
        'room': room
    })


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    user = Player.objects.get(name=username)
    money = user.money
    return render(request, 'room.html', {
        'username': username,
        'money': str(money),
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']


    if Room.objects.filter(name=room).exists():
        return redirect('/account/'+room+"/")

    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/account/'+room+"/")

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    user = Player.objects.filter(name=username)
    user.update(money= Player.objects.get(name=username).money+10)
    
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def getUser(request, user):
    pass
    # user_detail = .objects.get(name=room)

    # messages = Message.objects.filter(room=room_details.id)
    # return JsonResponse({"messages":list(messages.values())})


def signupUser(request,room):
    username = request.POST['username']
    password = request.POST['password']
    room = request.GET.get('room')

    if Player.objects.filter(name=username).exists():
        return HttpResponse("account already exists")
    else:
        new_user = Player.objects.create(name=username, userPassword=password, inv="", money=0)
        new_user.save()
        return redirect('/'+room+'/?username='+username)


def loginUser(request,room):
    username = request.POST['username']
    password = request.POST['password']
    room = request.GET.get('room')

    if not Player.objects.filter(name=username).exists():
        return HttpResponse("this account does not exist")
    if not Player.objects.filter(name=username, userPassword=password).exists():
        return HttpResponse("the password is not correct")
    else:
        return redirect('/'+room+'/?username='+username)


