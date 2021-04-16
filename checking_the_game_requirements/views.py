from django.shortcuts import render

from checking_the_game_requirements.business_logic import filter_values, \
    check_proc, check_memory, check_video, proc_output, video_output
from checking_the_game_requirements.models import Game
from checking_the_game_requirements.forms import SearchForm


# Create your views here.


def display_main(request):
    context = {
        'form': SearchForm(),
    }
    if request.method == 'POST':
        data = SearchForm(request.POST)
        hardware = filter_values(data)
        games = Game.objects.all()
        game_name = []

        for game in games:

            results_processor = check_proc(game.processor_one.first().name, game.processor_two.first().name,
                                           hardware['processor'].name)
            results_memory = check_memory(game.memory, hardware['memory'].size_memory)
            results_video_card = check_video(game.video_card_one.first().name, game.video_card_two.first().name,
                                             hardware['video_card'].name)

            if results_processor == 'OK':
                if results_memory == 'OK':
                    if results_video_card == 'OK':
                        game_name += [game.name]

        result = {'games': game_name}

        return render(request, 'list_games_page.html', result)
    return render(request, 'main_page.html', context)


def list_games(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'games_page.html', context)


def check_game(request, my_id):
    game = Game.objects.get(pk=my_id)

    request.session['game_id'] = game.id
    request.session['processor_one'] = game.processor_one.first().name
    request.session['processor_two'] = game.processor_two.first().name
    request.session['memory'] = game.memory
    request.session['video_card_one'] = game.video_card_one.first().name
    request.session['video_card_two'] = game.video_card_two.first().name

    context = {'game': game,
               'form': SearchForm(),
               }
    return render(request, 'check_game.html', context)


def filter_components(request):
    game_id = request.session['game_id']
    processor_one = request.session.get('processor_one')
    processor_two = request.session.get('processor_two')
    memory = request.session.get('memory')
    video_card_one = request.session.get('video_card_one')
    video_card_two = request.session.get('video_card_two')

    if request.method == 'POST':
        data = SearchForm(request.POST)
        context = filter_values(data)

        game = Game.objects.get(pk=game_id)

        game_cpu = f'{proc_output(processor_two)} or {proc_output(processor_two)}'
        user_cpu = proc_output(context['processor'].name)

        game_gpu = f'{video_output(video_card_one)} or {video_output(video_card_two)}'
        user_gpu = context['video_card'].name

        results = {
            'Game': game.name,
            'GameCPU': game_cpu,
            'UserCPU': user_cpu,
            'GameRAM': memory,
            'UserRAM': context['memory'].size_memory,
            'GameGPU': game_gpu,
            'UserGPU': user_gpu,
            'CPU': (check_proc(processor_one, processor_two, context['processor'].name)),
            'RAM': (check_memory(memory, context['memory'].size_memory)),
            'GPU': (check_video(video_card_one, video_card_two, context['video_card'].name))
        }

        return render(request, 'results_page.html', results)
