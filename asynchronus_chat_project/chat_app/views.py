from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')

def room(request,room_name):
    return render(request,'chatroom.html',{
        'room_name' : room_name
    })