import socket        #Soket kütüphanesi kullanılmak için import edildi.

IP = "localhost"
#Server'ın çalışacağı IP adresi belirlendi.
Port = 8080
#Server'ın dinleyeceği Port numarası belirlendi. İlk 1024 port genel olarak kullanıldığı için boşta olan port numarası seçildi.

print("Server created... Waiting for connection...")        #Server'ın çalıştığı ve bağlantı beklendiği yazdırıldı.
host = socket.gethostname()                                 #Bağlantı kuran clientın adresinin alınması sağlandı.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #soket oluşturuldu. Soket türü ve tipi belirlendi.
sock.bind((IP,Port))                                        #Oluşturulan soket IP adresi ve port numarası ile ilişkilendirldi.
sock.listen()                                               #Server'ın soketi dinlemesi sağlandı.
conn, address= sock.accept()                                #Bağlantı isteği geldiğinde bağlantının kabul edilmesi sağlandı.

print("Connection from: " + str(address))                   #Bağlantı kuran istemcinin addresi yazdırıldı.

while True:
   message = conn.recv(1024).decode('utf-8')                #İstemciden gelen mesajın decode işlemi yapıldı.
   if not message:
      break                                                 #Eğer mesaj yoksa ekrana yazılacak bir şey yoktur.
   else:
      print ("From connected user:"+ str(message))          #mesaj geldiğinde ekrana yazdırılması sağlandı.

conn.close()                                                #Bağlantı kapatıldı.