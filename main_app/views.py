from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.views.generic import (CreateView, ListView,
                                  DetailView, DeleteView, UpdateView)
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


class HomeView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'index.html'
    context_object_name = 'contacts'


class DetailsView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = 'detail.html'
    context_object_name = 'contact'


class NewContactView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'new_contact.html'
    fields = ['name', 'email', 'phone',
              'designation', 'gender', 'group', 'image']

    success_url = '/'

    def form_valid(self, form):
        request = self.request
        request.manager = self.request.user
        form.save()
        messages.success(self.request, "New Contact is Created")

        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    template_name = 'contact_update.html'
    fields = ['name', 'email', 'phone',
              'designation', 'gender', 'group', 'image']

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, "Contact is Updated")
        return redirect('contact-details', instance.pk)

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.manager:
            return True
        return False


class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    template_name = 'contact_delete.html'
    success_url = '/'

    def delete(self, request, *args, **kewargs):
        messages.success(self.request, "Contact is successfully deleted")

        return super().delete(self, request, *args, **kewargs)

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.manager:
            return True
        return False


@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(designation__icontains=search_term) |
            Q(phone__iexact=search_term) |
            Q(group__iexact=search_term)
        )

        context = {
            'search_term': search_term,
            'contacts': search_results.filter(manager=request.user)
        }
        return render(request, 'search.html', context)

    else:
        return redirect('home')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    # def form_valid(self, form):
    #     res = super().form_valid(form)
    #     user = authenticate(
    #         username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
    #     if user is not None:
    #         if user.is_active:
    #             login(self.request, user)
    #     return res
