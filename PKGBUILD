pkgname=container-cargo
pkgver=1.0.0
pkgrel=1
pkgdesc="ContainerCargo is a Python program for export, and eventually sync on cloud, containers."

arch=('x86_64')

depends=('python' 'python-requests')

makedepends=('pyinstaller')

url="https://github.com/Iaio99/ContainerCargo"
license=('AGPL')

source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('ce7d6b3efab844003bbcb8469a0c7366a4ca25607ee3f6d21ce2e7cbb3b18873')

check() {
  cd "$pkgname-$pkgver"

  # no test to run
}

build() {
  cd "$pkgname-$pkgver"
  make
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 dist/$pkgname "$pkgdir/usr/local/bin/$pkgname"
  install -Dm644 config.ini.example "$pkgdir/etc/$pkgname/config.ini"
}