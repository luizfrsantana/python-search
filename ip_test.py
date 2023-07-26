def is_ip_address(ip):
    octets = ip.split('.')
        
    if len(octets) != 4:
            return "Errado"
    elif any(not octet.isdigit() for octet in octets):
            return "Errado"
    elif any(int(octet) < 0 for octet in octets):
            return "Errado"
    elif any(int(octet) > 255 for octet in octets):
            return "Errado"
    return "Certo"
    
def is_ip_correct_network(ip):
    octets = ip.split('.')

    if octets[0] == "10":
        return "Certa"
    else:
        return "Errada"