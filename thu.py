# from keras.preprocessing.text import Tokenizer

# # Một ví dụ văn bản
# text = "This is a sample text. You can replace it with your own text for dictionary creation."

# # Tạo một đối tượng Tokenizer với cơ chế OOV
# tokenizer = Tokenizer(oov_token="<OOV>")

# # Fit trên văn bản để tạo từ điển và gán số cho từng từ
# tokenizer.fit_on_texts([text])

# # Lấy từ điển và gán số
# word_index = tokenizer.word_index

# # In từ điển và số
# print("Từ điển:")
# print(word_index)

# # Một văn bản mới
# new_text = "This is another example text for testing the tokenizer."

# # Chuyển đổi văn bản mới thành vector sử dụng từ điển đã tạo, bao gồm OOV
# new_text_sequences = tokenizer.texts_to_sequences([new_text])

# # In vector của văn bản mới
# print("Vector của văn bản mới (bao gồm OOV):")
# print(new_text_sequences)


import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Giả sử A và B là hai ma trận văn bản chuyển thành vector
vector_A = np.array([1, 2, 3, 4, 5])
vector_B = np.array([2, 3, 4, 5, 6])

# Reshape vectors to make them 2D arrays
vector_A = vector_A.reshape(1, -1)
vector_B = vector_B.reshape(1, -1)

# Tính cosine similarity
similarity_score = cosine_similarity(vector_A, vector_B)[0, 0]

# Tính tỉ lệ đạo văn giống
plagiarism_percentage = similarity_score * 100

print(f"Tỉ lệ đạo văn giống: {plagiarism_percentage}%")

