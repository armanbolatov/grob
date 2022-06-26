import yaml
from generator import LyricsGenerator

# грузим конфигурационные параметры
config = yaml.safe_load(open('config/params.yaml'))
model_path          = config['path']['model_write']
test_title_path     = config['path']['test_title']
test_lyrics_path    = config['path']['test_lyrics']

# загружаем генератор из директории model_path
lyrics_generator = LyricsGenerator(model_path, use_cuda=True)

# меняем один гиперпараметр
lyrics_generator.update_params(temperature=1.1)

# сохраняем название из файла в test_title в song_name
with open(test_title_path, "r", encoding="utf-8") as f:
    song_name = f.read().splitlines()[0]

# генерируем песню по названию song_name и сохраняем в test_lyrics
lyrics = lyrics_generator.generate(song_name)
with open(test_lyrics_path, "w", encoding="utf-8") as f:
    f.write(lyrics)