
from django.conf.urls import url

from . import views
# ...

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # 127.0.0.1/polls,

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # 127.0.0.1/polls/1

    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # 127.0.0.1/polls/2

    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # 127.0.0.1/polls/3/vote
]

