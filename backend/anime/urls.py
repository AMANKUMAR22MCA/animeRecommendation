from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    RegisterView,
    search_anime_view,
    user_preferences,
    anime_recommendations_view,
)

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User-specific endpoints
    path('user/preferences/', user_preferences, name='user_preferences'),

    # Anime endpoints
    path('anime/search/', search_anime_view, name='anime_search'),
    path('anime/recommendations/', anime_recommendations_view, name='anime_recommendations'),
]
