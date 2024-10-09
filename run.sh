#!/bin/bash
source .venv/Scripts/activate
gunicorn app.app:app