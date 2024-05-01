import socket

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket ke alamat dan port tertentu
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Mendengarkan koneksi masuk
server_socket.listen(5)

print("Server berjalan di", server_address)

while True:
    # Menunggu koneksi masuk
    client_socket, client_address = server_socket.accept()
    
    try:
        print("Terhubung dengan", client_address)
        
        # Menerima data dari klien
        data = client_socket.recv(1024)
        print("Menerima:", data.decode())
        
        # Mengirim balasan ke klien
        client_socket.sendall(b"Terima kasih!")
        
    finally:
        # Tutup koneksi dengan klien
        client_socket.close()
