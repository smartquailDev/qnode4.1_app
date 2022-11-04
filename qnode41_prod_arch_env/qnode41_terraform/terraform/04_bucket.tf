resource "digitalocean_spaces_bucket" "qnd41-static" {
  name   = "qnd41-staticfiles"
  region = "sfo3"
  acl = "public-read"
}

