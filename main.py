import os
from gtts import gTTS
from pydub import AudioSegment
import pandas

def textToSpeech(text, filename):
    text = str(text)
    language = 'en'
    myobj = gTTS(text = text, lang = language)
    myobj.save(filename)

def mergeAudio(audios):
    combinied = AudioSegment.empty()
    for audio in audios:
        combinied += AudioSegment.from_mp3(audio)
    return combinied

def generateSkleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1 Generating may i have your attention please train number
    start = 18150
    finish = 23800
    audioProcessed = audio[start:finish]
    audioProcessed.export('1_english.mp3', format='mp3')

    # 2 tain number + train name

    # 3 Generating from
    start = 30000
    finish = 31000
    audioProcessed = audio[start:finish]
    audioProcessed.export('3_english.mp3', format='mp3')

    # 4 location name

    # 5 Generating to
    start = 31800
    finish = 32800
    audioProcessed = audio[start:finish]
    audioProcessed.export('5_english.mp3', format='mp3')

    # 6 destination name

    # 7 Generating via
    start = 33500
    finish = 34900
    audioProcessed = audio[start:finish]
    audioProcessed.export('7_english.mp3', format='mp3')

    # 8 via name

    # 9 Generating is arriving shortly on platform number
    start = 36200
    finish = 40500
    audioProcessed = audio[start:finish]
    audioProcessed.export('9_english.mp3', format='mp3')

    # 10 platform number

    # 11 last music
    start = 87000
    finish = 88600
    audioProcessed = audio[start:finish]
    audioProcessed.export('11_english.mp3', format='mp3')
 

def generateAnnouncement(filename):
    sd = pandas.read_excel(filename)
    print(sd)
    for index, item in sd.iterrows():
        # 2 train number and train name
        textToSpeech(item['train_no'] + "   " + item['train_name'], '2_english.mp3')

        # 4 from 
        textToSpeech(item['from'], '4_english.mp3')

        # 6 to
        textToSpeech(item['to'], '6_english.mp3')

        # 8 via
        textToSpeech(item['via'], '8_english.mp3')

        # 10 platform number
        textToSpeech(item['platform'], '10_english.mp3')

        audios = [f'{i}_english.mp3' for i in range(1, 12)]
        print(audios)

        announcement = mergeAudio(audios)
        announcement.export(f'announcement_{index+1}.mp3', format='mp3') 


if __name__ == "__main__":
    print('Generating Skeleton...')
    generateSkleton()
    print("Generating Announcement...")
    generateAnnouncement('announce_english.xlsx')