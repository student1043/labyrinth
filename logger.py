import sys
import re
from collections import Counter


def analyzer(log_path):
    with open(log_path, 'r') as file:
        logger = file.readlines()
    
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    logged_ips = []

    for line in logger:
        match = pattern.search(line)
        if match:
            logged_ips.append(match.group())

    counted_ips = Counter(logged_ips)

    sorted_ips = sorted(counted_ips.items(), key=lambda x: x[1], reverse=True)

    print(sorted_ips)


file_path = sys.argv[1]
analyzer(file_path)
