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
    brand = models.ForeignKey(
        BrandsProcessor,
        null=True,
        on_delete=models.SET_NULL,
        related_name='processors'
    )

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.socket} - ' \
               f'{self.frequency} - {self.brand.name}'


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
    brand = models.ForeignKey(
        BrandsVideoCard,
        null=True,
        on_delete=models.SET_NULL,
        related_name='video_cards'
    )

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.size_memory} - ' \
               f'{self.frequency} - {self.brand.name}'


class Game(models.Model):
    name = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    memory = models.IntegerField()
    video_card_name = models.CharField(max_length=100)
    video_card_memory = models.IntegerField()

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.processor} - ' \
               f'{self.memory} - {self.video_card_name} - {self.video_card_memory}'
