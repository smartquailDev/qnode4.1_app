#
# Creamos el droplet

resource "digitalocean_droplet" "QNODE41" {
  image     = "ubuntu-22-04-x64"
  name      = "QNODE41"
  region    = "sfo3"
  size      = "s-2vcpu-2gb"
  user_data = "${file("docker.yaml")}"
  ssh_keys  = ["${digitalocean_ssh_key.qnd41.fingerprint}"]
}
