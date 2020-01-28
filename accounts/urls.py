from django.conf.urls import url, include
from accounts.views import logout, login, user_registartion, user_profile
from accounts import url_reset


urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', user_registartion, name='registration'),
    url(r'^profile/$', user_profile, name='profile'),
    url(r'^password_reset/', include(url_reset))
]