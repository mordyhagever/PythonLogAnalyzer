from reader import *
def external_ip():
    data = get_file("network_traffic.log")
    good_numbers = ("192.168", "10.")
    external = [row for row in data if not row[1].startswith(good_numbers)]
    return "\n".join([str(row) for row in external])
print(external_ip())

