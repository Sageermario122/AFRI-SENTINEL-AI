import os
import shutil

BASE_DIR = r"D:\Geoplotics how it afftects millitary"

dirs = [
    os.path.join(BASE_DIR, "datasets", "raw", "GDELT"),
    os.path.join(BASE_DIR, "datasets", "raw", "ACLED"),
    os.path.join(BASE_DIR, "datasets", "raw", "WorldBank"),
    os.path.join(BASE_DIR, "datasets", "raw", "VDEM"),
    os.path.join(BASE_DIR, "datasets", "raw", "SIPRI"),
    os.path.join(BASE_DIR, "datasets", "raw", "GTD"),
    os.path.join(BASE_DIR, "datasets", "raw", "NaturalEarth"),
    os.path.join(BASE_DIR, "datasets", "processed", "cleaned"),
    os.path.join(BASE_DIR, "datasets", "processed", "normalized"),
    os.path.join(BASE_DIR, "datasets", "processed", "aggregated"),
    os.path.join(BASE_DIR, "datasets", "processed", "merged"),
    os.path.join(BASE_DIR, "datasets", "processed", "feature_engineering"),
    os.path.join(BASE_DIR, "datasets", "processed", "final_dataset"),
    os.path.join(BASE_DIR, "datasets", "processed", "metadata"),
    os.path.join(BASE_DIR, "src", "preprocessing"),
    os.path.join(BASE_DIR, "src", "feature_engineering"),
    os.path.join(BASE_DIR, "src", "evaluation"),
    os.path.join(BASE_DIR, "outputs", "reports"),
    os.path.join(BASE_DIR, "outputs", "evaluation"),
    os.path.join(BASE_DIR, "tests")
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"Created: {d}")

print("Directory structure setup completed successfully.")
