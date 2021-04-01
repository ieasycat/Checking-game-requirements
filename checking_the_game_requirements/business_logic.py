from checking_the_game_requirements.models import Processor, Memory, VideoCard


def filter_values(data):
    if data.is_valid():
        cleaned_data = data.cleaned_data
        clean = cleaned_data.get

        processor_search = clean('processor')
        memory_search = clean('memory')
        video_card_search = clean('video_card')

        processor_filter = Processor.objects.filter(id=processor_search)
        memory_filter = Memory.objects.filter(id=memory_search)
        video_card_filter = VideoCard.objects.filter(id=video_card_search)

        context = {'processor': processor_filter[0],
                   'memory': memory_filter[0],
                   'video_card': video_card_filter[0],
                   }
        return context


def check_proc(game_proc_one, game_proc_two, user_proc):
    game_processor_one = Processor.objects.filter(name=game_proc_one)
    game_processor_two = Processor.objects.filter(name=game_proc_two)

    user_processor = Processor.objects.filter(name=user_proc)

    if game_processor_one[0] == user_processor[0] \
            or game_processor_two[0] == user_processor[0]:
        return 'OK'
    else:
        if game_processor_one[0].benchmarking <= user_processor[0].benchmarking \
                or game_processor_two[0].benchmarking <= user_processor[0].benchmarking:
            return 'OK'
        else:
            return 'NO'


def proc_output(processor):
    proc = Processor.objects.filter(name=processor)
    return f'{proc[0].brand.name} {proc[0].name}'


def video_output(video_card):
    video = VideoCard.objects.filter(name=video_card)
    return f'{video[0].brand.name} {video[0].name}'


def check_memory(game_mem, user_mem):
    if game_mem <= user_mem:
        return 'OK'
    else:
        return 'NO'


def check_video(game_video_one, game_video_two, user_video):
    game_video_card_one = VideoCard.objects.filter(name=game_video_one)
    game_video_card_two = VideoCard.objects.filter(name=game_video_two)
    user_video_card = VideoCard.objects.filter(name=user_video)

    if user_video_card == game_video_card_one or user_video_card == game_video_card_two:
        return 'OK'
    else:
        if user_video_card[0].benchmarking >= game_video_card_one[0].benchmarking \
                or user_video_card[0].benchmarking >= game_video_card_two[0].benchmarking:
            return 'OK'
        else:
            return 'NO'
