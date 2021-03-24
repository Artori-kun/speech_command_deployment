import numpy as np
import json
import tensorflow as tf
from python_speech_features import mfcc
from difflib import SequenceMatcher
import time
import textdistance


class SpeechModel:
    def __init__(self):
        with open("./model/encode_decode.json", "r") as load_label:
            self.label_dic = json.load(load_label)
            self.encode_dic = self.label_dic["encode"]

        with open("./model/normalize_param.json", "r") as normalize:
            nor_param = json.load(normalize)
            self.mean = np.array(nor_param["mean"])
            self.sqrt = np.array(nor_param["sqrt"])

        with tf.compat.v1.gfile.FastGFile("./model/lstm_model_2021-02-25-full.pb", 'rb') as f:
            self.graph_def = tf.compat.v1.GraphDef()
            self.graph_def.ParseFromString(f.read())
            tf.import_graph_def(self.graph_def, name='')

        self.sess = tf.compat.v1.Session()

        with open("./model/cmd_list.txt", "r", encoding="utf8") as cmd_list:
            self.cmd_list = []
            for i in range(70):
                cmd = cmd_list.readline()
                cmd = cmd.lower()
                self.cmd_list.append(cmd)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_key(self, val):
        for key, value in self.encode_dic.items():
            if val == value:
                return key
        return ''

    def predict(self, input_wav):
        start = time.time()
        inputs = mfcc(input_wav, samplerate=16000, winlen=0.025, winstep=0.01, numcep=39, nfilt=40)

        # inputs = (inputs - self.mean) / self.sqrt

        wav_inputs = np.expand_dims(inputs, axis=0)
        data_len = np.array([len(inputs)])
        data_len = np.asarray([data_len[0]])

        y = self.sess.graph.get_tensor_by_name('SparseToDense:0')

        labels = self.sess.run(y, feed_dict={'InputData:0': wav_inputs, 'SeqLen:0': data_len})

        str_decoded = ''.join([self.get_key(x) for x in labels[0]])
        # Replacing blank label to none
        str_decoded = str_decoded.replace(self.get_key(self.label_dic["char_num"]), '')
        # Replacing space label to space
        str_decoded = str_decoded.replace(self.get_key(0), ' ')

        # match = [SequenceMatcher(None, str_decoded, cmd).ratio() for cmd in self.cmd_list]
        # best_match = max(match)
        # end = time.time()
        # print(end - start)
        #
        # print(str_decoded)
        # if best_match < 0.8:
        #     return "Non match"
        # else:
        #     return match.index(best_match)
        levenshtein = textdistance.Levenshtein(external=True)
        distances = [levenshtein.normalized_distance(str_decoded, cmd) for cmd in self.cmd_list]

        best_match = min(distances)

        print("Min distance: " + str(best_match))

        end = time.time()
        print(end - start)
        print(str_decoded)

        if best_match > 0.4:
            return -1
        else:
            return distances.index(best_match)
