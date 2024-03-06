#!/usr/bin/env bash
python3 -m venv .venv

activate () {
    . .venv/bin/activate
}

activate

pip3 install -r api/requirements.txt
pip3 install -r frontend/requirements.txt

