from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^create-client/$', TemplateView.as_view(template_name="polls/create-client.html")),
    url(r'^confirm-addition$', views.ConfirmAddition, name='confirm_addition'),
    url(r'^confirm-page/$', views.ConfirmView, name='confirm_page'),
)