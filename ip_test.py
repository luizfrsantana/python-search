class is_ip_address:

    def is_ip_address(self):
        octets = self.split('.')
        
        if len(octets) != 4:
            return "Errado"
        elif any(not octet.isdigit() for octet in octets):
            return "Errado"
        elif any(int(octet) < 0 for octet in octets):
            return "Errado"
        elif any(int(octet) > 255 for octet in octets):
            return "Errado"
        return "Certo"
    
    def is_ip_correct_network(self):
        octets = self.split('.')

        if octets[0] == "10":
            return "Certa"
        else:
            return "Errada"