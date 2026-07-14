from reader import *
def external_ip():
    data = get_file("network_traffic.log")
    good_numbers = ("192.168", "10.")
    external = [row for row in data if not row[1].startswith(good_numbers)]
    return external
#print(*external_ip(), sep="\n")

def bad_port():
    data = get_file("network_traffic.log")
    bad_numbers = ("22", "23", "3389")
    sensitive = [row for row in data if row[3] in bad_numbers]
    return sensitive

#print(*bad_port(), sep="\n")

def size_check():
    data = get_file("network_traffic.log")
    big_size = [row for row in data if int(row[5]) > 5000]
    return big_size
#print(*size_check(), sep="\n")

def check_large():
    data = get_file("network_traffic.log")
    pass