import socket                       #soket kütüphanesi kullanılmak üzere import edildi.

IP = "localhost"                    #Bağlanılacak olan ip adresi yazıldı.
Port = 8080                         #Server'ın dinlediği port numarasına bağlantı kurmak için tanımlandı.

my_username = input("Username : ")                              #Kullanıcı adı soruldu ve alındı.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #Soket oluşturuldu. Soket türü ve tipi belirlendi.
sock.connect((IP, Port))                                        #Belirlenen IP adresi ve Port numarası ile bağlantı kurulması sağlandı.

def client():
    while True:
        message = input("Type your message : ")                 #Server'a mesaj göndermek için mesaj girilmesi sağlandı.
        sock.send(message.encode('utf-8'))                             #Oluşturulan soket üzerinden mesajın kodlanması sağlandı.

        if message.lower().strip() == 'exit':                   #eğer mesaj exit ise çıkış yapılması sağlandı.

            break

    sock.close()                                                #Soket kapatıldı.



if __name__ == '__main__':
    client()                                                    #Oluşturulan fonksiyon çağırıldı.