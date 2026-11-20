import os
import sys
import pandas as pd
import openpyxl
import json

DATASET_DIR = r"D:\Geoplotics how it afftects millitary\dataset"
OUTPUT_DIR = r"D:\Geoplotics how it afftects millitary\outputs\reports"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Starting FAST dataset profiling...", flush=True)

reports = {}

# 1. SIPRI MILITARY EXPENDITURE DATASET
sipri_path = os.path.join(DATASET_DIR, "SIPRI-Milex-data-1949-2025_v1.2.xlsx")
if os.path.exists(sipri_path):
    print("Profiling SIPRI...", flush=True)
    wb = openpyxl.load_workbook(sipri_path, read_only=True, data_only=True)
    sheets = wb.sheetnames
    
    # Inspect "Share of GDP" sheet
    sheet = wb["Share of GDP"] if "Share of GDP" in sheets else wb[sheets[0]]
    rows = list(sheet.iter_rows(values_only=True))
    header = [str(c) for c in rows[5] if c is not None]
    years = [c for c in header if c.isdigit()]
    
    sipri_info = {
        "file": "SIPRI-Milex-data-1949-2025_v1.2.xlsx",
        "file_size": f"{os.path.getsize(sipri_path) / 1024:.1f} KB",
        "sheets": sheets,
        "total_rows": len(rows),
        "total_cols": len(header),
        "year_min": min([int(y) for y in years]) if years else 1949,
        "year_max": max([int(y) for y in years]) if years else 2025,
        "country_column": "Country / Territory (Column 0)",
        "sample_columns": header[:12]
    }
    reports["SIPRI"] = sipri_info

# 2. V-DEM CORE DATASET
vdem_core_path = os.path.join(DATASET_DIR, "V-Dem-CY-Core-v16.csv")
if os.path.exists(vdem_core_path):
    print("Profiling V-Dem Core...", flush=True)
    with open(vdem_core_path, 'r', encoding='utf-8', errors='ignore') as f:
        header_line = f.readline().strip().split(',')
        total_rows = sum(1 for _ in f)
        
    df_vdem = pd.read_csv(vdem_core_path, usecols=['year', 'country_name', 'country_text_id', 'country_id', 'v2x_polyarchy', 'v2x_libdem', 'v2x_execorr'])
    
    vdem_info = {
        "file": "V-Dem-CY-Core-v16.csv",
        "file_size": f"{os.path.getsize(vdem_core_path) / (1024**2):.1f} MB",
        "rows": total_rows,
        "cols": len(header_line),
        "year_min": int(df_vdem['year'].min()),
        "year_max": int(df_vdem['year'].max()),
        "unique_countries": int(df_vdem['country_name'].nunique()),
        "country_col": "country_name",
        "country_code_col": "country_text_id (ISO3)",
        "key_democracy_indices": ['v2x_polyarchy', 'v2x_libdem', 'v2x_delibdem', 'v2x_egaldem', 'v2x_partipdem', 'v2x_execorr', 'v2x_pubcorr', 'v2x_freexp_altinf'],
        "sample_vars": header_line[:15]
    }
    reports["VDem_Core"] = vdem_info

# 3. GLOBAL TERRORISM DATABASE (GTD)
gtd_path = os.path.join(DATASET_DIR, "globalterrorismdb_0522dist.xlsx")
if os.path.exists(gtd_path):
    print("Profiling GTD...", flush=True)
    wb = openpyxl.load_workbook(gtd_path, read_only=True, data_only=True)
    sheet = wb.active
    rows = sheet.iter_rows(values_only=True)
    header = next(rows)
    
    # Read first 10,000 rows quickly to compute stats
    sample_rows = []
    for i, r in enumerate(rows):
        sample_rows.append(r)
        if i >= 10000:
            break
            
    df_sample = pd.DataFrame(sample_rows, columns=header)
    
    gtd_info = {
        "file": "globalterrorismdb_0522dist.xlsx",
        "file_size": f"{os.path.getsize(gtd_path) / (1024**2):.1f} MB",
        "sample_rows_analyzed": len(df_sample),
        "cols": len(header),
        "year_min": int(df_sample['iyear'].min()) if 'iyear' in df_sample else 1970,
        "year_max": int(df_sample['iyear'].max()) if 'iyear' in df_sample else 2020,
        "country_col": "country_txt",
        "region_col": "region_txt",
        "key_vars": ['eventid', 'iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'city', 'latitude', 'longitude', 'success', 'suicide', 'attacktype1_txt', 'targtype1_txt', 'gname', 'nkill', 'nwound']
    }
    wb.close()
    reports["GTD"] = gtd_info

# 4. GDELT MASTER REDUCED V2
gdelt_path = os.path.join(DATASET_DIR, "GDELT.MASTERREDUCEDV2.TXT")
if os.path.exists(gdelt_path):
    print("Profiling GDELT...", flush=True)
    df_sample = pd.read_csv(gdelt_path, sep='\t', nrows=5000, header=None, low_memory=False)
    
    gdelt_info = {
        "file": "GDELT.MASTERREDUCEDV2.TXT",
        "file_size": f"{os.path.getsize(gdelt_path) / (1024**3):.2f} GB",
        "cols": len(df_sample.columns),
        "sample_rows_analyzed": len(df_sample),
        "date_col_index": 1,
        "actor1_col_index": 6,
        "actor2_col_index": 16,
        "eventcode_col_index": 26,
        "quadclass_col_index": 29,
        "goldstein_col_index": 30,
        "actiongeo_country_index": 51
    }
    reports["GDELT"] = gdelt_info

print("\n--- FAST Profiling Results ---", flush=True)
print(json.dumps(reports, indent=2, default=str), flush=True)

with open(os.path.join(OUTPUT_DIR, "fast_profiling_results.json"), "w") as f:
    json.dump(reports, f, indent=2, default=str)

print("FAST profiling completed.", flush=True)
