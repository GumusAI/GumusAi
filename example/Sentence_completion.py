import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Modeli yükleme
model = load_model('best_model.h5')

# Kelime ve etiket indekslerini yükleme
with open('kelime2idx.json', 'r', encoding='utf-8') as f:
    kelime2idx = json.load(f)

with open('y2idx.json', 'r', encoding='utf-8') as f:
    y2idx = json.load(f)

# Ters sözlükler
idx2kelime = {idx: kelime for kelime, idx in kelime2idx.items()}
idx2y = {idx: upos for upos, idx in y2idx.items()}

# Eğitim sırasında kullanılan maksimum uzunluk (142 olarak belirlenmiş)
maxlen = 142

def cumle_tamamlama(cumle, tamamlanacak_kelime_sayisi=5):
    cumle_tokens = cumle.split()
    for _ in range(tamamlanacak_kelime_sayisi):
        cumle_idx = [kelime2idx.get(kelime, kelime2idx['<unk>']) for kelime in cumle_tokens]
        cumle_idx = pad_sequences([cumle_idx], maxlen=maxlen, padding='post', value=kelime2idx['<pad>'])
        tahminler = model.predict(cumle_idx)
        tahmin_kelime_idx = tahminler.argmax(axis=-1)[0][len(cumle_tokens)]
        
        # Eğer tahmin edilen kelime <pad> ise, rastgele bir kelime seç
        tahmin_kelime = idx2kelime.get(tahmin_kelime_idx, '<unk>')
        if tahmin_kelime == '<pad>':
            tahmin_kelime = np.random.choice(list(kelime2idx.keys()))
        
        cumle_tokens.append(tahmin_kelime)
    return ' '.join(cumle_tokens)

# Kullanıcıdan girdi alma
ornek_cumle = input("Lütfen bir cümle başlatın: ")
tamamlanmis_cumle = cumle_tamamlama(ornek_cumle)

# Sonuçları yazdırma
print("Tamamlanmış cümle:", tamamlanmis_cumle)
