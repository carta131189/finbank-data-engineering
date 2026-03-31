variable "location" {
  default = "East US"
}

variable "env" {}

variable "resource_group_name" {}

variable "storage_account_name" {}

variable "container_names" {
  type = list(string)
  default = ["bronze", "silver", "gold"]
}