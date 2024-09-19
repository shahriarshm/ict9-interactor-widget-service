# Installation Instructions

1. Clone the repository:
   ```bash
   git clone http://git.sharifict.ir/shahriarshm/interactor-widget-service.git
   cd interactor-widget-service
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Copy the `.env.example` file to `.env` and fill in the required values.

5. Initialize the database:
   ```bash
   alembic upgrade head
   ```

## Docker Installation
If you prefer using Docker:

1. Make sure Docker and Docker Compose are installed on your system.
2. Run:
   ```bash
   docker-compose up --build
   ```

This will build the Docker image and start the containers for the application and the database.