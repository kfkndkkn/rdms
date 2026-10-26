import os
import pandas as pd
from supabase import create_client, Client

# Ambil kredensial dari Environment Variables (GitHub Secrets)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

if not url or not key:
    raise ValueError("Supabase URL dan Key harus diset pada environment variables.")

supabase: Client = create_client(url, key)

def sync_csv_to_supabase():
    # Nama file CSV di root repository
    csv_path = "timeseries_all.csv" 

    if not os.path.exists(csv_path):
        print(f"File CSV tidak ditemukan: {csv_path}")
        return

    # Baca CSV menggunakan Pandas
    df = pd.read_csv(csv_path)
    
    # Tangani nilai kosong (NaN) agar menjadi None yang valid untuk JSON/Supabase
    df = df.where(pd.notnull(df), None)
    
    # Konversi DataFrame ke format list of dictionaries
    data_records = df.to_dict(orient="records")

    # Lakukan Upsert ke tabel Supabase 'timeseries_all'
    # Catatan: Pastikan 'on_conflict' diisi kolom unik/primary key di tabel Anda (misal: 'timestamp' atau 'id')
    response = supabase.table("timeseries_all").upsert(
        data_records, 
        on_conflict="timestamp" 
    ).execute()
    
    print("Sinkronisasi ke Supabase berhasil:", response)

if __name__ == "__main__":
    sync_csv_to_supabase()
