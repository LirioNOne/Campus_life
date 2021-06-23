from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Event, GoingToEvent, Comments
from .forms import AddComment, AddEvent


def main_page(request):
    qs = Event.objects.all()
    user = request.user

    context = {
        'qs': qs,
        'user': user,
    }
    return render(request, 'CampusLife/Main_page.html', context)


def going_to_event(request):
    user = request.user
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event_obj = Event.objects.get(id=event_id)

        if user in event_obj.going_to_event.all():
            event_obj.going_to_event.remove(user)
        else:
            event_obj.going_to_event.add(user)

        event, created = GoingToEvent.objects.get_or_create(user=user, event_id=event_id)

        if not created:
            if event.value == 'Пойти':
                event.value = 'Уже иду'
            else:
                event.value = 'Пойти'

        event.save()
    return redirect('events:main_page')


def going_to_event_detail(request, pk):
    qs = GoingToEvent.objects.filter(event=pk)
    context = {
        'qs': qs,
    }
    return render(request, 'CampusLife/Going_to_event_details.html', context)


def event_detail(request, pk):
    qs = Comments.objects.filter(event=pk)
    event = Event.objects.filter(id=pk)
    form = AddComment()
    user = request.user

    if request.method == 'POST':
        event_obj = Event.objects.get(id=pk)

        if user in event_obj.going_to_event.all():
            event_obj.going_to_event.remove(user)
        else:
            event_obj.going_to_event.add(user)

        event, created = GoingToEvent.objects.get_or_create(user=user, event_id=pk)

        if not created:
            if event.value == 'Пойти':
                event.value = 'Уже иду'
            else:
                event.value = 'Пойти'

        event.save()
        return redirect('events:event_detail', pk)

    context = {
        'qs': qs,
        'event': event,
        'form': form,
    }
    return render(request, 'CampusLife/Event_details.html', context)


def comments(request, pk):
    user = request.user
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        form = AddComment(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.event = event
            obj.user = user
            obj.save()

            return redirect('events:event_detail', pk)


def create_event(request):
    user = request.user
    if request.method == "POST":
        form = AddEvent(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator_id = user
            obj.save()

            return redirect('events:main_page')
    else:
        form = AddEvent()
        context = {
            'form': form
        }
        return render(request, 'CampusLife/Create.html', context)


def edit_event(request, pk):
    try:
        event = Event.objects.get(id=pk)

        if request.method == "POST":
            event.title = request.POST.get("title")
            event.description = request.POST.get("description")
            event.event_img = request.POST.get("event_img")
            event.save()
            return redirect('events:main_page')
        else:
            form = AddEvent()
            context = {
                'form': form,
                'event': event,
            }
            return render(request, 'CampusLife/Edit_Events.html', context)
    except Event.DoesNotExist:
        return HttpResponseNotFound("<h2>Событие не найдено</h2>")


def delete_event(request, pk):
    try:
        event = Event.objects.get(id=pk)
        event.delete()
        return redirect('events:main_page')
    except Event.DoesNotExist:
        return HttpResponseNotFound("<h2>Событие не найдено</h2>")


def login_page(request):
    return render(request, 'CampusLife/Login_page.html')


def registration_page(request):
    return render(request, 'CampusLife/Registration_page.html')
