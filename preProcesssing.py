import pandas as pd
import re
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import word_tokenize

# Baca data dari file CSV
data = pd.read_csv('reviews.csv')

# Membaca data slang-formal dari file CSV
slang_formal = pd.read_csv('colloquial-indonesian-lexicon.csv')
slang_dict = dict(zip(slang_formal['slang'], slang_formal['formal']))

#Pra-pemrosesan data
def preprocess_text(text):
    # Mengubah teks menjadi huruf kecil
    text = text.lower()

    # Menghapus tanda baca dan karakter khusus
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Tokenisasi teks menjadi kata-kata
    words = word_tokenize(text)

    # Normalisasi
    words = [slang_dict.get(word, word) for word in words]

    # Menghapus stop words (kata-kata umum yang tidak relevan)
    stop_words = set(stopwords.words('indonesian'))
    custom_stopwords = ["ya", "oke", "nih", "oiya", "sih"]
    stop_words.update(custom_stopwords)
    words = [word for word in words if word not in stop_words]

    # Stemming (mengubah kata-kata menjadi bentuk dasarnya)
    stemmer = StemmerFactory().create_stemmer()
    words = [stemmer.stem(word) for word in words]

    return ' '.join(words)

# Terapkan pra-pemrosesan pada kolom "Review User"
data['Review User'] = data['Review User'].apply(preprocess_text)

# Menangani nilai null setelah pra-pemrosesan
data['Review User'].fillna('', inplace=True)

# Menyimpan data yang telah diproses ke file CSV baru
data.to_csv('reviews_test_cleaned.csv', index=False)
