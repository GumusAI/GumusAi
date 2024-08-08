import numpy as np
import tensorflow as tf

# İndeks dosyasını yükleme
index_file_path = '/content/drive/MyDrive/birlesik_kelime_indeksleri.npy'
index_to_word = np.load(index_file_path, allow_pickle=True).item()  # Eğer dosya bir sözlük ise

# Vokabülere göre indekslere dönüştürme
word_to_index = {word: idx for idx, word in enumerate(index_to_word.keys())}
vocab_size = len(word_to_index)  # Vokabül büyüklüğü

def words_to_indices(words):
    """Kelimeleri indekslere dönüştürür."""
    return [word_to_index.get(word, vocab_size - 1) for word in words]

def indices_to_words(indices):
    """İndeksleri kelimelere dönüştürür."""
    reverse_index_to_word = {idx: word for word, idx in word_to_index.items()}
    if isinstance(indices, (int, np.int64)):  # Tekil bir değer
        return reverse_index_to_word.get(indices, '<UNK>')
    return [reverse_index_to_word.get(idx, '<UNK>') for idx in indices]

def pad_sequence(sequence, max_len):
    """Giriş dizisini belirtilen uzunluğa sıfırlarla doldurur."""
    if len(sequence) < max_len:
        return np.pad(sequence, (0, max_len - len(sequence)), mode='constant')
    return sequence[:max_len]  # Uzunluğu kes

def predict_completion(model, input_sequence, vocab_size):
    """Modeli kullanarak bir giriş dizisini tamamlar."""
    max_len = model.input_shape[1]  # Modelin beklediği giriş uzunluğu
    padded_sequence = pad_sequence(input_sequence, max_len)
    padded_sequence = np.expand_dims(padded_sequence, axis=0)  # Batch boyutunu ekle

    # Tahmin yap
    y_pred_proba = model.predict(padded_sequence)
    y_pred = np.argmax(y_pred_proba, axis=-1)[0]

    return y_pred

# Test için kullanıcıdan girdi alma
input_words = input("Lütfen tamamlamak istediğiniz kelimeleri (boşluk ile ayırın) girin: ").split()
input_indices = words_to_indices(input_words)

# Modeli yükleme
model_save_path = '/content/drive/MyDrive/final_model.keras'
loaded_model = tf.keras.models.load_model(model_save_path)

# Tamamlanmış diziyi tahmin et
completed_indices = predict_completion(loaded_model, input_indices, vocab_size)
completed_words = indices_to_words(completed_indices)

# Tahmin edilen diziyi yazdır
print("Tamamlanmış kelimeler: ")
print(' '.join(completed_words))
