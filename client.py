import socket

# Inisialisasi socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hubungkan ke server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Kirim data ke server
    message = "Halo, ini klien!"
    client_socket.sendall(message.encode())
    
    # Terima balasan dari server
    data = client_socket.recv(1024)
    print("Menerima dari server:", data.decode())
    
finally:
    # Tutup koneksi
    client_socket.close()
