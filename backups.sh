#!/bin/bash

source_location="logger.py"

backup_location="./backups"

backup_rotation=10

backup_name="backup-$(date +%Y-%m-%d).tar.gz"

backup_file_location="${backup_location}/${backup_name}"

tar -czf "${backup_file_location}" "${source_location}"

find "${backup_location}" -maxdepth 1 -name "backup-*" -type f -mtime +7 -exec rm -r {} +