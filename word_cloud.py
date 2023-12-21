from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# Baca data dari file CSV
data = pd.read_csv('reviews_cleaned_dengan_sentimen.csv')

# Memisahkan ulasan positif dan negatif
ulasan_positif = " ".join(data[data['sentimen'] == 'positif']['Review User'])
ulasan_negatif = " ".join(data[data['sentimen'] == 'negatif']['Review User'])

# Membuat word cloud untuk sentimen positif
wordcloud_positif = WordCloud(width=800, height=400, background_color='white').generate(ulasan_positif)
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud_positif, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud Sentimen Positif')
plt.show()

# Membuat word cloud untuk sentimen negatif
wordcloud_negatif = WordCloud(width=800, height=400, background_color='white').generate(ulasan_negatif)
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud_negatif, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud Sentimen Negatif')
plt.show()
