from checking_the_game_requirements.forms import PROCESSOR_CHOICES, MEMORY_CHOICES, VIDEO_CARD_CHOICES
from checking_the_game_requirements.models import Processor, Memory, VideoCard


def filter_values(data):
    if data.is_valid():
        cleaned_data = data.cleaned_data
        clean = cleaned_data.get

        processor_search = clean('processor')
        memory_search = clean('memory')
        video_card_search = clean('video_card')

        processor = dict(PROCESSOR_CHOICES).get(processor_search)
        memory = dict(MEMORY_CHOICES).get(memory_search)
        video_card = dict(VIDEO_CARD_CHOICES).get(video_card_search)

        processor = ' '.join(processor.split(' ')[1:])
        memory = ' '.join(memory.split(' ')[1:])
        video_card = ' '.join(video_card.split(' ')[1:])

        processor_filter = Processor.objects.filter(name=processor)
        memory_filter = Memory.objects.filter(name=memory)
        video_card_filter = VideoCard.objects.filter(name=video_card)

        context = {'processor': processor_filter[0],
                   'memory': memory_filter[0],
                   'video_card': video_card_filter[0],
                   }
        return context


def check_proc(game_proc, user_proc):
    game_processor = Processor.objects.filter(name=game_proc)

    user_processor = Processor.objects.filter(name=user_proc)

    print(f"2 {game_processor[0].frequency}")
    print(f"2 {user_processor[0].frequency}")

    if game_processor[0] == user_processor[0]:
        print('WOW')
    else:
        if game_processor[0].frequency <= user_processor[0].frequency:
            print('Yes')
        else:
            print('No')


def check_memory(game_mem, user_mem):
    if game_mem <= user_mem:
        print('Yes')
    else:
        print('No')


def check_video(game_video, user_video):
    # game_video_card = VideoCard.objects.filter(name=game_video)
    game_video_card = list_video(game_video)
    user_video_card = list_video(user_video.name)
    # user_video_card = VideoCard.objects.filter(name=user_video)

    print('check_one', game_video, user_video.name)
    print(game_video_card)

    print(user_video_card)


def list_video(video_card):
    print('list', video_card)
    video_cards = VideoCard.objects.all()
    for video in range(len(video_cards)):
        if f'{video_card}' in video_cards[video].name:
            return video_cards[video]
