from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from unidecode import unidecode
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


# Đường dẫn tới tệp văn bản của bạn
file_path = "b.txt"

# Đọc nội dung từ tệp
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Tiền xử lý dữ liệu văn bản
def preprocess_text(text):
    # Chuyển đổi thành chữ thường
    text = text.lower()
    
    # Loại bỏ dấu câu
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Loại bỏ stop words
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stop_words]
    text = ' '.join(filtered_words)
    
    return text

# Áp dụng tiền xử lý
preprocessed_text = preprocess_text(text)
########################################################################################################

def vectorize(Text): 
    return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2): 
    return cosine_similarity([doc1, doc2])

try:
    # Đọc nội dung từ hai tệp tin văn bản
    document1_text = open("BTL\A.txt", encoding='utf-8').read()
    # Áp dụng unidecode để chuyển đổi ký tự Unicode thành không dấu
    document1_text = unidecode(document1_text)
    # Ví dụ loại bỏ dấu câu
    document1_text = re.sub(r'[^\w\s]', '', document1_text)

    
    preprocessed_text = open("BTL/b.txt", encoding='utf-8').read()
    preprocessed_text = unidecode(preprocessed_text)
    preprocessed_text = re.sub(r'[^\w\s.,?!]', '', preprocessed_text)

    # Chuyển đổi đoạn văn thành vector
    vectors = vectorize([document1_text, preprocessed_text])

    # So sánh tương đồng giữa hai đoạn văn
    similarity_score = similarity(vectors[0], vectors[1])[0][1]

    print("Tương đồng:", similarity_score)

except Exception as e:
    print("Đã xảy ra lỗi:", str(e))
