from django.http import HttpResponse
from django.shortcuts import render

from checking_the_game_requirements.business_logic import filter_values, check_proc, check_memory, check_video
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

    request.session['processor'] = game('processor')[0]['processor'].split('/')
    request.session['memory'] = game('memory')[0]['memory']
    request.session['video_card_name'] = game('video_card_name')[0]['video_card_name'].split('/')
    request.session['video_card_memory'] = game('video_card_memory')[0]['video_card_memory']
    # request.session['video'] = game('video_card_name')[0]['video_card_name'].split('/')

    context = {'games': game,
               'form': SearchForm(),
               }
    return render(request, 'check_game.html', context)


def filter_components(request):
    processor = request.session.get('processor')
    memory = request.session.get('memory')
    video_card_name = request.session.get('video_card_name')
    video_card_memory = request.session.get('video_card_memory')
    # video = request.session.get('video')

    tmp = processor[0].split(' ')
    tmp2 = ' '.join(video_card_name[0].split(' ')[1:])

    # print(tmp)
    print(tmp2)
    print(video_card_memory)

    if request.method == 'POST':
        data = SearchForm(request.POST)
        context = filter_values(data)

        check_proc(tmp[5], context['processor'].name)
        check_memory(memory, context['memory'].size_memory)
        check_video(tmp2, context['video_card'])

        return HttpResponse(f"{context['processor']} - {context['memory']} - {context['video_card']}")
