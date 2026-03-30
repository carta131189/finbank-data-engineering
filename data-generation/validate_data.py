import os
import pandas as pd

# Base path dinámico
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "output", "csv")

TABLES = [
    "TB_CLIENTES_CORE",
    "TB_PRODUCTOS_CAT",
    "TB_MOV_FINANCIEROS",
    "TB_OBLIGACIONES",
    "TB_COMISIONES_LOG",
    "TB_SUCURSALES_RED"
]

def validate_table(table):
    path = os.path.join(DATA_PATH, f"{table}.csv")

    print(f"\n Validando {table}")

    if not os.path.exists(path):
        print(f" Archivo no encontrado: {path}")
        return

    df = pd.read_csv(path)

    # Métricas
    rows = df.shape[0]
    cols = df.shape[1]
    duplicates = df.duplicated().sum()
    nulls = df.isnull().sum().sum()

    print(f"Filas: {rows}")
    print(f"Columnas: {cols}")
    print(f"Duplicados: {duplicates}")
    print(f"Nulos totales: {nulls}")

    # Validaciones clave
    if rows == 0:
        print("Tabla vacía")

    if duplicates > 0:
        print("Tiene duplicados (esperado en algunas tablas)")

    if nulls > 0:
        print("Tiene valores nulos (controlados)")

    print("Validación completada")


def main():
    print("\n INICIANDO VALIDACIÓN DE DATOS\n")

    for table in TABLES:
        validate_table(table)

    print("\n VALIDACIÓN FINALIZADA\n")


if __name__ == "__main__":
    main()