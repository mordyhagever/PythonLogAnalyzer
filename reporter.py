from analyzer import *

#returning a dictionary of all the IP's with a list of what are they suspected for
def suspect_list():
    sus_dict = {}
    for row in external_ip():
        ip = row[1]
        if ip not in sus_dict:
            sus_dict[ip] = []
        if "EXTERNAL_IP" not in sus_dict[ip]:
            sus_dict[ip].append("EXTERNAL_IP")
    for row in bad_port():
        ip = row[1]
        if ip not in sus_dict:
            sus_dict[ip] = []
        if "SENSITIVE_PORT" not in sus_dict[ip]:
            sus_dict[ip].append("SENSITIVE_PORT")
    for row in size_check():
        ip = row[1]
        if ip not in sus_dict:
            sus_dict[ip] = []
        if "LARGE_PACKET" not in sus_dict[ip]:
            sus_dict[ip].append("LARGE_PACKET")
    for row in night_activity():
        ip = row[1]
        if ip not in sus_dict:
            sus_dict[ip] = []
        if "NIGHT_ACTIVITY" not in sus_dict[ip]:
            sus_dict[ip].append("NIGHT_ACTIVITY")
    return sus_dict
#print(suspect_list())

