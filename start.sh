#!/bin/bash

set -e

# TODO: make this install deps and start properly
node server.js
python api/api.py
