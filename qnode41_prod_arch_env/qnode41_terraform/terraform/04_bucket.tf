resource "digitalocean_spaces_bucket" "qnd41-staticfiles" {
  name   = "qnd41-staticfiles"
  region = "sfo3"
  acl = "public-read"
}

