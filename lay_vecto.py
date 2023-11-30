import tensorflow as tf

# Đọc từ điển từ file
word_index = {}
with open('word_index.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(': ')
        word, index = parts[0], int(parts[1])
        word_index[word] = index

# Thêm khóa '<OOV>' vào từ điển
# word_index['<OOV>'] = len(word_index) + 1

# Đoạn văn bản cần chuyển thành vector
input_text = "The first software is called Wiki"

# Chuyển đoạn văn bản thành danh sách các chỉ số từ từ điển
sequence = [word_index.get(word, word_index['<OOV>']) for word in input_text.lower().split()]

# Hiển thị kết quả
print(f"Đoạn văn bản: {input_text}")
print(f"Vector tương ứng: {sequence}")
