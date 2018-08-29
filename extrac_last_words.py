# _*_ coding: utf8 _*_
# 마지막 어절을 추출

N_LAST_WORDS = 1

src_file = open("data/adc_raw.txt", "r")
tgt_file = open("data/adc_trans.txt", "r")

sent_pairs = []
for src_line, tgt_line in zip(src_file.readlines(), tgt_file.readlines()):
    src_words = src_line.strip().split(" ")
    tgt_words = tgt_line.strip().split(" ")

    last_sw = src_words[-1]
    last_tw = tgt_words[-1]

    print(last_sw)
    print(last_tw)

    sent_pairs += [(last_sw, last_tw)]

src_file.close()
tgt_file.close()

last_sw_file = open("data/last_src_words.txt", "w")
last_tw_file = open("data/last_tgt_words.txt", "w")

for sent_pair in sent_pairs:
    last_sw_file.write(sent_pair[0]+"\n")
    last_tw_file.write(sent_pair[1]+"\n")
