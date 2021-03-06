from django.urls import path
from . import views


# avoid namespace collisions
app_name = "mastergame"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add", views.add, name="add"),
    path("reset", views.reset, name="reset"),
    path("settings", views.settings, name="settings"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
]