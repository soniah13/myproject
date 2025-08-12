from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
# other URL patterns
path('subscribe/', views.subscribe, name='subscribe'),
path('add_pet/', views.add_pet, name='pets'),
path('pet_list/', views.pet_list, name='pet_list'),
path('log_in/', views.login_form, name='log_in'),
path('log_out/', views.logout_form, name='log_out'),
path('register/', views.register, name='register'),
path('api/add_books/', views.add_book, name='add_book'),
path('api/book_list/<int:pk>/', views.book_list, name="book_list"),

path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),

]