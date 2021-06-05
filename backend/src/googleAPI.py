import io
import os 

from google.cloud import speech
from IPython.display import Audio

def send_GG_API(filename):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'E:\Python\Voice\VietNamSpeech\My First Project-9cd31d857d6e.json'

    path = "./" + filename
    Audio(path)

    client = speech.SpeechClient()

    with io.open(path,'rb') as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content = content)

    config = speech.RecognitionConfig(
        encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='vi-VN',
        audio_channel_count=1,
        enable_word_time_offsets=True
    )  
    response = client.recognize(
        request={
            "config": config,
            "audio": audio,
        }
    )

    res = ""
    for result in response.results:
        res = res + '{}'.format(result.alternatives[0].transcript)
    return res




