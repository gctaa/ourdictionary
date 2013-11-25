from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from wordviewer.models import WordEntry, SitePreferences, Dictionary
from django.core.exceptions import ValidationError

class WordEntryForm(forms.ModelForm):
    class Meta:
       model = WordEntry
       exclude = ("user_creator", "user_last_modified", "dictionary")

    def clean(self):
        cleaned_data = super(WordEntryForm, self).clean()
        if self.is_valid():
            return cleaned_data
        return  HttpResponseRedirect("wordviewer/wordentry_form.html")
             
class WordEntryCreationView(CreateView):
    form_class = WordEntryForm
    dictionary = ''
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
            return super(WordEntryCreationView, self).dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(WordEntryCreationView, self).get_context_data(**kwargs)
        if WordEntryCreationView.dictionary == '':
            context["dictionary"] = get_object_or_404(Dictionary, pk=self.request.META['HTTP_REFERER'].split('/')[4])
            WordEntryCreationView.dictionary = context["dictionary"]
            return context
        else:
            return context

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user_creator = self.request.user
        object.user_last_modified = self.request.user
        object.dictionary = WordEntryCreationView.dictionary
        object.save()
        WordEntryCreationView.dictionary = ''
        return HttpResponseRedirect("/dictionaries/" + str(object.dictionary.id) + "/words/")

class WordEntryUpdateView(UpdateView):
    model = WordEntry
    form_class = WordEntryForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WordEntryUpdateView, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user_last_modified = self.request.user
        object.save()
        return HttpResponseRedirect("/dictionaries/" + str(object.dictionary.id) + "/words/")

class WordEntryDeletionView(DeleteView):
    model = WordEntry
    success_url = "/dictionaries/"

    @method_decorator(permission_required('wordviewer.delete_entry'))
    def dispatch(self, *args, **kwargs):
        return super(WordEntryDeletionView, self).dispatch(*args, **kwargs)

class WordListView(ListView):
    model = WordEntry

    def get_context_data(self, **kwargs):
        context = super(WordListView, self).get_context_data(**kwargs)
        context["dictionary"] = get_object_or_404(Dictionary, pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return WordEntry.objects.filter(dictionary_id=self.kwargs['pk'])

class UserListView(ListView):
    model = User

    @method_decorator(permission_required('wordviewer.view_users'))
    def dispatch(self, *args, **kwargs):
        return super(UserListView, self).dispatch(*args, **kwargs)

class UserProfileView(DetailView):
    model = User
    slug_field = 'username'

    @method_decorator(permission_required('wordviewer.view_users'))
    def dispatch(self, *args, **kwargs):
        return super(UserProfileView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context["user_word_entries"] = WordEntry.objects.filter(user_creator=self.object).order_by("-date_created")
        return context


class RichUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last name")

    def save(self, commit=True):
        user = super(RichUserCreationForm, self).save(commit=False)
        first_name =self.cleaned_data["first_name"]
        last_name =self.cleaned_data["last_name"]
        user.first_name = first_name
        user.last_name = last_name
        if commit:
            user.save()
        return user

class TokenRegistrationForm(RichUserCreationForm):
    token = forms.CharField(max_length=20, label="Registration Token")
    def clean_token(self):
        data = self.cleaned_data["token"]
        if data != settings.REGISTRATION_TOKEN:
            raise forms.ValidationError("Incorrect Registration Token!")
        return data


class SitePreferencesUpdateView(UpdateView):
    template_name = 'wordviewer/admin/sitepreferences_form.html'
   
    def get_object(self):
        object = SitePreferences.objects.get(id=1)
        return object

    @method_decorator(permission_required('wordviewer.change_sitepreferences'))
    def dispatch(self, *args, **kwargs):
        return super(SitePreferencesUpdateView, self).dispatch(*args, **kwargs)


def site_preferences(request):
    return {'preferences': SitePreferences.objects.get(id=1),}

def register(request):
    if request.method == 'POST':
        if settings.REGISTRATION_TOKEN:
           form = TokenRegistrationForm(request.POST)
        else:
           form = RichUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        if settings.REGISTRATION_TOKEN:
            form = TokenRegistrationForm()
        else:
            form = RichUserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    }, context_instance=RequestContext(request))
    
class DictionaryForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        exclude = ("owner")

class DictionaryCreationView(CreateView):
    form_class = DictionaryForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DictionaryCreationView, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return HttpResponseRedirect("/dictionaries/")

