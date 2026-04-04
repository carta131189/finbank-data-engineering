# Changelog – Proyecto Ingeniería de Datos FinBank

Todos los cambios importantes en este proyecto se documentan en este archivo.  
Se sigue la convención de [Keep a Changelog](https://keepachangelog.com/) y versionamiento semántico (MAJOR.MINOR.PATCH).

---

## [1.0.0] – 2026-04-03
### Added
- **Pipelines ADF**:
  - `pl_bronze_ingestion` → Ingesta de datos crudos desde Azure SQL a ADLS (Parquet).
  - `pl_silver_all_dataflows_parallel` → Ejecución de Data Flows para limpieza y transformación (Silver).
  - `pl_gold_reporting` → Agregaciones, métricas y preparación de datos para análisis (Gold).
- **Data Flows Silver**:
  - `df_silver_clientes`, `df_silver_obligaciones`, `df_silver_movimientos`, `df_silver_comisiones`, `df_silver_productos`, `df_silver_sucursales`.
- **Datasets principales**:
  - `ds_sql_source`, `ds_bronze_parquet`, `ds_silver_<tabla>`, `ds_gold_<tabla>`.
- **Scripts Python**:
  - `generate_data.py` → Generación de datos sintéticos con comportamientos financieros y anomalías.
  - `load_data.py` → Simulación de carga de datos a ADLS / Azure SQL.
  - `validate_data.py` → Validación automática de calidad de datos (duplicados, nulos, consistencia).
- **Modelo de datos**:
  - 6 tablas principales: `TB_CLIENTES_CORE`, `TB_PRODUCTOS_CAT`, `TB_MOV_FINANCIEROS`, `TB_OBLIGACIONES`, `TB_COMISIONES_LOG`, `TB_SUCURSALES_RED`.
  - Diagrama ER disponible en `/docs/ER_FinBank.png`.
- **Documentación**:
  - README.md actualizado con descripción completa de pipelines, datasets y evidencia.
  - Evidencias de ejecución y logs agregados en `/docs`.

### Changed
- README.md mejorado para reflejar arquitectura end-to-end: Bronze → Silver → Gold.
- Evidencias visuales de carga y transformaciones agregadas.

### Fixed
- Ajustes menores en validación de datos para tablas con valores negativos y duplicados.

---

## [0.2.0] – 2026-03-28
### Added
- Scripts iniciales para generación de datos sintéticos financieros.
- Simulación de anomalías:
  - Transacciones fraudulentas.
  - Registros duplicados.
  - Valores negativos.
  - Fechas inconsistentes.
- Exportación de datos en formatos CSV y Parquet.
- Validación de calidad básica con Pandas.

### Changed
- Configuración dinámica de parámetros mediante YAML.
- Inclusión de logs de ejecución en archivos de evidencia.

### Fixed
- Problemas de formato en CSV (valores nulos y fechas inconsistentes).

---

## [0.1.0] – 2026-03-25
### Added
- Estructura inicial del proyecto.
- Primeros scripts de generación de datos de clientes y productos.
- Diseño inicial del modelo de datos (ER).
- Configuración inicial de repositorio Git.