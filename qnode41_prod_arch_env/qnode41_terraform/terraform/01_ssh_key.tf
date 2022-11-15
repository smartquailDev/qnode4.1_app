#
# Exportamos nuestra key SSH

resource "digitalocean_ssh_key" "qnd41" {
  name       = "qnd41"
  public_key = "${file("id_rsa.pub")}"
}

