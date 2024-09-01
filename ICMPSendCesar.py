# from ICMP.py import send_custom_icmp and all it's dependencies
from cesar import cifrado_cesar
from ICMP import send_custom_icmp
from scapy.layers.inet import IP, ICMP
from scapy.packet import Raw

if __name__ == "__main__":
    texto_a_cifrar = input("Ingresa el texto a cifrar: ")
    corrimiento = int(input("Ingresa el corrimiento: "))
    advice= cifrado_cesar('incoming message', corrimiento)
    texto_cifrado = cifrado_cesar(texto_a_cifrar, corrimiento)
    packet = IP(dst='127.0.0.1')/ICMP(type=8)/Raw(load=advice)
    send_custom_icmp(texto_cifrado, packet)
    
