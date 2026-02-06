# ptctools - Portainer Client Tools

CLI for managing Portainer stacks, volume backups, and database operations.

> **Note:** Only tested on Portainer 2.33.6

## Installation

```bash
# From Git repository
uv tool install git+https://github.com/tamntlib/ptctools.git
# or
uv tool install ptctools --from git+https://github.com/tamntlib/ptctools.git

# From local path
uv tool install openapi-generator-cli==7.19.0
openapi-generator-cli generate \
  -i portainer_openapi.yml \
  -g python \
  -o ./src/ptctools/portainer_client \
  --skip-validate-spec \
  --additional-properties=generateSourceCodeOnly=true
uv tool install . --no-cache --reinstall
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `PORTAINER_URL` | Yes* | Portainer base URL (can also use `-u` flag) |
| `PORTAINER_ACCESS_TOKEN` | Yes | Portainer API key |
| `S3_ACCESS_KEY` | For S3 | S3 access key |
| `S3_SECRET_KEY` | For S3 | S3 secret key |
| `S3_ENDPOINT` | For S3 | S3/MinIO endpoint URL |
| `DUPLICATI_PASSPHRASE` | No | Backup encryption passphrase |

\* Required for `docker` commands. Can be provided via `-u` flag instead.

## Usage

```bash
# Set environment variables
export PORTAINER_URL=https://portainer.example.com
export PORTAINER_ACCESS_TOKEN=your-api-key
export S3_ACCESS_KEY=your-s3-key
export S3_SECRET_KEY=your-s3-secret
export S3_ENDPOINT=https://s3.<region>.amazonaws.com

# Stack deployment (Swarm-only)
ptctools docker stack deploy -n mystack -f compose.yaml

# Secret management (Swarm-only)
echo "postgresql://user:pass@db:5432/mydb" | ptctools docker secret create db_dsn
ptctools docker secret create -f /path/to/secret.txt my_secret
ptctools docker secret create -v "secret-value" my_secret

# Config management (Swarm-only)
ptctools docker config set -n my-config -d "config content"
ptctools docker config set -n nginx.conf -f ./nginx.conf
ptctools docker config set -n my-config -d "new content" --force
ptctools docker config list
ptctools docker config get -n my-config
ptctools docker config delete -n my-config

# Volume backup/restore (uses Duplicati)
ptctools docker volume backup -v vol1,vol2 -o s3://mybucket
ptctools docker volume restore -i s3://mybucket/vol1  # volume name derived from URI path
ptctools docker volume restore -v vol1 -i s3://mybucket/vol1  # explicit volume name

# Volume copy (raw copy using mc/busybox)
ptctools docker volume cp source dest                         # volume to volume
ptctools docker volume cp s3://mybucket/path dest              # S3 to volume
ptctools docker volume cp source s3://mybucket/path            # volume to S3

# Volume management
ptctools docker volume rm myvolume                             # remove volume (with confirmation)
ptctools docker volume rm -y myvolume                          # remove without confirmation
ptctools docker volume rename old_name new_name                # rename volume (copy + delete)

# Database backup/restore (uses minio/mc for S3)
ptctools docker db backup -c container_id -v db_data \
  --db-user postgres --db-name mydb -o backup.sql.gz
ptctools docker db backup -c container_id -v db_data \
  --db-user postgres --db-name mydb -o s3://mybucket/backups/db.sql.gz

ptctools docker db restore -c container_id -v db_data \
  --db-user postgres --db-name mydb -i backup.sql.gz
ptctools docker db restore -c container_id -v db_data \
  --db-user postgres --db-name mydb -i s3://mybucket/backups/db.sql.gz

# Override PORTAINER_URL with -u flag
ptctools docker secret create -u https://other.portainer.com -f dsn.txt my_secret

# Utils - local Duplicati operations (no Portainer needed)
ptctools utils backup --input ./data --output s3://backups/mydata
ptctools utils restore --input s3://backups/mydata --output ./restored

```

## CLI Structure

```
ptctools
├── docker                    # Docker commands (via Portainer Docker proxy)
│   ├── stack deploy         # Deploy/update stack (Swarm-only)
│   ├── secret create        # Create Docker secret (Swarm-only)
│   ├── config set/get/list/delete  # Manage configs (Swarm-only)
│   ├── volume backup/restore/cp/rm/rename
│   └── db backup/restore
├── utils backup/restore     # Local Duplicati operations
└── k8s ...                  # Kubernetes commands (future)
```

## Commands

### `ptctools docker stack deploy`
Deploy or update a Docker Swarm stack in Portainer.

### `ptctools docker secret create`
Create a Docker Swarm secret. Value can be provided via stdin, file, or command-line argument.

### `ptctools docker config set/get/list/delete`
Manage Docker Swarm configs via Portainer API.

### `ptctools docker volume backup/restore`

- **backup**: Backup multiple Docker volumes (comma-separated) to S3 using Duplicati container.
- **restore**: Restore a single Docker volume from S3. Volume name can be specified via `--volume` or derived from the input URI path.

### `ptctools docker volume cp`
Copy data between volumes and S3 (raw file copy).
- **volume to volume**: Uses `busybox` with `cp -a`
- **S3 to volume**: Uses `minio/mc` to download files
- **volume to S3**: Uses `minio/mc` to upload files

### `ptctools docker volume rm`
Remove a Docker volume. Use `-y` to skip confirmation, `-f` to force removal.

### `ptctools docker volume rename`
Rename a volume by copying data to a new volume and deleting the original.

### `ptctools docker db backup/restore`
Backup/restore PostgreSQL database. Supports both local files and S3 URIs.
- Uses `pg_dump`/`psql` for database operations
- Uses `minio/mc` container for S3 transfers

### `ptctools utils backup/restore`
Local backup/restore operations using Duplicati CLI (docker or local). Does not require Portainer.
