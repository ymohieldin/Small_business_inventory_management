# Management Handmade

A Django web application for managing handmade products business, tracking materials, products, and profits.

## Features

- Dashboard with key metrics
- Material management (CRUD operations)
- Product management (CRUD operations)
- Material assignment to products
- Cost and profit calculations
- Image upload support
- Modern Bootstrap 5 interface

## Requirements

- Python 3.8+
- Django 5.0+
- Pillow (for image handling)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/management_handmade.git
cd management_handmade
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 to access the application.

## Usage

1. Log in as admin
2. Add materials with prices and quantities
3. Create products and set selling prices
4. Assign materials to products
5. View dashboard for business insights

## Project Structure

```
management_handmade/
├── inventory/              # Main app
│   ├── migrations/        # Database migrations
│   ├── templates/        # HTML templates
│   ├── forms.py         # Form definitions
│   ├── models.py        # Database models
│   ├── urls.py          # URL configurations
│   └── views.py         # View functions
├── static/               # Static files
│   └── css/
│       └── style.css    # Custom styles
├── media/               # Uploaded files
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
