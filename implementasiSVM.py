import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Baca data yang telah diberi label sentimen
data = pd.read_csv('reviews_test_cleaned_dengan_sentimen.csv')

# Ekstraksi fitur dengan TF-IDF
tfidf_vectorizer = TfidfVectorizer()
X = data['Review User']
y = data['sentimen']
X_tfidf = tfidf_vectorizer.fit_transform(X)

# Bagi data menjadi data pelatihan dan data pengujian
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.1, random_state=42)

# Implementasi SVM
svm_classifier = SVC(kernel='linear', C=1)
svm_classifier.fit(X_train, y_train)

# Prediksi sentimen pada data pengujian
y_pred = svm_classifier.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Evaluasi model pada data validasi
accuracy_validasi = accuracy_score(y_pred, y_pred)

print("Confusion Matrix:\n", cm)
print("Akurasi Model SVM pada data pengujian: ", accuracy)
print("Akurasi Model SVM pada data validasi: ", accuracy_validasi)
print("Laporan Klasifikasi:\n", classification_rep)
