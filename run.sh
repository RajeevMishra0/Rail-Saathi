#!/bin/bash
source .venv/Scripts/activate
gunicorn app.app:app --workers 3