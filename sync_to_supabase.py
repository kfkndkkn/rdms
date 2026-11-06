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

    # 1. Baca CSV menggunakan Pandas
    df = pd.read_csv(csv_path)
    
    # 2. Tangani nilai infinity dan NaN agar aman untuk JSON/Supabase
    df = df.replace([np.inf, -np.inf], np.nan)
    
    # Konversi DataFrame ke list of dictionaries
    data_records = df.to_dict(orient="records")
    
    cleaned_records = []
    for row in data_records:
        cleaned_row = {k: (None if pd.isna(v) else v) for k, v in row.items()}
        cleaned_records.append(cleaned_row)

    print("Mengosongkan tabel Supabase (Truncate)...")
    # 3. Kosongkan tabel secara instan menggunakan fungsi RPC Supabase
    supabase.rpc("truncate_timeseries").execute()

    print("Memasukkan data baru dari CSV ke Supabase...")
    # 4. Masukkan data yang baru dari CSV
    response = supabase.table("timeseries_all").insert(
        cleaned_records
    ).execute()
    
    print("Sinkronisasi (Replace total) ke Supabase berhasil:", response)

if __name__ == "__main__":
    sync_csv_to_supabase()
