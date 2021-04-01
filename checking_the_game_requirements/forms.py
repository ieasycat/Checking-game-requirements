from django import forms
from checking_the_game_requirements.models import Processor, Memory, VideoCard


PROCESSOR_CHOICES = ((i.id, f'{i.brand.name + " " + i.name}') for i in Processor.objects.all())


MEMORY_CHOICES = ((i.id, f'{i.brand.name + " " + i.name}') for i in Memory.objects.all())

VIDEO_CARD_CHOICES = ((i.id, f'{i.brand.name + " " + i.name}') for i in VideoCard.objects.all())


class SearchForm(forms.Form):
    processor = forms.ChoiceField(choices=PROCESSOR_CHOICES)
    memory = forms.ChoiceField(choices=MEMORY_CHOICES)
    video_card = forms.ChoiceField(choices=VIDEO_CARD_CHOICES)
