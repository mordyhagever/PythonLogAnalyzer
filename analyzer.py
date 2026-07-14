from config import *
import csv
def count_ip():
    data = get_file("network_traffic.log")
    ip_type = []
    for row in data:
        if row[1] not in ip_type:
            ip_type.append(row[1])
    count = dict.fromkeys(ip_type,0)
    for row in data:
        ip = row[1]
        if ip in count:
            count[ip] += 1
    return count
print(count_ip())


