import librosa
import numpy as np
import sys, os
import audioread
def buf_to_float(x, n_bytes=2, dtype = np.float32):
	scale = 1.#/float(1<<((8*n_bytes)-1))
	fmt = '<i{:d}'.format(n_bytes)
	return scale * np.frombuffer(x, fmt).astype(dtype)

def audioLoad(data_path, offset=0., duration=None):
	with audioread.audio_open(data_path) as data_file:
		n_channels = data_file.channels
		n_frames = data_file.nframes
		sr_native = data_file.samplerate
		duration = data_file.duration
	y, sr = librosa.load(data_path, sr=sr_native, offset=offset, duration=duration, mono=False)
	return y, sr

def extractFrames(nframes, window_size):
	start=0
	while start < len(data):
		yield int(start), int(start+window_size)
		start+=(window_size/2)

def extract_features(signal, band=60,feature='stft'):
	data=[]
	for i in xrange(nchannels):
		if feature=='logmel':
			melspec = librosa.feature.melspectrogram(signal, n_mels = bands)
			logspec = librosa.logamplitude(melspec)
			logspec = logspec.T.flatten()[:, np.newaxis].T
			log_specgrams.append(logspec)
		elif feature=='stft':
			for i in xrange(nchannels):
				stft_f = librosa.core.stft(signal[i,:], nfft=signal.shape[1])
				data.append(stft_f)
	data=np.vstack(data)
	return data
		


if __name__=='__main__':
	audioLoad(sys.argv[1])
