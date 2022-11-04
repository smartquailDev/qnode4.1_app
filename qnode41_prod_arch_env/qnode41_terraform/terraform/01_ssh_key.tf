#
# Exportamos nuestra key SSH

resource "digitalocean_ssh_key" "qnode41" {
  name       = "qnode41"
  public_key = "${file("id_rsa.pub")}"
}

