"""ASAPdrone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from droneExchange import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout/$', auth_views.logout, {'next_page': ('next','/')}, name='logout'),
    #url(r'^add-footage/$', views.UserFootageCreateView.as_view(), name='add-footage'),
    url(r'^add_footage/$', views.UserFootageCreateView.as_view(), name='add-footage'),
    url(r'^accounts/', admin.site.urls),
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^user/(?P<pk>(\d)+)/$', views.UserView.as_view(), name='user-details'),
    url(r'^user/(?P<pk>(\d)+)/add_details/$', views.UserDetailsCreateView.as_view(), name='user-add-details'),
    url(r'^user/(?P<pk>(\d)+)/update_details/$', views.DetailsUpdateView.as_view(), name='user-update-details'),
    #url(r'^user/update_details/$', views.DetailsUpdateView.as_view(), name='user-update-details'),
    url(r'^console/(?P<pk>(\d)+)/$', views.ConsoleView.as_view(), name='console'),
    url(r'^search/$', views.UserSearchView.as_view(), name='search'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^message/(?P<pk>(\d)+)/$', views.SendMessageView.as_view(), name='message'),
    url(r'^messages/$', views.MessagesView.as_view(), name='messages'),
    url(r'^delete-message/(?P<pk>(\d)+)', views.MessageDeleteView.as_view(),
        name='delete-message'),
    url(r'^reply/(?P<pk>(\d)+)/$', views.ReplyView.as_view(), name='reply'),
    url(r'^footage-delete/(?P<pk>(\d)+)/$', views.FootageDeleteView.as_view(), name='delete-footage'),
    url(r'^edit-footage/(?P<pk>(\d)+)', views.FootageUpdateView.as_view(), name="edit-footage"),
    url(r'^recommend/(?P<pk>(\d)+)/$', views.RecommendView.as_view(), name='recommend'),

]
