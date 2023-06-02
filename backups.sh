#!/bin/bash

source_location="/path/source"

backup_location="/path/backup"

backup_rotation=10

backup_name="backup-$(date +%Y-%m-%d).tar.gz"

backup_file_location="${backup_location}/${backup_name}"

tar -czf "${backup_file_location}" "${source_location}"

find "${backup_directory}" -maxdepth 1 -name "backup-*" -type f -mtime +7 -exec rm -r {} +