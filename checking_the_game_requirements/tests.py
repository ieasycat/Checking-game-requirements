from django.test import TestCase
from checking_the_game_requirements.business_logic import check_proc, \
    proc_output, video_output, check_memory, check_video
from checking_the_game_requirements.models import BrandsProcessor, \
    BrandsVideoCard, Processor, VideoCard, Game

# Create your tests here.


class TestLogic(TestCase):
    def setUp(self):
        BrandsProcessor.objects.create(
            name='AMD',
        )
        Processor.objects.create(
            name='Ryzen 5 2600',
            socket='AM4',
            frequency=3400,
            brand_id=1,
            benchmarking=13221,
        )
        BrandsVideoCard.objects.create(
            name='AMD',
        )
        VideoCard.objects.create(
            name='ASUS Mining Radeon RX 470 4GB GDDR5',
            size_memory=4,
            frequency=926,
            brand_id=1,
            benchmarking=7993,
        )

    def test_check_memory(self):
        ram = check_memory(8, 8)
        self.assertEqual(ram, 'OK')

    def test_check_proc(self):
        game_proc_one = game_proc_two = user_proc = 'Ryzen 5 2600'
        result = check_proc(game_proc_one, game_proc_two, user_proc)
        self.assertEqual(result, 'OK')

    def test_proc_output(self):
        result = proc_output('Ryzen 5 2600')
        self.assertEqual(result, 'AMD Ryzen 5 2600')

    def test_video_output(self):
        result = video_output('ASUS Mining Radeon RX 470 4GB GDDR5')
        self.assertEqual(result, 'AMD ASUS Mining Radeon RX 470 4GB GDDR5')

    def test_check_video(self):
        game_video_one = game_video_two = user_video = 'ASUS Mining Radeon RX 470 4GB GDDR5'
        result = check_video(game_video_one, game_video_two, user_video)
        self.assertEqual(result, 'OK')


class TestViews(TestCase):
    def setUp(self):
        BrandsProcessor.objects.create(
            name='AMD',
        )
        Processor.objects.create(
            name='Ryzen 5 2600',
            socket='AM4',
            frequency=3400,
            brand_id=1,
            benchmarking=13221,
        )
        BrandsVideoCard.objects.create(
            name='AMD',
        )
        VideoCard.objects.create(
            name='ASUS Mining Radeon RX 470 4GB GDDR5',
            size_memory=4,
            frequency=926,
            brand_id=1,
            benchmarking=7993,
        )
        game = Game.objects.create(
            name='Cyberpunk 2077',
            memory=8,
        )
        game.processor_one.add(Processor.objects.get(id=1))
        game.processor_two.add(Processor.objects.get(id=1))
        game.video_card_one.add(VideoCard.objects.get(id=1))
        game.video_card_two.add(VideoCard.objects.get(id=1))

    def test_main(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_list_games(self):
        result = self.client.get('/games')
        self.assertEqual(result.status_code, 200)

    def test_check_game(self):
        result = self.client.get('/check_game/1')
        self.assertEqual(result.status_code, 200)
