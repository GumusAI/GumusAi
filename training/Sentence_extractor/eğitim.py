import json
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense, TimeDistributed, Dropout
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import tensorflow_addons as tfa


# JSON dosyasından veri yükleme
with open('kelimeanlamları.json', 'r', encoding='utf-8') as f:
    veri_seti = json.load(f)

# Veri setini oluşturma
X = []
y = []

for veri in veri_seti:
    tokens = veri['tokens']
    kelime_listesi = [token['form'] for token in tokens]
    etiket_listesi = [token['upos'] for token in tokens]  # 'upos' kullanarak örnek etiketler alındı
    X.append(kelime_listesi)
    y.append(etiket_listesi)

# Kelimeleri sayısal vektörlere dönüştürme
kelime_seti = set([kelime for cumle in X for kelime in cumle])
kelime2idx = {kelime: idx + 2 for idx, kelime in enumerate(kelime_seti)}
kelime2idx['<pad>'] = 0
kelime2idx['<unk>'] = 1

idx2kelime = {idx: kelime for kelime, idx in kelime2idx.items()}
y2idx = {upos: idx + 1 for idx, upos in enumerate(set([upos for etiketler in y for upos in etiketler]))}
y2idx['<pad>'] = 0

X = [[kelime2idx.get(kelime, kelime2idx['<unk>']) for kelime in cumle] for cumle in X]
X = pad_sequences(maxlen=max([len(cumle) for cumle in X]), sequences=X, padding="post", value=kelime2idx['<pad>'])

y = [[y2idx[upos] for upos in etiketler] for etiketler in y]
y = pad_sequences(maxlen=max([len(etiketler) for etiketler in y]), sequences=y, padding="post", value=y2idx['<pad>'])


# Eğitim ve test setlerini oluşturma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluşturma
model = Sequential()
model.add(Embedding(input_dim=len(kelime2idx), output_dim=100, input_length=X.shape[1]))  # Embedding boyutu artırıldı
model.add(Dropout(0.3))  # Dropout eklendi
model.add(Bidirectional(LSTM(units=128, return_sequences=True)))
model.add(Dropout(0.3))  # Dropout eklendi
model.add(Bidirectional(LSTM(units=128, return_sequences=True)))
model.add(TimeDistributed(Dense(len(y2idx), activation="softmax")))

# Modeli derleme
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt

# Early stopping ve model checkpoint callbacks tanımlama
early_stopping = EarlyStopping(monitor='val_loss', patience=3)  # val_loss'ta düşüş durursa 3 epoch sonra eğitimi durdur
model_checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True, save_weights_only=False, monitor='val_accuracy', mode='max', verbose=1)  # En iyi val_accuracy'ye sahip modeli kaydet

# Modeli eğitme
history = model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test), callbacks=[early_stopping, model_checkpoint])

# Eğitim ve validation loss değerlerini alın
train_loss = history.history['loss']
val_loss = history.history['val_loss']

# Eğitim ve validation accuracy değerlerini alın
train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']


# Kelime ve etiket indekslerini JSON dosyalarına kaydetme
with open('kelime2idx.json', 'w', encoding='utf-8') as f:
    json.dump(kelime2idx, f, ensure_ascii=False, indent=4)

with open('y2idx.json', 'w', encoding='utf-8') as f:
    json.dump(y2idx, f, ensure_ascii=False, indent=4)

# Loss değerlerini ve accuracy değerlerini görselleştirme
epochs = range(1, len(train_loss) + 1)
plt.figure(figsize=(12, 4))

# Loss değerleri
plt.subplot(1, 2, 1)
plt.plot(epochs, train_loss, 'bo-', label='Training loss')
plt.plot(epochs, val_loss, 'ro-', label='Validation loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Accuracy değerleri
plt.subplot(1, 2, 2)
plt.plot(epochs, train_acc, 'bo-', label='Training accuracy')
plt.plot(epochs, val_acc, 'ro-', label='Validation accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()