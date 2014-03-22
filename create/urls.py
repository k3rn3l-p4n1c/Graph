from django.conf.urls import patterns, url
<<<<<<< HEAD

from create import views

urlpatterns = patterns('',
    url(r'^/', views.create, name='create')
=======
from create import views

urlpatterns = patterns('',
    url(r'^$', views.create, name='create'),
         (r'^login/$', 
	 'django.contrib.auth.views.login', 
	 {'template_name': 'create/login.html'}),

	(r'^logout/$', 
	 'django.contrib.auth.views.logout', 
	 {'template_name': 'create/logged_out.html'}),

	(r'^password_change/$', 
	 'django.contrib.auth.views.password_change', 
	 {'template_name': 'create/password_change_form.html'}),

	(r'^password_change/done/$', 
	 'django.contrib.auth.views.password_change_done', 
	 {'template_name': 'create/password_change_done.html'}),

	(r'^password_reset/$', 
	 'django.contrib.auth.views.password_reset', 
	 {'template_name': 'create/password_reset_form.html',
	  'email_template_name': 'create/password_reset_email.html'}),

	(r'^password_reset/done/$', 
	 'django.contrib.auth.views.password_reset_done', 
	 {'template_name': 'create/password_reset_done.html'}),

	(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
	 'django.contrib.auth.views.password_reset_confirm', 
	 {'template_name': 'create/password_reset_confirm.html'}),

	(r'^reset/done/$', 
	 'django.contrib.auth.views.password_reset_complete', 
	 {'template_name': 'create/password_reset_complete.html'}),

	(r'^signup/$', 
	 'create.views.signup', 
	 {'template_name': 'create/signup_form.html',
	  'email_template_name': 'create/signup_email.html'}),

	(r'^signup/done/$', 
	 'create.views.signup_done', 
	 {'template_name': 'create/signup_done.html'}),

	(r'^signup/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
	 'create.views.signup_confirm'),

	(r'^signup/complete/$', 
	 'create.views.signup_complete', 
	 {'template_name': 'create/signup_complete.html'}),
	 
	 (r'^profile/$', 
	 'create.views.signed_in'),
	 
	 (r'^settings/$', 
	 'create.views.go_to_settings'),
	 
	 (r'^settings/saved$', 
	 'create.views.save_profile'),
	 
	 (r'^settings/cemail$', 
	 'create.views.change_email'),
                       
>>>>>>> 5446d8e9f93113a41fed678241a5478d2d6bf2d0
)
