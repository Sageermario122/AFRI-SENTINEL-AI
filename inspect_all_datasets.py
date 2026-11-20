import os
import sys
import pandas as pd
import numpy as np
import openpyxl
import json

DATASET_DIR = r"D:\Geoplotics how it afftects millitary\dataset"
OUTPUT_DIR = r"D:\Geoplotics how it afftects millitary\outputs\reports"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Starting dataset profiling...")

reports = {}

# 1. SIPRI MILITARY EXPENDITURE DATASET
sipri_path = os.path.join(DATASET_DIR, "SIPRI-Milex-data-1949-2025_v1.2.xlsx")
if os.path.exists(sipri_path):
    print(f"\n--- Profiling SIPRI: {sipri_path} ---")
    xl = pd.ExcelFile(sipri_path)
    sheet_names = xl.sheet_names
    print(f"Sheets found: {sheet_names}")
    
    sipri_info = {"file": "SIPRI-Milex-data-1949-2025_v1.2.xlsx", "sheets": sheet_names}
    
    # Read Share of GDP sheet if available
    sheet_to_read = "Share of GDP" if "Share of GDP" in sheet_names else sheet_names[0]
    df_sipri = pd.read_excel(sipri_path, sheet_name=sheet_to_read, skiprows=5)
    
    sipri_info["rows"] = len(df_sipri)
    sipri_info["cols"] = len(df_sipri.columns)
    sipri_info["columns_sample"] = list(df_sipri.columns[:15])
    sipri_info["missing_pct"] = float(df_sipri.isnull().mean().mean() * 100)
    reports["SIPRI"] = sipri_info

# 2. V-DEM CORE DATASET
vdem_core_path = os.path.join(DATASET_DIR, "V-Dem-CY-Core-v16.csv")
if os.path.exists(vdem_core_path):
    print(f"\n--- Profiling V-Dem Core: {vdem_core_path} ---")
    df_vdem_sample = pd.read_csv(vdem_core_path, nrows=1000)
    
    with open(vdem_core_path, 'r', encoding='utf-8', errors='ignore') as f:
        total_rows = sum(1 for _ in f) - 1
        
    vdem_info = {
        "file": "V-Dem-CY-Core-v16.csv",
        "rows": total_rows,
        "cols": len(df_vdem_sample.columns),
        "key_vars": [c for c in df_vdem_sample.columns if c.startswith('v2x_') or c in ['year', 'country_name', 'country_text_id', 'COWcode', 'histcode']][:20]
    }
    
    df_vdem_light = pd.read_csv(vdem_core_path, usecols=['year', 'country_name', 'country_text_id', 'v2x_polyarchy', 'v2x_libdem', 'v2x_execorr'])
    vdem_info["year_min"] = int(df_vdem_light['year'].min())
    vdem_info["year_max"] = int(df_vdem_light['year'].max())
    vdem_info["unique_countries"] = int(df_vdem_light['country_name'].nunique())
    vdem_info["missing_pct"] = float(df_vdem_light.isnull().mean().mean() * 100)
    reports["VDem_Core"] = vdem_info

# 3. GLOBAL TERRORISM DATABASE (GTD)
gtd_path = os.path.join(DATASET_DIR, "globalterrorismdb_0522dist.xlsx")
if os.path.exists(gtd_path):
    print(f"\n--- Profiling GTD: {gtd_path} ---")
    df_gtd_sample = pd.read_excel(gtd_path, nrows=1000)
    
    gtd_cols = ['eventid', 'iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'city', 'latitude', 'longitude', 'success', 'suicide', 'attacktype1_txt', 'targtype1_txt', 'gname', 'nkill', 'nwound']
    avail_cols = [c for c in gtd_cols if c in df_gtd_sample.columns]
    
    df_gtd = pd.read_excel(gtd_path, usecols=avail_cols)
    
    gtd_info = {
        "file": "globalterrorismdb_0522dist.xlsx",
        "rows": len(df_gtd),
        "cols": len(df_gtd.columns),
        "year_min": int(df_gtd['iyear'].min()),
        "year_max": int(df_gtd['iyear'].max()),
        "unique_countries": int(df_gtd['country_txt'].nunique()),
        "total_fatalities": float(df_gtd['nkill'].sum()) if 'nkill' in df_gtd else 0,
        "total_events": len(df_gtd),
        "missing_pct": float(df_gtd.isnull().mean().mean() * 100),
        "key_vars": avail_cols
    }
    reports["GTD"] = gtd_info

# 4. GDELT MASTER REDUCED V2
gdelt_path = os.path.join(DATASET_DIR, "GDELT.MASTERREDUCEDV2.TXT")
if os.path.exists(gdelt_path):
    print(f"\n--- Profiling GDELT Master Reduced: {gdelt_path} ---")
    df_gdelt_sample = pd.read_csv(gdelt_path, sep='\t', nrows=10000, header=None, low_memory=False)
    
    gdelt_info = {
        "file": "GDELT.MASTERREDUCEDV2.TXT",
        "sample_rows": len(df_gdelt_sample),
        "cols": len(df_gdelt_sample.columns),
        "file_size_gb": round(os.path.getsize(gdelt_path) / (1024**3), 2)
    }
    reports["GDELT"] = gdelt_info

print("\n--- Summary of Inspection ---")
print(json.dumps(reports, indent=2, default=str))

with open(os.path.join(OUTPUT_DIR, "profiling_raw_summary.json"), "w") as f:
    json.dump(reports, f, indent=2, default=str)

print("Profiling script completed.")
