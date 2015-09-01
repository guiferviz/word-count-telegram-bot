#!/bin/sh

LIB_DIR="./lib"

# Download all packages to LIB_DIR
pip install --upgrade --target=$LIB_DIR -r requirements.txt

echo "Build finished!"
