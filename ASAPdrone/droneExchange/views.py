from django.shortcuts import render
from .forms import UserFootageForm, UserDetailsForm, EditDetailsForm, UserSearchForm, MessageForm
from django.views.generic import FormView, CreateView, UpdateView, ListView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login
from .models import UserFootage, Details, Message
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.template.response import TemplateResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


class UserFootageCreateView(CreateView):
    model = UserFootage
    form_class = UserFootageForm
    success_url ='main'
    #permission_required = 'droneExchange.add_userfootage'
    #raise_exception = True

    '''def handle_no_permission(self):
        if self.request.user.is_authenticated and self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())'''

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('main'))


class MainView(View):
    model = UserFootage
    template_name = 'droneExchange/main.html'

    def get(self, request):
        ctx = {
            'object_list': UserFootage.objects.all().order_by("-id"),
        }

        return render(request,'droneExchange/main.html', ctx)

'''
    def get_queryset(self):
        queryset = super().get_queryset()  # to na razie zadziała jak oryginana metoda
        queryset = queryset.filter(receiver_id=int(self.kwargs['student_id']))  # dobierz się do Id. poza tym kwargs to str
        return queryset

'''
'''
    class StudentNoticeDeleteView(DeleteView):
        model = StudentNotice

        def get_success_url(self):
            return reverse('student-notice-list', kwargs={
                'student_id': int(self.kwargs['student_id'])
            })

'''

class UserView(View):
    def get(self, request, pk):
        current_user = User.objects.get(pk=pk)
        if Details.objects.all().filter(person_id=pk).exists():
            details = Details.objects.get(person=current_user)
            return render(request, 'droneExchange/user_view.html', {
                'user': current_user,
                'details': details,
                'footage_list': UserFootage.objects.all().filter(author= pk)})
        else:
            return render(request, 'droneExchange/user_view.html', {
                'user': current_user,
                'footage_list': UserFootage.objects.all().filter(author= pk)})

class UserDetailsCreateView(LoginRequiredMixin, CreateView):
    model = Details
    form_class = UserDetailsForm
    # template_name = 'exercises/generic_form.html'
    #permission_required = 'droneExchange.add_details'
    raise_exception = True

    '''def handle_no_permission(self):
        if self.request.user.is_authenticated and self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())'''

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.person = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('/main/'))


class OldUserDetailsCreateView(View):
    def get(self, request, pk):
        #model = Details
        current_user = User.objects.get(id = pk)
        form = UserDetailsForm(instance=current_user)
        return render(request, 'droneExchange/details_form.html', {
            'form': form,
        })

    def post(self, request, pk):
        current_user = User.objects.get(id=pk)
        form = UserDetailsForm(instance=current_user, data=request.POST)

        def form_valid(self, form):
            obj = form.save(commit=False)
            obj.person = self.request.user
            obj.save()
            return HttpResponseRedirect(reverse('main'))



class DetailsUpdateView(UpdateView):
    model = Details
    form_class = EditDetailsForm
    success_url = 'main'

    def get_object(self):
        return self.request.user.details


class ConsoleView(View):

    def get(self, request, pk):

        current_user = User.objects.get(pk=pk)
        if Details.objects.all().filter(person_id=pk).exists():
            details = Details.objects.get(person=current_user)
            edit_details = 'edit details'
            cities = Details.objects.get(person_id=pk).cities.all()

            return render(request, 'droneExchange/user_console.html', {
                'user': current_user,
                'details': details,
                'edit_details': edit_details,
                'cities': cities,
            })

        else:
            add_details = 'add details'

            return render(request, 'droneExchange/user_console.html', {
                'user': current_user,
                'add_details': add_details,
            })

class UserSearchView(FormView):
    template_name = 'droneExchange/user_search_form.html'
    form_class = UserSearchForm

    def form_valid(self, form):
        city_name = form.cleaned_data['city']
        pricing = form.cleaned_data['maximum_price']
        filtered_details = Details.objects.filter(cities__name=city_name).filter(pricing__lt=pricing)

        return render(self.request, self.template_name, {
            'form': form,
            'details': filtered_details,
        })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/main/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class SendMessageView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'droneExchange/generic_form.html'
    #permission_required = 'droneExchange.add_details'
    raise_exception = True

    '''def handle_no_permission(self):
        if self.request.user.is_authenticated and self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())'''

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sender = self.request.user
        obj.receiver = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return HttpResponseRedirect(reverse('main'))


class MessagesView(ListView):
    model = Message

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            receiver=self.request.user)
        return queryset

class MessageDeleteView(DeleteView):
    model = Message

    def get_success_url(self):
        return reverse('messages')