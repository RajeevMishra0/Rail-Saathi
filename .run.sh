#!/bin/bash
source .venv/Scripts/activate
pip install -r requirements.txt
gunicorn app.app:app