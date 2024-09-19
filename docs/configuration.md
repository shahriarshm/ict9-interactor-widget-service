# Configuration

This project uses environment variables for configuration. The main configuration is handled in `app/config.py`.

## Environment Variables

- `DATABASE_URL`: The connection string for the database
- `SECRET_KEY`: Secret key for JWT token generation
- `ALGORITHM`: Algorithm used for JWT token (default: "HS256")
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Expiration time for access tokens in minutes

## Setting Up Environment Variables

1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and fill in the required values.

## Configuration in Docker

When using Docker, environment variables can be set in the `docker-compose.yml` file under the `environment` section for the app service.

## Accessing Configuration in Code

Configuration values can be accessed in the code by importing from `app.config`:

```python
from app.config import settings

database_url = settings.DATABASE_URL
```

Always use the `settings` object to access configuration values throughout the application to ensure consistency and ease of management.