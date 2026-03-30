import os
import yaml
import pandas as pd
import numpy as np
import shutil
import random
from datetime import datetime, timedelta

from utils.helpers import (
    set_seed,
    generate_name,
    generate_document,
    generate_segment,
    generate_score,
    generate_city,
    random_date,
    inject_null,
    log,
    get_date_range
)

# CONFIGIGURACIONES

def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

# CLIENTES

def generate_clientes(config):
    log("Generating TB_CLIENTES_CORE")

    num_records = config["data"]["TB_CLIENTES_CORE"]
    start_date, end_date = get_date_range(config["data"]["months"])

    data = []

    for i in range(num_records):
        first_name, last_name = generate_name()
        city, depto = generate_city()

        birth_date = random_date(datetime(1960, 1, 1), datetime(2005, 1, 1))
        alta_date = random_date(start_date, end_date)

        data.append({
            "id_cli": i + 1,
            "nomb_cli": inject_null(first_name),
            "apell_cli": inject_null(last_name),
            "tip_doc": "CC",
            "num_doc": inject_null(generate_document()),
            "fec_nac": birth_date,
            "fec_alta": alta_date,
            "cod_segmento": generate_segment(),
            "score_buro": generate_score(),
            "ciudad_res": city,
            "depto_res": depto,
            "estado_cli": "ACTIVO",
            "canal_adquis": "DIGITAL"
        })

    return pd.DataFrame(data)

# PRODUCTOS

def generate_productos(config):
    log("Generating TB_PRODUCTOS_CAT")

    num_records = config["data"]["TB_PRODUCTOS_CAT"]

    data = []

    for i in range(num_records):
        data.append({
            "cod_prod": f"P{i+1}",
            "desc_prod": f"Producto_{i+1}",
            "tip_prod": ["CREDITO", "AHORRO", "TRANSACCIONAL"][i % 3],
            "tasa_ea": round(0.1 + (i % 10) * 0.02, 4),
            "plazo_max_meses": (i % 60) + 12,
            "cuota_min": 50000,
            "comision_admin": 10000,
            "estado_prod": "ACTIVO"
        })

    return pd.DataFrame(data)

# MOVIMIENTOS

def generate_movimientos(config, clientes, productos):
    log("Generating TB_MOV_FINANCIEROS")

    num_records = config["data"]["TB_MOV_FINANCIEROS"]

    start_date, end_date = get_date_range(config["data"]["months"])
    date_range = (end_date - start_date).days

    df = pd.DataFrame({
        "id_mov": range(1, num_records + 1),
        "id_cli": np.random.choice(clientes["id_cli"], num_records),
        "cod_prod": np.random.choice(productos["cod_prod"], num_records),
        "num_cuenta": [
            str(random.randint(10**9, 10**10 - 1))
            for _ in range(num_records)
        ],
        "fec_mov": [
            start_date + timedelta(days=np.random.randint(0, date_range))
            for _ in range(num_records)
        ],
        "tip_mov": np.random.choice(["debito", "credito"], num_records),
        "cod_canal": np.random.choice(["APP", "WEB", "ATM", "OFICINA"], num_records),
        "cod_ciudad": np.random.choice(["BOG", "MED", "LIM", "SCL", "MEX"], num_records),
        "cod_estado_mov": np.random.choice(["OK", "PEND", "REV"], num_records),
        "id_dispositivo": np.random.randint(1000, 9999, num_records)
    })

    def generate_hour():
        if np.random.rand() < 0.7:
            return np.random.choice(list(range(8, 11)) + list(range(18, 22)))
        return np.random.randint(0, 24)

    df["hra_mov"] = [generate_hour() for _ in range(len(df))]

    df["vr_mov"] = np.round(
        np.random.exponential(scale=200000, size=len(df)), 2
    )

    # ANOMALIAS
    fraud_idx = np.random.choice(df.index, int(0.01 * len(df)), replace=False)
    df.loc[fraud_idx, "vr_mov"] *= 20

    night_idx = np.random.choice(df.index, int(0.02 * len(df)), replace=False)
    df.loc[night_idx, "hra_mov"] = np.random.choice(range(0, 5))

    duplicates = df.sample(frac=0.01)
    df = pd.concat([df, duplicates], ignore_index=True)

    df["vr_mov_mean_30d"] = None
    df["vr_mov_std_30d"] = None
    df["ind_sospechoso"] = 0

    log(f"Total registros: {len(df)}")

    return df

# OBLIGACIONES

def generate_obligaciones(config, clientes, productos):
    log("Generating TB_OBLIGACIONES")

    num_records = config["data"]["TB_OBLIGACIONES"]

    start_date, end_date = get_date_range(config["data"]["months"])
    date_range = (end_date - start_date).days

    data = []

    for i in range(num_records):
        vr_aprobado = np.random.randint(500000, 50000000)
        vr_desembolsado = vr_aprobado * np.random.uniform(0.8, 1.0)

        fec_desembolso = start_date + timedelta(days=np.random.randint(0, date_range))

        data.append({
            "id_obl": i + 1,
            "id_cli": np.random.choice(clientes["id_cli"]),
            "cod_prod": np.random.choice(productos["cod_prod"]),
            "vr_aprobado": round(vr_aprobado, 2),
            "vr_desembolsado": round(vr_desembolsado, 2),
            "sdo_capital": round(vr_desembolsado * np.random.uniform(0.3, 1.0), 2),
            "vr_cuota": round(vr_desembolsado / np.random.randint(6, 60), 2),
            "fec_desembolso": fec_desembolso,
            "fec_venc": fec_desembolso + timedelta(days=np.random.randint(30, 365 * 3)),
            "dias_mora_act": np.random.choice([0]*60 + list(range(1,120))),
            "num_cuotas_pend": np.random.randint(1, 60),
            "calif_riesgo": np.random.choice(["A","B","C","D","E"])
        })

    df = pd.DataFrame(data)

    idx = np.random.choice(df.index, int(0.01 * len(df)), replace=False)
    df.loc[idx, "fec_venc"] = df.loc[idx, "fec_desembolso"] - timedelta(days=10)

    return df

# COMISIONES

def generate_comisiones(config, clientes, productos):
    log("Generating TB_COMISIONES_LOG")

    num_records = config["data"]["TB_COMISIONES_LOG"]

    start_date, end_date = get_date_range(config["data"]["months"])
    date_range = (end_date - start_date).days

    data = []

    for i in range(num_records):
        data.append({
            "id_comision": i + 1,
            "id_cli": np.random.choice(clientes["id_cli"]),
            "cod_prod": np.random.choice(productos["cod_prod"]),
            "fec_cobro": start_date + timedelta(days=np.random.randint(0, date_range)),
            "vr_comision": round(np.random.exponential(scale=15000), 2),
            "tip_comision": np.random.choice(["ADMIN","RETIRO","TRANSFERENCIA","CUOTA_MANEJO"]),
            "estado_cobro": np.random.choice(["COBRADO","PENDIENTE","ANULADO"], p=[0.8,0.15,0.05])
        })

    return pd.DataFrame(data)

# SUCURSALES

def generate_sucursales(config):
    log("Generating TB_SUCURSALES_RED")

    num_records = config["data"]["TB_SUCURSALES_RED"]

    ciudades = ["Bogotá", "Medellín", "Lima", "Santiago", "CDMX"]

    data = []

    for i in range(num_records):
        data.append({
            "cod_suc": f"SUC{i+1}",
            "nom_suc": f"Sucursal_{i+1}",
            "tip_punto": np.random.choice(["OFICINA","CAJERO","APP","WEB"]),
            "ciudad": ciudades[i % len(ciudades)],
            "latitud": round(np.random.uniform(-35, 5), 6),
            "longitud": round(np.random.uniform(-75, -30), 6),
            "activo": np.random.choice([1,0], p=[0.9,0.1])
        })

    return pd.DataFrame(data)

#  LIMPIEZA OUTPUT GARANTIZANDO IDEMPOTENCIA
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def clean_output(config):
    base_path = os.path.join(BASE_DIR, config["output"]["path"])

    if os.path.exists(base_path):
        shutil.rmtree(base_path)

    os.makedirs(base_path, exist_ok=True)


# GUARDAR


def save_data(df, name, config):
    base_path = os.path.join(BASE_DIR, config["output"]["path"])

    csv_path = os.path.join(base_path, "csv")
    parquet_path = os.path.join(base_path, "parquet")

    os.makedirs(csv_path, exist_ok=True)
    os.makedirs(parquet_path, exist_ok=True)

    df.to_csv(f"{csv_path}/{name}.csv", index=False)
    df.to_parquet(f"{parquet_path}/{name}.parquet", index=False)

    log(f"Saved {name}")


# MAIN

def main():
    config = load_config()

    set_seed(config["seed"])
    clean_output(config)

    clientes = generate_clientes(config)
    productos = generate_productos(config)
    movimientos = generate_movimientos(config, clientes, productos)
    obligaciones = generate_obligaciones(config, clientes, productos)
    comisiones = generate_comisiones(config, clientes, productos)
    sucursales = generate_sucursales(config)

    save_data(clientes, "TB_CLIENTES_CORE", config)
    save_data(productos, "TB_PRODUCTOS_CAT", config)
    save_data(movimientos, "TB_MOV_FINANCIEROS", config)
    save_data(obligaciones, "TB_OBLIGACIONES", config)
    save_data(comisiones, "TB_COMISIONES_LOG", config)
    save_data(sucursales, "TB_SUCURSALES_RED", config)

    log("Data generation completed successfully")

# EXECUTION

if __name__ == "__main__":
    main()