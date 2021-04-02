import model
import librosa
import os

path_name = "/home/minhhiu/MyProjects/Compressed Speech Data/full_command_data/test/wav/"

cmd_list = []
m = model.SpeechModel()
correct = 0
total = 0

with open("./model/cmd_list.txt", "r", encoding="utf8") as cmd_r:
    for i in range(71):
        cmd = cmd_r.readline()
        cmd = cmd.lower().strip("\n")
        cmd_list.append(cmd)

print(cmd_list)

for d in os.listdir(path_name):
    path = os.path.join(path_name, d)
    for file in os.listdir(path):
        wav_path = os.path.join(path, file)
        txt_path = wav_path.replace("wav", "txt")

        audio, _ = librosa.load(wav_path, sr=16000, mono=True)
        audio = audio.reshape(-1, 1)

        pred_index = m.predict(audio)

        with open(txt_path, "r", encoding="utf8") as fr:
            label = fr.read().strip("\n").lower()

        true_index = cmd_list.index(label)

        if pred_index == true_index:
            correct += 1

        total += 1

print(correct/total)

