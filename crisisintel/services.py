import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f) 