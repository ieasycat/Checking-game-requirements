from django.urls import path
from checking_the_game_requirements.views import list_games, check_game, display_main, filter_components

urlpatterns = [
    path('main', display_main, name='display_main'),
    path('games', list_games, name='list_games'),
    path('check_game/<int:my_id>', check_game, name='check_game'),
    path('filter_components>', filter_components, name='filter_components'),
]
