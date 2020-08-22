#!/usr/bin/env sh

apt update
apt -y install gcc-mingw-w64
rustup update

rustup target add x86_64-unknown-linux-musl
cargo install --force svgbob_cli --root=svgbob --target=x86_64-unknown-linux-musl

rustup target add x86_64-pc-windows-gnu
cargo install --force svgbob_cli --root=svgbob_win --target=x86_64-pc-windows-gnu

rustup target add x86_64-apple-darwin
cargo install --force svgbob_cli --root=svgbob_osx --target=x86_64-apple-darwin
