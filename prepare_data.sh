echo "Running python script: make_ban_char_level.py"
python make_ban_char_level.py
echo "Done!"

echo "Running python script: make_vocab.py"
cat data/chars/train.chars.* | python make_vocab.py > data/chars/chars_vocab.all
echo "Done!"

cp data/chars/chars_vocab.all data/chars/chars_vocab.sho
cp data/chars/chars_vocab.all data/chars/chars_vocab.yo
cp data/chars/chars_vocab.all data/chars/chars_vocab.ban

echo "All Done!"