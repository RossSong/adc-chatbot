# 어체변환 모델
Style Transfer Model for Korean Language

## Introduction
챗봇 대화시스템 발화의 어체를 변환하는 Attention Encoder-Decoder 모델이다.
소스 코드는 [구글 NMT 모델](https://github.com/tensorflow/nmt)을 기반으로 한다.

## 실행방법

* Train 데이터로 Vocabulary 파일 만들기
```sh
python make_vocab.py < train.txt > vocab.txt
```

* 환경변수 정의
데이터폴더, 모델폴더, 학습 파라미터 등 환경변수를 정의한다. (정확한 경로는 본인 작업환경에 맞게 수정필요)

```sh
export PRJ_DIR=/home/hkh/sources/adc-style-transfer
export DATA_DIR=$PRJ_DIR/data/chars
export MODEL_DIR=$PRJ_DIR/models/char_baseline_dropout0.2
export HPARAM_DIR=$PRJ_DIR/hparams
```

* 모델학습
모델 학습에 필요한 train, dev, test 및 vocab 파일을 준비해야 함. (파일명 prefix는 같게하고 확장자로 source, target 구분!)
```sh
python -m nmt.nmt \
--src=src \
--tgt=tgt \
--vocab_prefix=$DATA_DIR/chars_vocab \
--train_prefix=$DATA_DIR/train.last_chars \
--dev_prefix=$DATA_DIR/dev.last_chars \
--test_prefix=$DATA_DIR/test.last_chars \
--out_dir=$MODEL_DIR \
--hparams_path=$HPARAM_DIR/chars_baseline.json
```

* Inference
```sh
python -m nmt.nmt \
--out_dir=$MODEL_DIR \
--inference_input_file=$DATA_DIR/dev.last_chars.src \
--inference_output_file=/tmp/dev.last_chars.tgt
```
