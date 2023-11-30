import tensorflow as tf
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

word_index = {}
with open('word_index.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(': ')
        word, index = parts[0], int(parts[1])
        word_index[word] = index

# Mở file chứa các từ mới
with open('b.txt', 'r', encoding='utf-8') as new_words_file:
    new_words = new_words_file.read().split()
    # Chuẩn hóa văn bản bằng cách sử dụng stemming (Porter Stemmer)
    ps = PorterStemmer()
    new_words = [ps.stem(word) for word in new_words if word]
    # Loại bỏ kí tự đặc biệt
    new_words = [re.sub(r'[^a-zA-Z0-9]', '', word) for word in new_words]


if '<OOV>' not in word_index:
    word_index['<OOV>'] = 1
# Kiểm tra và bổ sung từ mới vào từ điển
for new_word in new_words:
    if new_word not in word_index:
        word_index[new_word] = len(word_index) + 1
with open('word_index.txt', 'w', encoding='utf-8') as file:
    for word, index in word_index.items():
        file.write(f"{word}: {index}\n")

# tokenizer = tf.keras.preprocessing.text.Tokenizer(oov_token="<OOV>")
# tokenizer.word_index = word_index
#################################################################
# import tensorflow as tf

# # Đoạn văn bản cần thêm vào từ điển
# input_text = "This is a sample text. You can replace it with your own for dictionary creation."

# # Tạo tokenizer với OOV
# tokenizer = tf.keras.preprocessing.text.Tokenizer(oov_token="<OOV>")

# # Cập nhật từ điển với đoạn văn bản
# tokenizer.fit_on_texts([input_text])

# # Lưu từ điển vào file txt
# with open('word_index.txt', 'w', encoding='utf-8') as file:
#     for word, index in tokenizer.word_index.items():
#         file.write(f"{word}: {index}\n")

# # Kiểm tra từ điển
# print(f"Từ điển: {tokenizer.word_index}")

