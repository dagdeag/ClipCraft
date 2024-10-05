from gtts import gTTS
import os
file = open(r'ResultTTS\text.txt', 'r')
text = file.read()
def tts(text, name):
    # tts = gTTS(str(text), lang='en', tld='us')
    # tts.save(f'tts{output}')
    # print(f'saved to tts\{output}')
    outputPath = os.path.join('ResultTTS', name)

    tts = gTTS(text, lang='en', tld='us')
    tts.save(f'{outputPath}.mp3')

    print(f'Saved to {outputPath}')


nm = input('Name: ')
tts(text, nm)