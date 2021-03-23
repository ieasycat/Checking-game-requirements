from django.http import HttpResponse
from django.shortcuts import render

from checking_the_game_requirements.business_logic import filter_values
from checking_the_game_requirements.models import Game
from checking_the_game_requirements.forms import SearchForm


# Create your views here.


def display_main(request):
    return render(request, 'main_page.html')


def list_games(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'games_page.html', context)


def check_game(request, my_id):
    game = Game.objects.filter(pk=my_id).values
    # processor = game('processor')[0]['processor'].split('/')
    # memory = game('memory')[0]['memory']
    # video_card_name = game('video_card_name')[0]['video_card_name'].split('/')
    # video_card_memory = game('video_card_memory')[0]['video_card_memory']
    # video = game('video_card_name')[0]['video_card_name'].split('/')
    context = {'games': game,
               'form': SearchForm(),
               }
    return render(request, 'check_game.html', context)


def filter_components(request):
    if request.method == 'POST':
        data = SearchForm(request.POST)
        context = filter_values(data)
        return HttpResponse(f"{context['processor']} - {context['memory']} - {context['video_card']}")
