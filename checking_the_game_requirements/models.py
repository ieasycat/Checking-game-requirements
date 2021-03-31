from django.db import models

# Create your models here.


class BrandsProcessor(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Processor(models.Model):
    name = models.CharField(max_length=50)
    socket = models.CharField(max_length=20)
    frequency = models.IntegerField()

    # check cpu.json 'cpumark'
    benchmarking = models.IntegerField(null=True)

    brand = models.ForeignKey(
        BrandsProcessor,
        null=True,
        on_delete=models.SET_NULL,
        related_name='processors'
    )

    def __str__(self):
        return f'{self.pk} - {self.brand.name} - {self.name} - ' \
               f'{self.socket} - {self.frequency} - {self.benchmarking}'


class BrandsMemory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Memory(models.Model):
    name = models.CharField(max_length=50)
    size_memory = models.IntegerField()
    type_memory = models.CharField(max_length=4)
    frequency = models.IntegerField()
    brand = models.ForeignKey(
        BrandsMemory,
        null=True,
        on_delete=models.SET_NULL,
        related_name='memory'
    )

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.size_memory} - ' \
               f'{self.type_memory} - {self.frequency} - {self.brand.name}'


class BrandsVideoCard(models.Model):
    name = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class VideoCard(models.Model):
    name = models.CharField(max_length=50)
    size_memory = models.IntegerField()
    frequency = models.IntegerField()

    # check gpu.json 'g3d'
    benchmarking = models.IntegerField(null=True)

    brand = models.ForeignKey(
        BrandsVideoCard,
        null=True,
        on_delete=models.SET_NULL,
        related_name='video_cards'
    )

    def __str__(self):
        return f'{self.pk} - {self.brand.name} - {self.name} - ' \
               f'{self.size_memory} - {self.frequency} - {self.benchmarking}'


class Game(models.Model):
    name = models.CharField(max_length=50)
    processor_one = models.ManyToManyField(
        'Processor',
        related_name='processor_one'
    )
    processor_two = models.ManyToManyField(
        'Processor',
        related_name='processor_two'
    )
    memory = models.IntegerField()
    video_card_one = models.ManyToManyField(
        'VideoCard',
        related_name='card_one'
    )
    video_card_two = models.ManyToManyField(
        'VideoCard',
        related_name='card_two'
    )

    def __str__(self):
        return f'{self.pk} - {self.name} - ' \
               f'{self.processor_one.first().brand.name} {self.processor_one.first().name} - ' \
               f'{self.processor_two.first().brand.name} {self.processor_two.first().name} - ' \
               f'{self.memory} - ' \
               f'{self.video_card_one.first().brand.name} {self.video_card_one.first().name} - ' \
               f'{self.video_card_two.first().brand.name} {self.video_card_two.first().name}'
