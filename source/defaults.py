from pathlib import Path

# Template Variables
default_model_name = "model.pkl"
default_model_path = Path(__file__).resolve().parents[1] / "model_bin" / default_model_name