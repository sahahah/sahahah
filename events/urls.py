from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('homepage/', views.home, name="home"),
    path('acc/', views.userPage, name="user-page"),
    path('events/', views.events,name='events'),
    path('user/<str:pk_test>/', views.user,name='user'),
   
    path('create_event/<str:pk>/', views.createEvent, name="create_event"),
    path('update_event/<str:pk>/', views.updateEvent, name="update_event"),
    path('delete_event/<str:pk>/', views.deleteEvent, name="delete_event"),


    path('', views.homePage, name="homePage"),
    path('eventspage/', views.eventsPage, name="eventsPage"),
    path('clubpage/', views.clubPage, name="clubPage"),
    path('account/', views.accountSettings, name="accountSettings"),
    path('addevent/', views.addEvent, name="addEvent"),
    path('regevent/', views.regEvent, name="regEvent"),
    path('evre/<int:event_id>/', views.Evre, name="Evre"),
    path('events/<int:event_id>/feedback/', views.submit_feedback, name='submit_feedback'),
    
    path('reset_password/' , auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    

    ]