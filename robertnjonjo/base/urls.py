from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('mywork/',views.projects,name='work'),
    path('mywork/<slug:slug>/',views.detail,name='detail'),
    path('create_project/', views.createProject, name="create_project"),
    path('update_project/<slug:slug>/', views.updateProject, name='update_project'),
	path('delete_project/<slug:slug>/', views.deleteProject, name='delete_project'),
    
    path('blogs/',views.blogs,name='blog'),
    path('blog/<slug:slug>/', views.post, name="blogs"),
    
    path('update_post/<slug:slug>/', views.updatePost, name="update_post"),
	path('delete_post/<slug:slug>/', views.deletePost, name="delete_post"),
 
    path('contact/',views.contact,name='contact'),
    path('create_post/', views.createPost, name="create_post"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    path('reset/',auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='email_sent.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),

	path('account/', views.userAccount, name="account"),
	path('update_profile/', views.updateProfile, name="update_profile"),
    
    path('reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    
    path('reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    
    path('reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
    path('__debug__/', include('debug_toolbar.urls')),
    
]