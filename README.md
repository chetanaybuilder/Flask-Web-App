# Project Name

A modern, responsive portfolio application built with Python and Flask. This project showcases my skills, projects, and learning journey in software development.

> **Note**: This is my learning repository. I understand many fundamentals of web development and this project represents my progression from a beginner's Flask script to a professionally structured web application.

## Overview

This application serves as a personal portfolio, displaying information such as skills, hobbies, and completed projects. It demonstrates the ability to build a web application using Flask with a clean, maintainable architecture, separating logic from presentation, and following best practices for Python web development.

## Features

- **Modern UI**: Clean, responsive design with CSS custom properties and flexbox/grid layouts.
- **Application Factory**: Built using the Flask application factory pattern for scalability.
- **Blueprints**: Routes are organized using Flask Blueprints.
- **Environment Configuration**: Secure configuration management using environment variables.
- **Custom Error Handling**: Professional 404 and 500 error pages.
- **Testing**: Includes a test suite written with `pytest`.
- **CI/CD**: GitHub Actions workflow for automated testing.

## Tech Stack

- Python
- Flask
- HTML5
- CSS3
- pytest

## Architecture

The project follows a standard professional Flask directory structure:

```
Flask-Web-App/
├── app/
│   ├── __init__.py       # Application factory
│   ├── routes/           # Blueprints and route handlers
│   ├── templates/        # Jinja2 HTML templates
│   └── static/           # CSS, JS, and image assets
├── tests/                # Test suite
├── config.py             # Configuration classes
├── run.py                # Application entry point
├── requirements.txt      # Project dependencies
└── .env.example          # Example environment variables
```

## Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/chetanaybuilder/Flask-Web-App.git
   cd Flask-Web-App
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   *(Edit `.env` to add your specific configuration if necessary)*

### Running the Application

To start the development server, run:
```bash
python run.py
```
Alternatively, using the Flask CLI:
```bash
flask --app run run --debug
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Environment Variables

| Variable | Description | Default (Dev) |
|----------|-------------|---------------|
| `FLASK_ENV` | Application environment (`dev`, `test`, `prod`) | `dev` |
| `SECRET_KEY` | Cryptographic key for sessions and tokens | (Required in production) |

*Never commit real secrets or `.env` files to version control.*

## Testing

This project uses `pytest` for testing. To run the test suite:

```bash
pytest
```

Tests validate route availability, HTML rendering, and custom error handlers.

## Development

Contributions are welcome! If you'd like to improve the application:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Ensure all tests pass.
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a Pull Request.

## Security

- Configuration differentiates between development, testing, and production environments.
- `DEBUG` is strictly disabled in production.
- Secrets are loaded from the environment and not hardcoded.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
