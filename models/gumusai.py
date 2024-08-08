from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

# Google Drive'a giriş yap
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Yerel bir kimlik doğrulama sunucusu başlatır
drive = GoogleDrive(gauth)

# Klasör ID'sini belirtin (URL'deki 'folder/' sonrası ID)
folder_id = '1YMl4DHAyZhGxaRFpOC9bHPaPLRfnj8eA'

# Klasör içindeki dosyaları alın
file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

# Dosyaları indirmek için bir klasör oluştur
download_folder = 'GoogleDriveDownload'
os.makedirs(download_folder, exist_ok=True)

# Dosyaları indirin
for file in file_list:
    print(f"Downloading {file['title']}...")
    file.GetContentFile(os.path.join(download_folder, file['title']))

print("All files downloaded.")
