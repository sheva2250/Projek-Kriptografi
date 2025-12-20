import json
from pathlib import Path

DATA_PATH = Path("data/sbox_data_full.json")

def load_dataset():
    with open(DATA_PATH, "r") as f:
        raw = json.load(f)

    return {
        c["id"]: c
        for c in raw["candidates"]
    }

def get_sbox_by_id(dataset, sbox_id):
    return dataset[sbox_id]["sbox"]

def get_metrics_by_id(dataset, sbox_id):
    return dataset[sbox_id]["metrics"]

def get_matrix_by_id(dataset, sbox_id):
    return dataset[sbox_id]["matrix"]
