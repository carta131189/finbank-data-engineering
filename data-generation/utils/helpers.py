import random
import string
import uuid
from datetime import datetime, timedelta
import numpy as np

# ===============================
# CONFIG GLOBAL (SEED CONTROL)
# ===============================
def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)


# ===============================
# GENERADORES BÁSICOS
# ===============================
def generate_uuid():
    return str(uuid.uuid4())


def random_string(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


def random_datetime(start_date, end_date):
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start_date + timedelta(seconds=random_seconds)


def random_time_peak():
    """
    Simula horas pico (8-10 AM, 12-2 PM, 6-9 PM)
    """
    peak_hours = list(range(8, 10)) + list(range(12, 14)) + list(range(18, 21))
    if random.random() < 0.7:
        hour = random.choice(peak_hours)
    else:
        hour = random.randint(0, 23)

    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    return f"{hour:02d}:{minute:02d}:{second:02d}"


# ===============================
# DATOS REALISTAS
# ===============================
FIRST_NAMES = ["Juan", "Maria", "Carlos", "Ana", "Luis", "Laura", "Pedro", "Sofia"]
LAST_NAMES = ["Perez", "Gomez", "Rodriguez", "Lopez", "Martinez", "Garcia"]

CITIES = [
    ("Bogotá", "Cundinamarca"),
    ("Medellín", "Antioquia"),
    ("Cali", "Valle del Cauca"),
    ("Barranquilla", "Atlántico"),
    ("Lima", "Lima"),
    ("Ciudad de México", "CDMX"),
    ("Santiago", "RM"),
    ("Buenos Aires", "BA")
]


def generate_name():
    return random.choice(FIRST_NAMES), random.choice(LAST_NAMES)


def generate_document():
    return str(random.randint(10000000, 99999999))


def generate_segment():
    """
    Distribución realista de segmentos
    """
    return np.random.choice(
        ["BASICO", "ESTANDAR", "PREMIUM", "ELITE"],
        p=[0.4, 0.35, 0.2, 0.05]
    )


def generate_score():
    return int(np.clip(np.random.normal(650, 100), 300, 900))


def generate_amount():
    """
    Distribución log-normal para simular dinero real
    """
    return round(np.random.lognormal(mean=10, sigma=1), 2)


def generate_small_amount():
    return round(np.random.lognormal(mean=8, sigma=1), 2)


def generate_city():
    return random.choice(CITIES)


# ===============================
# ANOMALÍAS (CLAVE PARA EVALUACIÓN)
# ===============================
def inject_null(value, prob=0.05):
    if random.random() < prob:
        return None
    return value


def inject_duplicate(df, prob=0.01):
    """
    Duplica registros intencionalmente
    """
    duplicates = df.sample(frac=prob)
    return duplicates


def inject_outlier(value, prob=0.01):
    """
    Genera valores extremos
    """
    if random.random() < prob:
        return value * random.randint(5, 20)
    return value


def inject_invalid_date(date, prob=0.01):
    """
    Fechas fuera de rango
    """
    if random.random() < prob:
        return date + timedelta(days=random.randint(365, 1000))
    return date


# ===============================
# TRANSFORMACIONES AUXILIARES
# ===============================
def calculate_age(birth_date):
    today = datetime.today()
    return today.year - birth_date.year


def map_segment(segment_code):
    mapping = {
        "BASICO": "Básico",
        "ESTANDAR": "Estándar",
        "PREMIUM": "Premium",
        "ELITE": "Elite"
    }
    return mapping.get(segment_code, "Desconocido")


def generate_channel():
    return np.random.choice(
        ["APP", "WEB", "ATM", "OFICINA"],
        p=[0.5, 0.3, 0.1, 0.1]
    )


def generate_transaction_type():
    return random.choice(["DEBITO", "CREDITO"])


def generate_product_type():
    return np.random.choice(
        ["CREDITO", "AHORRO", "TRANSACCIONAL"],
        p=[0.5, 0.3, 0.2]
    )


# ===============================
# FECHAS CONFIGURABLES
# ===============================
def get_date_range(months=12):
    end_date = datetime.today()
    start_date = end_date - timedelta(days=30 * months)
    return start_date, end_date


# ===============================
# LOGGING SIMPLE
# ===============================
def log(message):
    print(f"[{datetime.now()}] {message}")