# tests the result of the system on sample file

from scipy import signal
from scipy.io.wavfile import read
from evaluate import process_sound, load

# data path
path = './data/'

def test(path):
    # rate, sample = read('./vivos/vivos/train/waves/VIVOSSPK01/VIVOSSPK01_R003.wav')
    # rate, sample = read(path + 'test/test.wav')
    rate, sample = read("E:/Python/Voice/VietNamSpeech/data/test/test.wav")

    # E:\Python\Voice\VietNamSpeech\data\test
    _, _, spectrogram = signal.spectrogram(sample[:,0], rate)

    # print(sample[:,0].shape)

    print(''.join(process_sound(spectrogram, load(path))))
    return (''.join(process_sound(spectrogram, load(path))))

if __name__ == '__main__':
    test(path)