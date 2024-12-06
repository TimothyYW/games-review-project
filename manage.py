#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

def main():
    """Run administrative tasks."""
    # Build paths inside the project
    BASE_DIR = Path(__file__).resolve().parent

    # Default settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Add the project directory to the sys.path
    sys.path.append(str(BASE_DIR))
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
