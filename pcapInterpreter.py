from scapy.all import rdpcap, ICMP
from termcolor import colored
from spellchecker import SpellChecker
import string

def cesar_decrypt(text, shift):
    decrypted = []
    for char in text:
        if char in string.ascii_letters:
            start = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

def extract_message_from_pcap(pcap_file):
    es = SpellChecker() 
    en = SpellChecker(language='es') 
    packets = rdpcap(pcap_file)
    messages = []

    # Extraer todos los posibles mensajes
    for packet in packets:
        if ICMP in packet and packet[ICMP].type == 8:  # Echo Request
            data = packet[ICMP].load.decode('latin1', errors='ignore')  # Decodificar la carga útil
            messages.append(data)

    combined_message = ''.join(messages)

    # Probar todos los desplazamientos posibles
    for shift in range(26):
        possible_message = cesar_decrypt(combined_message, shift)
        # count words in possible_message
        words = possible_message.split()
        english = 0
        spanish = 0
        for word in words:
            if es.known([word]):
                english += 1
            if en.known([word]):
                spanish += 1
        if english + spanish == len(words): 
            print(colored(f"Mensaje posible con desplazamiento {shift}:", 'green'))
            print(colored(possible_message, 'green'))
        else:
            print(colored(f"Mensaje con desplazamiento {shift}:", 'black'))
            print(colored(possible_message, 'black'))    

if __name__ == "__main__":
    pcap_file = "captura.pcap"  # Reemplaza con el nombre de tu archivo .pcap
    extract_message_from_pcap(pcap_file)
