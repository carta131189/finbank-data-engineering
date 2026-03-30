# Proyecto de Ingeniería de Datos – FinBank

## Descripción General

Proyecto end-to-end de ingeniería de datos que simula un ecosistema financiero, generando datos sintéticos con comportamientos realistas y anomalías para casos de uso analíticos y detección de fraude.

---

## Objetivo

Diseñar e implementar un pipeline de datos que permita:

* Análisis de riesgo crediticio
* Detección de fraude
* Análisis de comportamiento de clientes
* Validación de calidad de datos

---

## Arquitectura (Implementación Actual)

```
Generación de Datos → CSV / Parquet → Validación → Simulación de Carga
```

* Generación de datos sintéticos usando Python
* Almacenamiento en formatos CSV y Parquet
* Validación automática de calidad de datos
* Simulación de carga mediante pandas

---

## Modelo de Datos

El proyecto incluye 6 tablas principales:

* **TB_CLIENTES_CORE** → Información de clientes
* **TB_PRODUCTOS_CAT** → Catálogo de productos
* **TB_MOV_FINANCIEROS** → Transacciones (con fraude y anomalías)
* **TB_OBLIGACIONES** → Créditos / obligaciones financieras
* **TB_COMISIONES_LOG** → Registro de comisiones
* **TB_SUCURSALES_RED** → Red de sucursales

Diagrama Entidad-Relación disponible en:

```
/docs/ER_FinBank.png
```

---

## Funcionalidades Clave

* Generación reproducible mediante semilla aleatoria
* Configuración dinámica usando YAML
* Distribuciones financieras realistas
* Simulación de anomalías:

  * Transacciones fraudulentas
  * Registros duplicados
  * Valores negativos
  * Fechas inconsistentes
* Validación automática con pandas
* Exportación en múltiples formatos (CSV y Parquet)

---

## Validación de Datos

Se implementó un script de validación que permite:

* Validar cantidad de registros por tabla
* Detectar duplicados
* Analizar valores nulos

Ejecutar:

```bash
python validate_data.py
```

---

## Ejecución

### 1. Generar datos

```bash
python generate_data.py
```

### 2. Simular carga

```bash
python load_data.py
```

### 3. Validar datos

```bash
python validate_data.py
```

---

## Evidencia

* Logs de carga:

```
/docs/evidencia_carga.png
```

* Diagrama ER:

```
/docs/er_diagram.png
```

---

## Tecnologías Utilizadas

* Python (Pandas, NumPy)
* YAML (configuración)
* Git (control de versiones)

---

## Notas

Debido a limitaciones en el entorno (Azure Free Tier), la solución se implementó de forma local, incluyendo una simulación del proceso de carga en lugar de una integración real con servicios en la nube.

---

## Habilidades Demostradas

* Modelado de datos (diseño ER)
* Generación de datos sintéticos
* Validación de calidad de datos
* Diseño de pipelines (mentalidad ETL)
* Manejo de anomalías y consistencia de datos

---

## Próximas Mejoras

* Integración con Azure Data Factory
* Despliegue en Azure Data Lake / SQL Server
* Implementación de arquitectura Medallion (Bronze, Silver, Gold)
* Orquestación de pipelines

---

