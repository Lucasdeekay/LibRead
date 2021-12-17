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
    path('login/forgot-password/<str:user>/retrieve-password', views.password_retrieval, name='password_retrieval'),
    path('login/forgot-password/<str:user>/retrieve-password/process', views.process_recovery_password,
         name='process_recovery_password'),
    path('login/forgot-password/<str:user>/retrieve-password/update-password', views.update_password,
         name='update_password'),
    path('login/forgot-password/<str:user>/retrieve-password/update-password/set-password', views.set_updated_password,
         name='set_updated_password'),
    path('admin/', views.library_admin, name='library_admin'),
    path('register', views.register, name='register'),
    path('register/process-registration', views.process_registration, name='process_registration'),
    path('repository', views.repository, name='repository'),
    path('repository/e-books', views.offline_resources, name='offline_resources'),
    path('logout', views.log_out, name='logout'),
    path('api/', include(router.urls))
]
