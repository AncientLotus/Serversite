from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.sdtd, name='server-list-page'),

	url(r'^screenshots/$', views.screenshots, name='screenshots-page'),

    url(r'^whisperwind/$', views.whisperwind, name='whisperwind-main-page'),
    url(r'^whisperwind/rules', views.wwrules, name='whisperwind-rules-page'),
	url(r'^whisperwind/commands', views.wwcommands, name='whisperwind-commands-page'),
	url(r'^whisperwind/donations', views.wwdonations, name='whisperwind-donations-page'),

	url(r'^karazhan/$', views.karazhan, name='kara-main-page'),
    url(r'^karazhan/rules', views.kararules, name='karazhan-rules-page'),
	url(r'^karazhan/commands', views.karacommands, name='karazhan-commands-page'),
	url(r'^karazhan/donations', views.karadonations, name='karazhan-donations-page'),

	url(r'^lightbringer/$', views.lightbringer, name='lb-main-page'),
    url(r'^lightbringer/rules', views.lbrules, name='lightbringer-rules-page'),
	url(r'^lightbringer/commands', views.lbcommands, name='lightbringer-commands-page'),
	url(r'^lightbringer/donations', views.lbdonations, name='lightbringer-donations-page'),


]
