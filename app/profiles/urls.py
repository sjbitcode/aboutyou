from django.conf.urls import url, patterns, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^success/$', views.success, name='success'),
	url(r'^all/$', views.ProfileList.as_view(), name='all'),
	url(r'^login/$', views.custom_login, name='custom_login'),
	url(r'^logout/$', views.custom_logout, name='custom_logout'),
	#url(r'^(?P<pk>\d+)/$', views.ProfileView.as_view(), name='profile_view')
	url(r'^(?P<slug>[-\w]+)/$', views.ProfileView.as_view(), name='profile_view'),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.profile_update, name='profile_update'),
    url(r'^(?P<slug>[-\w]+)/editform/$', views.ProfileUpdate.as_view(), name='profile_update_form'),
]