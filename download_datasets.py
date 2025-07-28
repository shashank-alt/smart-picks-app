import gdown
import os

def download_datasets():
    files = {
        "similarity.pkl": "1MjFbrUuPYu-LHUsyx8NKjFxLLBTQi_xK",
        "similarity1.pkl": "1sJB1cHCqR8RxLZu2pTt2QMxcm66zVhMg"
    }

    os.makedirs("models", exist_ok=True)

    for filename, file_id in files.items():
        output = os.path.join("models", filename)
        if not os.path.exists(output):
            print(f"Downloading {filename}...")
            gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)

if __name__ == "__main__":
    download_datasets()
