from django.urls import path, include
from rest_framework import routers

from Library import views
from Library.api_views import ClienteleView, PasswordView, EbookView, JournalView

app_name = 'Library'

router = routers.DefaultRouter()
router.register('clientele', ClienteleView)
router.register('password', PasswordView)
router.register('ebook', EbookView)
router.register('journal', JournalView)

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.log_in, name='login'),
    path('login/process-login', views.process_login, name='process_login'),
    path('login/forgot-password', views.forgotten_password, name='forgot_password'),
    path('login/forgot-password/send-recovery-pin', views.send_recovery_pin, name='send_recovery_pin'),
    path('login/forgot-password/<int:clientele_id>/retrieve-password', views.password_retrieval, name='password_retrieval'),
    path('login/forgot-password/<int:clientele_id>/retrieve-password/process', views.process_recovery_password, name='process_recovery_password'),
    path('account//<int:clientele_id>/retrieve-password/update-password', views.update_password, name='update_password'),
    path('account/<int:clientele_id>/retrieve-password/update-password/set-password', views.set_updated_password, name='set_updated_password'),
    path('admin/', views.library_admin, name='library_admin'),
    path('admin/upload-ebook', views.upload_ebook, name='upload_ebook'),
    path('admin/upload-journal', views.upload_journal, name='upload_journal'),
    path('admin/upload-blog', views.upload_blog, name='upload_blog'),
    path('admin/approve-clientele/<str:clientele_id>', views.approve_clientele, name='approve_clientele'),
    path('admin/reject-clientele/<str:clientele_id>', views.reject_clientele, name='reject_clientele'),
    path('admin/approve-journal/<str:journal_id>', views.approve_journal, name='approve_journal'),
    path('admin/reject-journal/<str:journal_id>', views.reject_journal, name='reject_journal'),
    path('register', views.register, name='register'),
    path('register/process-registration', views.process_registration, name='process_registration'),
    path('account/repository', views.repository, name='repository'),
    path('account/upload-image', views.upload_image, name='upload_image'),
    path('account/update-profile-image', views.update_profile_image, name='update_profile_image'),
    path('account/repository/e-books', views.offline_resources, name='offline_resources'),
    path('account/logout', views.log_out, name='logout'),
    path('api/', include(router.urls))
]
