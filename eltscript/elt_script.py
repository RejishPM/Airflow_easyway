import subprocess
import time

def wait_for_postgres(host, max_retries=5, delay_seconds=5):
    retries = 0
    while retries < max_retries:
        try:
            result = subprocess.run(
                ["pg_isready", "-h", host],
                check=True, capture_output=True, text=True
            )
            if "accepting connections" in result.stdout:
                print(f"{host} is ready.")
                return True
        except subprocess.CalledProcessError as e:
            print(f"Error checking {host}: {e.stderr.strip()}")
            retries += 1
            print(f"{host} not ready. Retrying in {delay_seconds}s... ({retries}/{max_retries})")
            time.sleep(delay_seconds)
    print(f"Failed to connect to {host} after {max_retries} attempts.")
    return False

# Wait for both source and target DBs
if not wait_for_postgres("source_postgres"):
    exit(1)
if not wait_for_postgres("target_postgres"):
    exit(1)

print("Starting ELT script...")

source_config = {
    'dbname': 'source_db',
    'user': 'postgres',
    'password': 'postgres',  
    'host': 'source_postgres'
}

destination_config = {
    'dbname': 'destination_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'target_postgres'  
    }

# Dump from source
dump_command = [
    'pg_dump',
    '-h', source_config['host'],
    '-U', source_config['user'],
    '-d', source_config['dbname'],
    '-f', 'data_dump.sql',
    '-w'
]
try:
    result = subprocess.run(
        dump_command,
        env={'PGPASSWORD': source_config['password']},
        check=True,
        capture_output=True,  
        text=True             # <-- Decode bytes to string
    )
except subprocess.CalledProcessError as e:
    print("pg_dump failed with error:")
    print(e.stderr)  # <-- Now this will actually have content
    exit(1)


# Restore to target
load_command = [
    'psql',
    '-h', destination_config['host'],
    '-U', destination_config['user'],
    '-d', destination_config['dbname'],
    '-a', '-f', 'data_dump.sql'
]
subprocess.run(load_command, env={'PGPASSWORD': destination_config['password']}, check=True)

print("ELT process completed successfully.")
