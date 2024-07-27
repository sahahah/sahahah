from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import AddeventForm

from django.contrib.auth import authenticate, login, logout


from django.views.decorators.csrf import csrf_exempt 


from .forms import EventForm, CreateUserForm, UserEventForm
from .filters import EventFilter

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only

# from .forms import RegeventForm
from .forms import UserEventForm
from .models import UserEvent
from django.shortcuts import get_object_or_404

from .models import Events , Feedback, partcipateEvents
from .forms import FeedbackForm, partcipateForm

# Create your views here.
from .models import *

@unauthenticated_user
def registerPage(request):
   
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='user')
                user.groups.add(group)
                messages.success(request, 'Account was created for '+username+'!')

                return redirect('login')
            
        context = {'form':form}
        return render (request, 'events/register.html', context)

@unauthenticated_user
def loginPage (request):

            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('homePage')
                else:
                    messages.info(request, 'Username OR password is incorrect')
            context = {}
            return render(request, 'events/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    users = User.objects.all()
    events = Events.objects.all()
    
    total_users = users.count()

    total_events = events.count()
    completed = events.filter(category='Completed').count()
    pending = events.filter(category='Pending').count()

    context = {'users':users,'events':events,
    'total_events':total_events,'completed':completed,'pending':pending}

    return render(request, 'events/dashboard.html', context)
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def userPage(request):
    context = {}
    return render (request, 'events/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def events(request):
    events = Events.objects.all()
    return render(request, 'events/allevents.html', {'events': events})




def user(request,pk_test):
    user = User.objects.get(id=pk_test)

    regevents = user.regevents_set.all()
    regevents_count = regevents.count()

    myFilter =  EventFilter(request.GET, queryset=regevents)
    regevents = myFilter.qs

    username = request.user.username
    user = get_object_or_404(User, username=username)
    
    user_event = UserEvent.objects.filter(user=user).first()
    # context = {'user_event':user_event}
    # print(user_event) 
    # user_id = request.user.id
    
   
    # return render(request, 'events/account_settings.html',context)
    user= request.user
    user_event = None
    form = UserEventForm(instance=user)
   
    try:
        user_event = UserEvent.objects.get(user=user)
    except UserEvent.DoesNotExist:
        pass
    
    if request.method == 'POST':
        form = UserEventForm(request.POST, request.FILES, instance=user_event)
        if form.is_valid():
            form.save()

    context = {'user':user, 'regevents':regevents,'regevents_count':regevents_count,'myFilter':myFilter,'user_event': user_event, 'form': form,}
    return render(request, 'events/aboutus.html',context)
 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventForm

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createEvent(request, pk):
    EventFormSet = inlineformset_factory(User, regEvents,fields=('Events','status'))
    user = User.objects.get(id=pk)
    formset = EventFormSet(queryset=regEvents.objects.none(), instance=user)
    #form = EventForm(initial={'user':User})

    if request.method == 'POST':
        #print('Printing POST:',request.POST)
        formset = EventFormSet(request.POST, instance=user)
        if formset.is_valid():
            formset.save()
            return redirect('/')
        

    context = {'formset': formset}
    return render(request, 'events/event_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateEvent(request,pk):

    event = Events.objects.get(id=pk)
    form = EventForm(instance=event)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'events/event_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteEvent(request, pk):
    event = Events.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        return redirect('/')
    context = {'item':event}
    return render(request, 'events/delete.html', context) 


@login_required(login_url='login')
def homePage(request):
    context = {}
    return render (request, 'events/home.html', context)

@login_required(login_url='login')
def eventsPage(request):
    events = Events.objects.order_by('-date_created')
    # latest_event = Events.objects.order_by('-date_created').first()
    context = {'events':events}
    return render (request, 'events/events.html', context)

@login_required(login_url='login')
def clubPage(request):
    context = {}
    return render (request, 'events/clubs.html', context)

@login_required(login_url='login')
def Evre(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    context = {'event': event}
    return render(request, 'events/evre.html', context)

@login_required(login_url='login')
def accountSettings(request):

    # user_sister = Sister.objects.filter(user=request.user.username).first()
    # return render(request, 'accounts.html', {'user_sister': user_sister})
    # Get the username of the logged-in user
    username = request.user.username
    user = get_object_or_404(User, username=username)
    
    user_event = UserEvent.objects.filter(user=user).first()
    # context = {'user_event':user_event}
    # print(user_event) 
    # user_id = request.user.id
    
   
    # return render(request, 'events/account_settings.html',context)
    user= request.user
    user_event = None
    form = UserEventForm(instance=user)
   
    try:
        user_event = UserEvent.objects.get(user=user)
    except UserEvent.DoesNotExist:
        pass
    
    if request.method == 'POST':
        form = UserEventForm(request.POST, request.FILES, instance=user_event)
        if form.is_valid():
            form.save()

    context = {'user_event': user_event, 'form': form}
    return render(request, 'events/account_settings.html', context)

@login_required(login_url='login')
def addEvent(request):
    addevent_form = AddeventForm()

    if request.method == 'POST':
        if 'submit' in request.POST:
            addevent_form = AddeventForm(request.POST, request.FILES)
            if addevent_form.is_valid():
                addevent_form.instance.status = 'Pending'
                addevent_form.save()
                return redirect('eventsPage')
            else:
                form = EventForm()
                messages.success(request, 'New Event is created!!')
                # Retrieve the username of the currently logged-in user
                username = request.user.username
                return redirect('eventsPage')
    latest_event = Events.objects.order_by('-date_created').first()
    context = {'addevent_form': addevent_form, 'latest_event': latest_event}
    print(latest_event)
    return render(request, 'events/form.html', context)

@login_required
def regEvent(request):
    rgevent_form = partcipateForm()

    if request.method == 'POST':
        if 'rgevent' in request.POST:
            rgevent_form = partcipateForm(request.POST, request.FILES)
            if rgevent_form.is_valid():
                rgevent_instance = rgevent_form.save(commit=False)
                rgevent_instance.User = request.user
                rgevent_instance.status = 'Pending'
                rgevent_instance.save()
                messages.success(request, 'We got a new participant!!')
                return redirect('eventsPage')
    context = {'rgevent_form': rgevent_form}
    return render(request, 'events/partcipate.html', context)

@login_required
def submit_feedback(request, event_id):
    event = Events.objects.get(pk=event_id)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.event = event
            feedback.user = request.user
            feedback.save()
            return redirect('eventsPage')
    else:
        form = FeedbackForm()
    
    return render(request, 'events/submit_feedback.html', {'form': form, 'event': event})