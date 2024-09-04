from scapy.all import *
from scapy.layers.inet import IP, ICMP, ICMPTimeStampField 
from scapy.packet import Raw
from datetime import datetime
import time

def capture_ping():
    # Capturar un ping ICMP de ejemplo
    def filter_icmp(packet):
        return ICMP in packet and packet[ICMP].type == 8  # ICMP Echo Request
    
    print("Realizando ping para capturar un paquete ICMP real...")
    ans = sr1(IP(dst="8.8.8.8")/ICMP(), timeout=1, verbose=0)
    
    if ans:
        print("Paquete ICMP capturado:")
        ans.show()
        return ans
    else:
        print("No se capturó ningún paquete ICMP.")
        return None

def send_custom_icmp(string_to_send, original_icmp):
    # Enviar un carácter por paquete ICMP basado en un paquete ICMP original
    dst_ip = original_icmp[IP].dst
    id = original_icmp[ICMP].id
    seq = original_icmp[ICMP].seq
    print("\nEnviando datos en paquetes ICMP...")
    for char in string_to_send:
        timestamp = int(time.time()) # Obtener la marca de tiempo actual
        timestamp = struct.pack('<Q', timestamp) # Empaquetar la marca de tiempo en un formato de 8 bytes
        packet = IP(dst=dst_ip)/ICMP(id=id, seq=seq)/timestamp/Raw(load=char)
        packet.show()
        send(packet, verbose=0)
        print(f"Enviado: {char}")
        time.sleep(0.5)  # Pausa para evitar picos de tráfico sospechosos
        seq += 1  # Incrementar el número de secuencia para cada paquete
        
def capture_modified_ping():
    # Capturar el ping ICMP modificado enviado
    print("\nCapturando paquetes ICMP modificados enviados...")
    packets = sniff(filter="icmp", count=len(string_to_send), timeout=5)
    
    for packet in packets:
        if ICMP in packet and packet[ICMP].type == 8:
            print("\nPaquete ICMP modificado capturado:")
            packet.show()

if __name__ == "__main__":
    string_to_send = "HELLO"
    dst_ip = "127.0.0.1"  # IP de destino, en este caso Localhost
    packet = IP(dst=dst_ip)/ICMP(type=8)/Raw(load="OriginalPing")
    send_custom_icmp(string_to_send=string_to_send, original_icmp=packet)

