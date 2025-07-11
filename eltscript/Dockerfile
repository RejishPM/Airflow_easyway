FROM python:3.11-slim

# Install dependencies and PostgreSQL 17 client
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        gnupg \
        ca-certificates && \
    curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/postgres.gpg && \
    echo "deb http://apt.postgresql.org/pub/repos/apt $(. /etc/os-release && echo $VERSION_CODENAME)-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-client-17 \
        gcc \
        libpq-dev \
        python3-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set up virtual environment
ENV VENV_PATH="/opt/venv"
RUN python3 -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Install Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir psycopg2-binary

# Copy your app
WORKDIR /app
COPY elt_script.py .

# Run script
CMD ["python", "elt_script.py"]
