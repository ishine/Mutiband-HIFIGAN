import glob
import random

training_rate = 0.9999
val_rate = 0.0001


def find_files(path, pattren="*.wav"):
    filenames = []
    for filename in glob.iglob(f'{path}/**/*{pattren}', recursive=True):
        filenames.append(filename)
    return filenames


def create_metadata(path="datasets"):
    wav_lists = find_files(path=path)
    random.shuffle(wav_lists)
    train_num = int(len(wav_lists) * training_rate)
    train_lists = wav_lists[:train_num]
    val_lists = wav_lists[train_num:]
    with open("datasets/training.txt", 'w', encoding='utf-8') as w1:
        for i in train_lists:
            w1.write(f"{i}\n")
    with open("datasets/validation.txt", 'w', encoding='utf-8') as w2:
        for i in val_lists:
            w2.write(f"{i}\n")


if __name__ == '__main__':
    create_metadata()