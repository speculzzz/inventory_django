# Django Inventory Project

This is a test django project done according to the [tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/). 
It is a part of Homework 8 for the OTUS course and is intended for educational purposes.

## Features

- **Backend**: Django 5.2
- **Database**: PostgreSQL 13
- **Cache**: Redis 6
- **Web Server**: Nginx
- **ASGI**: Gunicorn
- **MIT License**: Open-source and free to use.

## Requirements

- Python 3.11+
- Django 5.2+
- Docker 20.10+
- Docker Compose 2.0+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/speculzzz/inventory_django.git
   cd inventory_django
   ```
2. Create virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the application in development mode  

```bash
make runserver
```
### Emulate the application in the production   

```bash
cp .env.prod.example .env.prod
... setup .env.prod ...
make production
```

### Testing

Run the pytest:
```bash
make test
```
Checking test coverage
```bash
make coverage
```

## License

MIT License. See [LICENSE](LICENSE) for details.

## Author

- **speculzzz** (speculzzz@gmail.com)

---

Feel free to use it!
