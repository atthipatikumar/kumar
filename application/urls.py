from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from application import views
#from .views import DetailView



urlpatterns = [
    #url(r'^user_details/', views.details_list),
    #url(r'^user/(?P<pk>[a-z0-9]+)/$', views.detail_view),

    url(r'^user_details/', views.details_list),
    url('user/(?P<pk>[a-zA-Z0-9]+)/$', views.detail_view),



]
urlpatterns = format_suffix_patterns(urlpatterns)

