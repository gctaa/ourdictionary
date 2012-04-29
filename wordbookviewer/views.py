from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from wordbookviewer.models import WordBookEntry

class WordBookEntryForm(forms.ModelForm):
    class Meta:
       model = WordBookEntry
       exclude = ("user_creator","user_last_modified")
    
class WordBookEntryCreationView(CreateView):
    
    form_class = WordBookEntryForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WordBookEntryCreationView, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user_creator = self.request.user
        object.user_last_modified = self.request.user
        object.save()
        return HttpResponseRedirect("/words/")

class WordBookEntryUpdateView(UpdateView):
    model = WordBookEntry
    form_class = WordBookEntryForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WordBookEntryUpdateView, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user_last_modified = self.request.user
        object.save()
        return HttpResponseRedirect("/words/")

class TokenRegistrationForm(UserCreationForm):
    token = forms.CharField(max_length=20,label="Registration Token")
    def clean_token(self):
        data = self.cleaned_data["token"]
        if data != "hilt_institute":
            raise forms.ValidationError("Incorrect Registration Token!")
        return data
            
def register(request):
    if request.method == 'POST':
        form = TokenRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = TokenRegistrationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    },context_instance=RequestContext(request))
