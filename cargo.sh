#!/usr/bin/env sh

rustup target add x86_64-unknown-linux-musl
cargo install --force svgbob_cli --root=svgbob --target=x86_64-unknown-linux-musl
