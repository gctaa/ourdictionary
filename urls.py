from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic import CreateView, ListView, DetailView, RedirectView
from wordviewer.models import WordEntry
from wordviewer.views import (register, WordEntryCreationView,
    WordEntryUpdateView, UserListView, UserProfileView, SitePreferencesUpdateView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.contrib.auth.models import User

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url="/words/")),
    url(r'^create_entry/$', WordEntryCreationView.as_view(template_name="wordviewer/wordentry_form.html")),
    url(r'^update_entry/(?P<pk>\d+)/$', WordEntryUpdateView.as_view(template_name="wordviewer/wordentry_update.html")),
    url(r'^words/$', ListView.as_view(model=WordEntry, queryset=WordEntry.objects.order_by('name'))),
    url(r'^words/(?P<pk>\d+)/$', DetailView.as_view(model=WordEntry)), 
    url(r'^register/$', register),
    url(r'^login/$', login),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^users/$', UserListView.as_view(queryset=User.objects.order_by('last_name'), template_name="wordviewer/user_list.html")),
    url(r'^users/(?P<slug>\w+)/$', UserProfileView.as_view(template_name="wordviewer/user_detail.html")),
    url(r'^sitepreferences/$', SitePreferencesUpdateView.as_view(success_url="/words/")),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
