# _*_ coding: utf8 _*_
# 마지막 어절을 추출
import numpy as np
from konlpy.tag import Komoran

N_LAST_WORDS = 1
DEV_COUNT = 100
TEST_COUNT = 100


def write_data(filename, data_arr):
    src_writer = open(filename+".src", "w")
    tgt_writer = open(filename+".tgt", "w")
    for data in data_arr:
        src_writer.write(data[0]+"\n")
        tgt_writer.write(data[1]+"\n")


def split_dataset(data_list):
    data_arr = np.asarray(data_list)
    np.random.shuffle(data_arr)

    dev_arr = data_arr[:DEV_COUNT]
    test_arr = data_arr[DEV_COUNT:DEV_COUNT + TEST_COUNT]
    train_arr = data_arr[DEV_COUNT + TEST_COUNT:]

    return train_arr, dev_arr, test_arr


src_file = open("data/last_src_words.txt", "r")
tgt_file = open("data/last_tgt_words.txt", "r")
komoran = Komoran()

chars_list = []
for src_line, tgt_line in zip(src_file.readlines(), tgt_file.readlines()):
    src_morph = "*".join(komoran.morphs(src_line.strip()))
    tgt_morph = "*".join(komoran.morphs(tgt_line.strip()))
    src_chars = [ch for ch in src_morph.strip()]
    tgt_chars = [ch for ch in tgt_morph.strip()]

    chars_list += [(" ".join(src_chars), " ".join(tgt_chars))]

src_file.close()
tgt_file.close()

train_arr, dev_arr, test_arr = split_dataset(chars_list)

write_data("data/train.morph_chars", train_arr)
write_data("data/dev.morph_chars", dev_arr)
write_data("data/test.morph_chars", test_arr)
