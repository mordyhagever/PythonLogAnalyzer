from config import *
import csv

#returning a dictionary of the IP's and how many times they appear
def count_ip():
    data = get_file("network_traffic.log")
    ip_list = [code[1] for code in data]
    ip_counts = {ip: ip_list.count(ip) for ip in ip_list}
    return ip_counts
#print(count_ip())

#returning a dictionary of the Ports and how many times they appear
def count_port():
    data = get_file("network_traffic.log")
    port_list = [code[3] for code in data]
    port_count = {port: port_list.count(port) for port in port_list}
    return port_count
#print(count_port())


