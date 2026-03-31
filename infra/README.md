# Infraestructura como Código – FinBank

## Descripción

Este módulo define la infraestructura necesaria para soportar el pipeline de datos utilizando Terraform sobre Azure.

---

## Herramienta utilizada

Terraform fue seleccionado por ser una herramienta estándar de Infraestructura como Código (IaC), que permite despliegues reproducibles, versionamiento y escalabilidad en entornos cloud.

---

## Recursos Aprovisionados

* Resource Group
* Storage Account (Azure Data Lake Gen2)
* Contenedores:

  * bronze → datos crudos
  * silver → datos procesados
  * gold → capa analítica

---

## Entornos

Se soportan múltiples entornos mediante archivos de variables:

* dev → terraform.tfvars
* prod → terraform.tfvars.prod

---

## Despliegue

```bash
cd infra

terraform init
terraform plan -var-file="terraform.tfvars"
terraform apply -var-file="terraform.tfvars"
```

---

## Outputs

El módulo exporta:

* Nombre del Resource Group
* Nombre del Storage Account
* Lista de contenedores

---

## Resultado

Infraestructura base lista para soportar arquitectura tipo Medallion (Bronze, Silver, Gold).
