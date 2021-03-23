import model
import librosa

file_name = "/home/minhhiu/MyProjects/Compressed Speech Data/full_command_data/test/wav/54/rec_8.wav"

audio, _ = librosa.load(file_name, sr=16000, mono=True)
audio = audio.reshape(-1, 1)
print(audio.shape)

m = model.SpeechModel()

print(m.predict(audio))

