from django import forms


PROCESSOR_CHOICES = (
    ('1', 'AMD Ryzen 5 2600'),
    ('2', 'AMD Ryzen 5 3600'),
    ('3', ' Intel i3-10100F'),
    ('4', ' Intel i5-7500'),
)

MEMORY_CHOICES = (
    ('1', 'Crucial Ballistix 2x8GB DDR4'),
    ('2', 'Crucial Ballistix Sport LT 4GB DDR4'),
    ('3', 'Corsair Vengeance LPX 4GB DDR4'),
    ('4', 'Corsair 16GB DDR4'),
)

VIDEO_CARD_CHOICES = (
    ('1', 'AMD ASUS Mining Radeon RX 470 4GB GDDR5'),
    ('2', 'AMD Gigabyte Radeon RX 5500 XT OC 4GB GDDR6'),
    ('3', 'NVIDIA MSI GeForce GTX 1650 Super Gaming X 4GB GDDR6'),
    ('4', 'NVIDIA Palit GeForce RTX 3060 Dual OC 12GB GDDR6'),
)


class SearchForm(forms.Form):
    processor = forms.ChoiceField(choices=PROCESSOR_CHOICES)
    memory = forms.ChoiceField(choices=MEMORY_CHOICES)
    video_card = forms.ChoiceField(choices=VIDEO_CARD_CHOICES)
