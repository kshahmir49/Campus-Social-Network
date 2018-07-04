from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done,  password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	

	url(r'^login/$', login, {'template_name': 'account/login.html'}, name ='login'),
	url(r'^logout/$', logout, {'template_name': 'account/logout.html'},
	 name ='logout' ),
	url(r'^aboutus/$', views.aboutus,{'template_name': 'account/aboutus.html'}, name='aboutus'),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.view_profile, name='view_profile'),
	url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
	url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	url(r'^change-password/', views.change_password, name='change_password'),

	url(r'^reset-password/$', password_reset,  {'template_name': 
		'account/reset_password.html','post_reset_redirect': 
		'account:password_reset_done', 'email_template_name': 'account/reset_password_email.html'},  name='password_reset'),
	

	url(r'^reset-password/done/$', password_reset_done, {'template_name': 
		'account/reset_password_done.html'},
	 name ='password_reset_done'),
	

	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
		password_reset_confirm, {'template_name': 
		'account/reset_password_confirm.html','post_reset_redirect': 
		'account:password_reset_complete'}, name='password_reset_confirm'),

	url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 
		'account/reset_password_complete.html'},  
		name='password_reset_complete')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
