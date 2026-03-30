import pandas as pd
import os

def load_data():
    base_path = "output/csv"

    tables = [
        "TB_CLIENTES_CORE",
        "TB_PRODUCTOS_CAT",
        "TB_MOV_FINANCIEROS",
        "TB_OBLIGACIONES",
        "TB_COMISIONES_LOG",
        "TB_SUCURSALES_RED"
    ]

    for table in tables:
        path = os.path.join(base_path, f"{table}.csv")
        df = pd.read_csv(path)

        print(f"{table} loaded successfully")
        print(f"Rows: {len(df)}")
        print("-" * 40)

if __name__ == "__main__":
    load_data()