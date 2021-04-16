from checking_the_game_requirements.models import Processor, Memory, VideoCard


def filter_values(data):
    if data.is_valid():
        cleaned_data = data.cleaned_data
        clean = cleaned_data.get

        processor_search = clean('processor')
        memory_search = clean('memory')
        video_card_search = clean('video_card')

        processor_filter = Processor.objects.get(id=processor_search)
        memory_filter = Memory.objects.get(id=memory_search)
        video_card_filter = VideoCard.objects.get(id=video_card_search)

        context = {'processor': processor_filter,
                   'memory': memory_filter,
                   'video_card': video_card_filter,
                   }
        return context


def check_proc(game_proc_one, game_proc_two, user_proc):
    game_processor_one = Processor.objects.get(name=game_proc_one)
    game_processor_two = Processor.objects.get(name=game_proc_two)

    user_processor = Processor.objects.get(name=user_proc)

    if game_processor_one == user_processor \
            or game_processor_two == user_processor:
        return 'OK'
    else:
        if game_processor_one.benchmarking <= user_processor.benchmarking \
                or game_processor_two.benchmarking <= user_processor.benchmarking:
            return 'OK'
        else:
            return 'NO'


def proc_output(processor):
    proc = Processor.objects.get(name=processor)
    return f'{proc.brand.name} {proc.name}'


def video_output(video_card):
    video = VideoCard.objects.get(name=video_card)
    return f'{video.brand.name} {video.name}'


def check_memory(game_mem, user_mem):
    if game_mem <= user_mem:
        return 'OK'
    else:
        return 'NO'


def check_video(game_video_one, game_video_two, user_video):
    game_video_card_one = VideoCard.objects.get(name=game_video_one)
    game_video_card_two = VideoCard.objects.get(name=game_video_two)
    user_video_card = VideoCard.objects.get(name=user_video)

    if user_video_card == game_video_card_one or user_video_card == game_video_card_two:
        return 'OK'
    else:
        if user_video_card.benchmarking >= game_video_card_one.benchmarking \
                or user_video_card.benchmarking >= game_video_card_two.benchmarking:
            return 'OK'
        else:
            return 'NO'
