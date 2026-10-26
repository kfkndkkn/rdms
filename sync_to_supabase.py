import os
import numpy as np
import pandas as pd
from supabase import create_client, Client

# Ambil kredensial dari Environment Variables (GitHub Secrets)
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

if not url or not key:
    raise ValueError("Supabase URL dan Key harus diset pada environment variables.")

supabase: Client = create_client(url, key)

def sync_csv_to_supabase():
    csv_path = "timeseries_all.csv" 

    if not os.path.exists(csv_path):
        print(f"File CSV tidak ditemukan: {csv_path}")
        return

    # Baca CSV menggunakan Pandas
    df = pd.read_csv(csv_path)
    
    # Ubah nilai infinity menjadi NaN
    df = df.replace([np.inf, -np.inf], np.nan)
    
    # Konversi DataFrame ke format list of dictionaries
    data_records = df.to_dict(orient="records")
    
    # Bersihkan setiap baris secara manual agar NaN benar-benar menjadi None (JSON compliant)
    cleaned_records = []
    for row in data_records:
        cleaned_row = {k: (None if pd.isna(v) else v) for k, v in row.items()}
        cleaned_records.append(cleaned_row)

    # Lakukan Upsert ke tabel Supabase 'timeseries_all'
    response = supabase.table("timeseries_all").upsert(
        cleaned_records, 
        on_conflict="timestamp" 
    ).execute()
    
    print("Sinkronisasi ke Supabase berhasil:", response)

if __name__ == "__main__":
    sync_csv_to_supabase()
