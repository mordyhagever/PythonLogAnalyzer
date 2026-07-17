from reader import *



#checking and returning bad external IP's
def external_ip():
    data = get_file("network_traffic.log")
    good_numbers = ("192.168", "10.")
    external = [row for row in data if not row[1].startswith(good_numbers)]
    return external
#print(*external_ip(), sep="\n")

#checking and returning bad ports
def bad_port():
    data = get_file("network_traffic.log")
    bad_numbers = ("22", "23", "3389")
    sensitive = [row for row in data if row[3] in bad_numbers]
    return sensitive

#print(*bad_port(), sep="\n")

#checking and returning suspicious big size data
def size_check():
    data = get_file("network_traffic.log")
    big_size = [row for row in data if int(row[5]) > 5000]
    return big_size
#print(*size_check(), sep="\n")

#checking and returning [pass]
def check_large():
    data = get_file("network_traffic.log")
    pass

#checking and returning suspicious night activity data
def night_activity():
    data = get_file("network_traffic.log")
    night_times = [row for row in data if 0 <= int(row[0].split(" ")[1].split(":")[0]) < 6]
    return night_times
#print(*night_activity(), sep="\n")

#part 3 - list of hours
data = get_file("network_traffic.log")
hours_list = list(map(lambda row: row[0].split(" ")[1].split(":")[0] ,data))
#print(hours_list)
#print(set(hours_list))

#transfer bytes to kilo bytes
kilo_bytes = list(map(lambda row: round(int(row[5]) / 1024,1), data))
#print(kilo_bytes)

#list of the bad ports line\
bad_numbers = ['22', '23', '3389']
bad_ports_line = list(filter(lambda row: row[3] in bad_numbers, data))
#print(*bad_ports_line, sep="\n")

#list of suspicious night activity lines
night_hours = list(filter(lambda row: 0 <= int(row[0].split(" ")[1].split(":")[0]) < 6,data))
#print(*night_hours, sep="\n")

#dictionary os suspicious check
good_numbers = ("192.168", "10.")
suspect_check = {
    "EXTERNAL_IP": lambda row: not row[1].startswith(good_numbers),
    "SENSITIVE_PORT": lambda row: row[3] in bad_numbers,
    "LARGE_PACKET": lambda row: int(row[5]) > 5000,
    "NIGHT_ACTIVITY": lambda row: 0 <= int(row[0].split(" ")[1].split(":")[0]) < 6,
}

#a function that gets the dictionary and a line and return the suspect
def suspect_dict(dictionary, line):
    sus_list = list(filter(lambda key: dictionary[key](line), dictionary))
    return sus_list
print(suspect_dict(suspect_check, ['2024-01-16 03:03:09', '45.33.32.156', '10.0.0.4', '22', 'SSH', '6151']))