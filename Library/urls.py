from django.urls import path, include
from rest_framework import routers

from Library import views
from Library.api_views import ClienteleView, PasswordView, EbookView, JournalView, LibraryFileView

app_name = 'Library'

router = routers.DefaultRouter()
router.register('clientele', ClienteleView)
router.register('password', PasswordView)
router.register('ebook', EbookView)
router.register('journal', JournalView)
router.register('library-file', LibraryFileView)

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.log_in, name='login'),
    path('login/forgot-password', views.forgotten_password, name='forgot_password'),
    path('login/forgot-password/<int:clientele_id>/retrieve-password', views.password_retrieval, name='password_retrieval'),
    path('account/<int:clientele_id>/retrieve-password/update-password', views.update_password, name='update_password'),
    path('admin/', views.library_admin, name='library_admin'),
    path('admin/approve-clientele/<int:clientele_id>', views.approve_clientele, name='approve_clientele'),
    path('admin/reject-clientele/<int:clientele_id>', views.reject_clientele, name='reject_clientele'),
    path('admin/approve-journal/<int:journal_id>', views.approve_journal, name='approve_journal'),
    path('admin/reject-journal/<int:journal_id>', views.reject_journal, name='reject_journal'),
    path('register', views.register, name='register'),
    path('account/update-profile-image', views.update_profile_image, name='update_profile_image'),
    path('account/repository', views.repository, name='repository'),
    path('account/logout', views.log_out, name='logout'),
    path('api/', include(router.urls))
]
