
from django.urls import path
from .views import (HomeView, DetailsView,
                    NewContactView, ContactUpdateView,
                    ContactDeleteView, SignUpView)
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contacts/<int:pk>/details/',
         DetailsView.as_view(), name="contact-details"),
    path('contacts/create/',
         NewContactView.as_view(), name="new-contact"),
    path('contacts/<int:pk>/update/',
         ContactUpdateView.as_view(), name="update-contact"),
    path('contacts/<int:pk>/delete/',
         ContactDeleteView.as_view(), name="delete-contact"),
    path('signup/', SignUpView.as_view(), name="signup"),



    path('search/', views.search, name="search"),

]
