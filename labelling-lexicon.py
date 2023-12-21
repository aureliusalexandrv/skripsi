import pandas as pd

# Baca data ulasan setelah di preprocess
data = pd.read_csv('reviews_cleaned.csv')
# Membaca file lexicon positif
lexicon_positif = pd.read_csv('positive.tsv', delimiter='\t', names=['word', 'weight'], skiprows=1)

# Membaca file lexicon negatif
lexicon_negatif = pd.read_csv('negative.tsv', delimiter='\t', names=['word', 'weight'], skiprows=1)

# Menggabungkan lexicon positif dan negatif
lexicon = pd.concat([lexicon_positif, lexicon_negatif], ignore_index=True)

# Mengkonversi lexicon menjadi kamus (dictionary) dalam Python
lexicon_dict = dict(zip(lexicon['word'], lexicon['weight']))

# Menganalisis dan melabeli ulasan
def analisis_sentimen(ulasan, lexicon_dict):
    skor_sentimen = sum(lexicon_dict.get(word, 0) for word in ulasan.split())
    if skor_sentimen >= 0:
        label = 'positif'
    else:
        label = 'negatif'
    return skor_sentimen, label

# Menerapkan analisis sentimen pada setiap ulasan
data[['skor_sentimen', 'sentimen']] = data['Review User'].apply(lambda x: pd.Series(analisis_sentimen(x, lexicon_dict)))

# Simpan hasil analisis sentimen ke dalam file atau database
data.to_csv('reviews_cleaned_dengan_sentimen.csv', index=False)

