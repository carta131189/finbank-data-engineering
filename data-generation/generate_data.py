import os
import yaml
import pandas as pd
from datetime import datetime

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


def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)



def generate_clientes(config):
    log("Generating TB_CLIENTES_CORE...")

    num_records = config["data"]["TB_CLIENTES_CORE"]
    start_date, end_date = get_date_range(config["data"]["months"])

    data = []

    for i in range(num_records):
        first_name, last_name = generate_name()
        city, depto = generate_city()

        birth_date = random_date(datetime(1960, 1, 1), datetime(2005, 1, 1))
        alta_date = random_date(start_date, end_date)

        row = {
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
        }

        data.append(row)

    df = pd.DataFrame(data)
    return df


def generate_productos(config):
    log("Generating TB_PRODUCTOS_CAT...")
    num_records = config["data"]["TB_PRODUCTOS_CAT"]

    data = []

    for i in range(num_records):
        row = {
            "cod_prod": f"P{i+1}",
            "desc_prod": f"Producto_{i+1}",


            "tip_prod": ["CREDITO", "AHORRO", "TRANSACCIONAL"][i % 3],
            "tasa_ea": round(0.1 + (i % 10) * 0.02, 4),
            "plazo_max_meses": (i % 60) + 12,
            "cuota_min": 50000,
            "comision_admin": 10000,

            "estado_prod": "ACTIVO"
        }
        data.append(row)

    df = pd.DataFrame(data)
    return df


def save_data(df, name, config):
    output_path = config["output"]["path"]

    os.makedirs(output_path, exist_ok=True)

    csv_path = f"{output_path}/{name}.csv"
    parquet_path = f"{output_path}/{name}.parquet"

    df.to_csv(csv_path, index=False)
    df.to_parquet(parquet_path, index=False)

    log(f"Saved {name} → CSV & Parquet")


def main():
    config = load_config()

    # reproducibilidad
    set_seed(config["seed"])

    clientes = generate_clientes(config)
    productos = generate_productos(config)

    save_data(clientes, "TB_CLIENTES_CORE", config)
    save_data(productos, "TB_PRODUCTOS_CAT", config)

    log("Data generation completed successfully")


if __name__ == "__main__":
    main()
