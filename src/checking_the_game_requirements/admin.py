from django.contrib import admin
from checking_the_game_requirements.models import BrandsMemory, BrandsProcessor, \
    BrandsVideoCard, Processor, Memory, VideoCard, Game

# Register your models here.

admin.site.register(BrandsMemory)
admin.site.register(BrandsProcessor)
admin.site.register(BrandsVideoCard)
admin.site.register(Processor)
admin.site.register(Memory)
admin.site.register(VideoCard)
admin.site.register(Game)
