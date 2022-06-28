# Grazhdanskaya Oborona

This is a language model that generates lyrics of a song by title in the style of Yegor Letov. It is a transformer [ruGPT3Large](https://github.com/ai-forever/ru-gpts) tuned on 600+ texts of ["Grazhdanskaya Oborona"](https://www.gr-oborona.ru/).

## Project Structure

    .
    ├───config
    │   └───params.yaml             # configuration parameters
    ├───data
    │   ├───raw                     
    │   │   └───all_lyrics.xlsx     # excel file with all lyrics
    │   ├───processed
    │   │   ├───train.txt           # dataset for training
    │   │   └───val.txt             # dataset for validation
    │   └───model                   # weights and parameters for the GPT model
    ├───src                         
    │   ├───create_dataset.py       # creates the dataset and saves to /processed
    │   └───scrape.py               # scrapes lyrics from the website
    ├───.gitignore
    ├───generator.py                # contains class with the tuned model
    ├───inference.py                # example how the inference works
    ├───requirements.txt            # all required dependencies
    ├───song_lyrics.txt             # output text
    ├───song_title.txt              # input text
    ├───train.py                    # trains the model on the training dataset
    └───README.md

## How to use?

The device must have python and git. Commands are executed from the terminal.

1. Clone the repo — ```git clone https://github.com/armanbolatov/grob```, go to the repo and put the folder [`model`](https://disk.yandex.com/d/r84HKWAIuHI2nw) inside `/data` as shown in the structure;
2. Install all dependencies — `pip install -r requirements.txt`;
3. Change the song title in `song_title.txt`;
4. Run the inference — `python inference.py`; (If the device has a CUDA kernel, you should change the the keyword `use_cuda=True` when creating the object.)
5. Read the song from file `song_lyrics.txt`.