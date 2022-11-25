# Creamos un dominio nuevo
resource "digitalocean_domain" "smartquail" {
  name = "smartquail.io"
  ip_address = digitalocean_droplet.QNODE41.ipv4_address
}

# Add a record to the domain
resource "digitalocean_record" "www" {
  domain = "${digitalocean_domain.smartquail.name}"
  type   = "A"
  name   = "smartquail"
  ttl    = "50"
  value  = "${digitalocean_droplet.QNODE41.ipv4_address}"
}

