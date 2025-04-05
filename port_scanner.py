import socket

target = "scanme.nmap.org"  # Legit test target
ports = [21, 22, 80, 443]  # FTP, SSH, HTTP, HTTPS

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"🔥 Port {port} is OPEN")
    sock.close()