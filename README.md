# FastAPI Project

## Description
This is a FastAPI-based project that provides a robust API structure with database integration, dependency injection, and containerization support.

## Features
- FastAPI framework for high-performance API development
- Beanie ODM for MongoDB integration
- Pydantic for data validation
- Docker support for easy deployment
- Makefile for common development tasks

## How to run
1. Clone the repository:
   ```bash
   git clone http://git.sharifict.ir/shahriarshm/interactor-widget-service.git
   cd interactor-widget-service
   ```

2. Run the project with docker:
   ```bash
   docker compose up -d
   ```

## Usage
To run the project locally:
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the API documentation:
   Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

## Documentation
For detailed information about the project structure, installation, usage, and API reference, please refer to the [project documentation](docs/README.md).
