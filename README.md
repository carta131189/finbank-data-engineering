# FinBank Data Engineering Project

##  Overview
Proyecto de ingeniería de datos basado en arquitectura Medallion (Bronze, Silver, Gold) usando Azure Data Factory.

##  Objetivo
Construir un pipeline end-to-end que permita:
- Análisis de riesgo crediticio
- Detección de fraude
- Cálculo de CLTV
- KPIs regulatorios

##  Plataforma
- Microsoft Azure
- Azure Data Factory
- Azure Data Lake Gen2

##  Arquitectura
- Bronze: datos crudos
- Silver: datos limpios y validados
- Gold: modelo analítico

##  Estructura del repositorio
- infra/: infraestructura como código
- data-generation/: generación de datos sintéticos
- pipelines/: transformaciones
- orchestration/: orquestación ADF
- docs/: documentación

##  Estado actual
✔ Estructura del proyecto creada  
✔ Generación de datos sintéticos en desarrollo  

##  Próximos pasos
- Completar data-generation
- Implementar Bronze en ADF
- Infraestructura con Terraform