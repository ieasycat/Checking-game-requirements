from checking_the_game_requirements.forms import PROCESSOR_CHOICES, MEMORY_CHOICES, VIDEO_CARD_CHOICES
from checking_the_game_requirements.models import Processor, Memory, VideoCard, Game


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


def check(game_proc, user_proc):
    game_processor = Processor.objects.filter(name=game_proc)
    game_memory = []
    game_video_card = []

    user_processor = Processor.objects.filter(name=user_proc)
    user_memory = []
    user_video_card = []

    print(game_proc, user_proc)

    print(f"2 {user_processor}")
    print(f"2 {game_processor}")

    if game_proc == user_proc:
        print('WOW')

    return game_processor
