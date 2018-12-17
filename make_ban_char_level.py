# _*_ coding: utf8 _*_
import numpy as np

DEV_COUNT = 100
TEST_COUNT = 100


def write_data(filename, data_arr):
    sho_writer = open(filename+".sho", "w")
    yo_writer = open(filename+".yo", "w")
    ban_writer = open(filename+".ban", "w")

    for data in data_arr:
        sho_writer.write(data[0]+"\n")
        yo_writer.write(data[1]+"\n")
        ban_writer.write(data[2]+"\n")


def split_dataset(data_list):
    data_arr = np.asarray(data_list)
    np.random.shuffle(data_arr)

    dev_arr = data_arr[:DEV_COUNT]
    test_arr = data_arr[DEV_COUNT:DEV_COUNT + TEST_COUNT]
    train_arr = data_arr[DEV_COUNT + TEST_COUNT:]
    train_close_arr = data_arr

    return train_close_arr, train_arr, dev_arr, test_arr


sho_file = open("data/raw/keti_sho_words.txt", "r")
yo_file = open("data/raw/keti_yo_words.txt", "r")
ban_file = open("data/raw/keti_ban_words.txt", "r")

chars_list = []
for sho_line, yo_line, ban_line in zip(sho_file.readlines(), yo_file.readlines(), ban_file.readlines()):
    sho_chars = ["▁" if ch == ' ' else ch for ch in sho_line.strip()]
    yo_chars = ["▁" if ch == ' ' else ch for ch in yo_line.strip()]
    ban_chars = ["▁" if ch == ' ' else ch for ch in ban_line.strip()]

    chars_list += [(" ".join(sho_chars), " ".join(yo_chars), " ".join(ban_chars))]

sho_file.close()
yo_file.close()
ban_file.close()

train_close_arr, train_arr, dev_arr, test_arr = split_dataset(chars_list)

write_data("data/chars/train_close.chars", train_close_arr)
write_data("data/chars/train.chars", train_arr)
write_data("data/chars/dev.chars", dev_arr)
write_data("data/chars/test.chars", test_arr)
