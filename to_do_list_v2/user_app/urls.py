from django.urls import path
from user_app import views
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

app_name = "user_app"

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    #not work - 405 ERR
    # path('logout/', LogoutView.as_view(next_page='user_app:login'), name="logout"),
    path('logout/', views.UserLogoutView.as_view(http_method_names = ['get', 'post', 'options']), name='logout'),
    path('register/', RegisterPage.as_view(), name="register"),
]
