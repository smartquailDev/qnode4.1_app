variable "digitalocean_token" {
  description = "Digital Ocean Token:qnode41"
  default     = "dop_v1_b497b4e3d2cb55108bedc815aba33fe93bd620fa679340233b68320200146f4d"
}

variable "spaces_access_id" {
  description = "Digital Ocean Spaces Acees ID"
  default     = "DO0064XX2WKMXAWNB3NT"
}
variable "spaces_secret_key" {
  description = "Digital Ocean Spaces Secret Key"
  default     = "m4oyT+RU72iYp7wjOXIYQ7MM5ZgFjiU81QlNhj6WXUw"
}

terraform {
  required_version = ">= 0.14.0"  
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
    }
  }
}

# Configure the DigitalOcean Provider

provider "digitalocean" {
  token = var.digitalocean_token
  spaces_access_id  = var.spaces_access_id
  spaces_secret_key = var.spaces_secret_key
}



