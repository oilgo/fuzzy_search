# FuzzySearch
An algorithm that helps users search for information they need and suggests similar variants.

## Getting started
1. Creave venv
```bash
python -m venv venv
python3 -m venv venv
```

2. Select interpreter
```bash
Left Ctrl + Left Shift + P 
> Select Interpreter
```

3. Create .env based on ENV.settings

4. Install requirements
```bash
pip install -r requirements.txt
```

## Usefull commands
1. Run server
```bash
python manage.py runserver
```

2. Make migration
```bash
python manage.py makemigrations
```

3. Migrate
```bash
python manage.py migrate
```

4. Create/Update requirements
```bash
pip freeze > requirements.txt
```