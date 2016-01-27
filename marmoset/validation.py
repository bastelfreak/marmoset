import ipaddress
import re


def is_mac(mac):
    return True if re.match("^([0-9a-f]{2}:){5}[0-9a-f]{2}$", mac) else False


def is_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
    except:
        return False
    return True


def is_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
    except:
        return False
    return True


def is_cidr(cidr):
    try:
        ipaddress.IPv4Interface(cidr)
    except:
        return False
    return True


def get_cidr(cidr):
    interface = ipaddress.IPv4Interface(cidr)
    gateway = list(interface.network.hosts())[0]
    return {'ip': interface.ip,
            'nm': interface.netmask,
            'gw': gateway}


def get_ip_from_cidr(cidr):
    data = get_cidr(cidr)
    return data['ip']


def get_nm_from_cidr(cidr):
    data = get_cidr(cidr)
    return data['nm']


def get_gw_from_cidr(cidr):
    data = get_cidr(cidr)
    return data['gw']
