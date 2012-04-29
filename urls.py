from django.conf.urls.defaults import patterns, include, url
from django.views.generic import CreateView, ListView, DetailView, RedirectView
from wordbookviewer.models import WordBookEntry
from wordbookviewer.views import register, WordBookEntryCreationView, WordBookEntryUpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url="/words/")),
    url(r'^create_entry/$', WordBookEntryCreationView.as_view(template_name="wordbookviewer/wordbookentry_form.html")),
    url(r'^update_entry/(?P<pk>\d+)/$', WordBookEntryUpdateView.as_view(template_name="wordbookviewer/wordbookentry_update.html")),
    url(r'^words/$', ListView.as_view(model=WordBookEntry,queryset=WordBookEntry.objects.order_by('name'))),
    url(r'^words/(?P<pk>\d+)/$', DetailView.as_view(model=WordBookEntry)), 
    url(r'^register/$',register),
    url(r'^login/$',login),
    url(r'^logout/$',logout,{'next_page': '/'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
