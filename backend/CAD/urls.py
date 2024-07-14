# urls.py

from django.urls import path
from . import views

app_name = 'CAD'

urlpatterns = [
    path('',views.live_matches,name='live_matches'),
    path('index/',views.home,name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    # path('live-matches/', views.live_matches, name='live_matches'),
    path('scorecard/<uuid:match_id>', views.match_details, name='match_details'),
    # path('scorecard/<uuid:match_id>/', views.view_scorecard, name='view_scorecard'),
    path('predict/', views.predict_victory, name='predict_victory'),
]
