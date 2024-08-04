import os, sys
from fcntl import ioctl
# ioctl commands defined at the pci driver

#Precisa configurar
NUMBER0 = 0
NUMBER1 = 0
NUMBER2 = 0
NUMBER3 = 0
NUMBER4 = 0
NUMBER5 = 0
NUMBER6 = 0
NUMBER7 = 0
NUMBER8 = 0
NUMBER9 = 0

RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934

class Integration:

    def __init__(self): 
        # if len(sys.argv) < 2:
        #     print("Error: expected more command line arguments")
        #     print("Syntax: %s </dev/device_file>"%sys.argv[0])
        #     exit(1)
        
        self.fd = os.open('/dev/mydev', os.O_RDWR)

    def __del__(self):
        os.close(self.fd)

    def bytes_to_str(self, b):
        bytes_int = int.from_bytes(b, byteorder='little') # Converte bytes pra integer
        bytes_bits = bin(bytes_int)[2:] # Converte integer pra binary string e remove o prefixo '0b'
        bytes_bits_str = bytes_bits.zfill(32) # Pad the binary string with leading zeros to ensure it has 32 bits

        return bytes_bits_str

    def Read_Switches(self):
        ioctl(self.fd, RD_SWITCHES) #Lê o switch
        ret_switch = os.read(self.fd, 4) #Retorna a leitura no valor de 4 bytes
        ret_switch_int = int.from_bytes(ret_switch, 'little') #Converte os bytes para inteiro
        ret_switch_str = self.bytes_to_str(ret_switch) #Converte os bytes para string
        return [ret_switch_int, ret_switch_str] #Retorna o valor do switch e a string

    def Read_Button(self, pos):
        ioctl(self.fd, RD_PBUTTONS)
        pos_button = (0x1 << pos)
        ret_button = os.read(self.fd, 4)
        return 1 if (pos_button & int.from_bytes(ret_button, 'little')) > 0 else 0
    
    def Write_Led_Green(self, health): #Desse jeito só um led pode ser aceso por vez
        ioctl(self.fd, WR_GREEN_LEDS)
        # pos_led = (0x1 << pos)
        os.write(self.fd, health.to_bytes(4, 'little'))

    def Write_Led_Red(self, health): #Desse jeito só um led pode ser aceso por vez
        ioctl(self.fd, WR_RED_LEDS)
        # pos_led = (0x1 << pos)
        os.write(self.fd, health.to_bytes(4, 'little'))


    #We have 4 numbers, in max

    # def Write_Display_Left(self, numbers):
    #     ioctl(self.fd, WR_L_DISPLAY)

    #     data = 0
    #     for n in numbers:
    #         data = Convert_to_hex(data, n)
        
    #     os.write(self.fd, data.to_bytes(4, 'little'))

    # def Write_Display_Right(self, numbers):
    #     ioctl(self.fd, WR_R_DISPLAY)
    #     data = 0
    #     for n in numbers:
    #         data = Convert_to_hex(data, n)
        
    #     os.write(self.fd, data.to_bytes(4, 'little'))
        

# def Convert_to_hex(data, number):
#         data = data << 8 #Each display have 8 bits to reference

#         if number == '9':
#             data = data | NUMBER_9
#         elif number == '8':
#             data = data | NUMBER_8
#         elif number == '7':
#             data = data | NUMBER_7
#         elif number == '6':
#             data = data | NUMBER_6
#         elif number == '5':
#             data = data | NUMBER_5
#         elif number == '4':
#             data = data | NUMBER_4
#         elif number == '3':
#             data = data | NUMBER_3
#         elif number == '2':
#             data = data | NUMBER_2
#         elif number == '1':
#             data = data | NUMBER_1
#         elif number == '0':
#             data = data | NUMBER_0



        
    

        
    

    
