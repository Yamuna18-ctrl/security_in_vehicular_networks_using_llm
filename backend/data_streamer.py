import os
import csv
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "I294_L1_final.csv")

def get_live_vehicle_batch(batch_size=6):
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"CSV not found at {DATA_FILE}")

    with open(DATA_FILE, newline="", encoding="utf-8", errors="ignore") as f:
        rows = list(csv.DictReader(f))

    sample = random.sample(rows, min(batch_size, len(rows)))
    messages = []

    for r in sample:
        messages.append({
            "vehicle_id": f"V{r.get('id','0')}",
            "speed": float(r.get("speed_kf", 0)),
            "acceleration": float(r.get("acceleration_kf", 0)),
            "lane": r.get("lane_kf", "NA"),
            "time": r.get("time", "NA")
        })

    return messages
