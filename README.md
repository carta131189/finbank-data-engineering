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

## Arquitectura del Pipeline


```
* Generación de Datos → CSV / Parquet → Validación → Simulación de Carga
* **Bronze**: Ingesta de datos crudos desde SQL a ADLS en formato Parquet
* **Silver**: Transformaciones y limpieza mediante Data Flows en ADF
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

## Pipelines y Datasets

### Pipelines

* **pl_bronze_ingestion** → Copia datos de SQL a ADLS (Bronze)
* **pl_silver_all_dataflows_parallel** → Ejecuta Data Flows de limpieza y transformación (Silver)

### Datasets

* **ds_sql_source** → Origen en Azure SQL
* **ds_bronze_parquet** → Datos crudos en Bronze
* **ds_silver_parquet** → Datos transformados en Silver

---

## Ejecución de Pipelines

1. Publicar pipelines en Azure Data Factory
2. Ejecutar pipeline Bronze: `pl_bronze_ingestion`
3. Ejecutar pipeline Silver: `pl_silver_all_dataflows_parallel`

---

## Evidencia

* Pipelines exportados: `/pipelines/pl_bronze_ingestion.json`, `/pipelines/pl_silver_all_dataflows_parallel.json`
* Data Flows: `/dataflows/df_silver_clientes.json`, `/dataflows/df_silver_comisiones.json`, `/dataflows/df_silver_cmovimientos.json`, `/dataflows/df_silver_obligaciones.json`, `/dataflows/df_silver_productos.json`, `/dataflows/df_silver_sucursales.json`.
* Datasets: `/Datasets/ds_silver_clientes.json`, `/Datasets/ds_silver_comisiones.json`, `/Datasets/ds_silver_movimientos.json`, `/Datasets/ds_silver_obligaciones.json`, `/Datasets/ds_silver_productos.json`, `/Datasets/ds_silver_sucursales.json`,`/Datasets/ds_bronze_clientes.json`, `/Datasets/ds_bronze_comisiones.json`, `/Datasets/ds_bronze_movimientos.json`, `/Datasets/ds_bronze_obligaciones.json`, `/Datasets/ds_bronze_productos.json`, `/Datasets/ds_bronze_sucursales.json`.
* Logs de carga: `/docs/evidencia_carga.png`
* Diagrama ER: `/docs/ER_FinBank.png`
* Carga bronze: `/docs/Carga_datos_adf_pipeline.png`
* Carga Silver: `/docs/Carga_silver.png`
* Pipeline bronze: `/docs/evidencia_adf_pipeline.png`
* Carpetas bronze: `/docs/evidencia_storage.png`
* Carga datos: `/docs/Validacion de datos.png`
* Terraform: `/docs/evidencia_terraform_plan.png`

---

## Tecnologías Utilizadas

* Python (Pandas, NumPy)
* YAML (configuración)
* Git (control de versiones)
* Azure Data Factory (pipelines y dataflows)
* Azure Data Lake Storage Gen2
* Git (control de versiones)

---

## Habilidades Demostradas

* Modelado de datos (diseño ER)
* Generación de datos sintéticos
* Validación de calidad de datos
* Diseño de pipelines (mentalidad ETL)
* Manejo de anomalías y consistencia de datos

---

## Próximas Mejoras

* Orquestación completa de pipelines con triggers en ADF
* Monitoreo y alertas de fallos de carga
* Integración con Power BI o dashboards analíticos
* Generación de reportes automáticos desde capa Gold

---

