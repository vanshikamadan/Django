from django.conf.urls import url
from polls import views
from . import views
app_name = 'polls'
urlpatterns = [
      
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^your_name/$', views.get_name, name='name'), 

    url(r'^ajax/more/$', views.more_todo, name='name'),
 
    url(r'^display/$', views.info, name='name'),  
]
