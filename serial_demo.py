import serial
import serial.tools.list_ports
import threading
import time

all_ports = []
for ports in serial.tools.list_ports.comports():
    print(ports.device)
    all_ports.append(ports.device)

serial_port = serial.Serial('/dev/cu.usbmodemLU_2022_88881', 115200, timeout=0.1)

# while True:
#     data = serial_port.readline()
#     if data:
#         print(data.hex())

print("end of the program")


#
# with serial.Serial('/dev/cu.usbmodemLU_2022_88881', 9600, timeout=0.1) as ser:
#     x = ser.read()          # read one byte
#     s = ser.read(10)        # read up to ten bytes (timeout)
#     line = ser.readline()   # read a '\n' terminated line
def read_serial():
    while True:
        data = serial_port.readline()
        if data:
            # print hex
            print("Received: " + data.hex())
            # # split every 8 characters and print to hex
            # data = [data[i:i+20] for i in range(0, len(data), 20)]
            # for d in data:
            #     print("every : "+d.hex() +"\n")



thread = threading.Thread(target=read_serial)
thread.start()

while True:
    # time.sleep(10)
    # read keyboard input
    res = input("Press Enter to continue...\n")
    # write hex to serial port
    serial_port.write(bytes.fromhex(res))
    # get hex from input
    print("You entered: " + hex(int(res, 16)))


# with serial.Serial('/dev/cu.usbmodemLU_2022_88881', 9600, timeout=0.1) as ser:

# 00 -> 06 共7个字节
# 68 固定开始
# 08 00 ， 07 00长度
# FF 模块地址
# 10 11 12 13 14 15 16 功能码
# 00 01 02 03 04 05 06 数据域
# 0F 10 11 17 校验码
# 16 固定结束
# 内部学习dd1       68 08 00 FF 10    00   0F 16   680800FF10000F16  680800FF10011016
# 退出内部学习      68 07 00 FF 11       10 16  680700FF111016
# 发送内部存储编码   68 08 00 FF 12    00   11 16      680800FF12001116  680800FF12011216
# 读取内部编码      68 08 00 FF 18    00   17 16     680800FF18001716  680800FF18011816
# 读取编码不存储     68 07 00 FF 20      1F 16         680700FF201F16
# 退出读取编码      68 07 00 FF 21 20 16              680700FF212016
# 683c0100180000ec08b1045343544254cc0153425442544254425442544253cd01544254cd0153435442544254425442534253425342534353cd0153435343534352435343504650d00150464fd1014f464f464fd0014f474fd0134f474f474e474e484ed2014e474e484e474e484e474e474e474e474ed2014e474e474e474e474e474e474f47524452444e474e474e484e484e484ed2014ed2014e484ed2014ea027e708b7044d484d484dd3014d484d484d484d494d494d494dd6014a4c4ad5014a4b4a4b4a4b4a4b4a4b4a4b4a4b4a4b4a4b4ad6014a4c4a4c4a4b4a4c4a4c4a4c4ad6014ad6014ad6014a4c4a4c4ad6014a4c4ad6134a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c494c494c494c494e484f465046504650465046504650465046da0146f216

# 683c0100180100ed08b104563f534354cd0153cd015342544254425342544253cd01534354cd0153425343544253435342534253435442544254cc0153425442544254425442544253cc01524354cc015243534254cc01544254cc13534254425343534353cd015343534354425442544253425343534352ce0152435343534353435343404653434f4650464f464f464f464f474f474fd1014fd1014f474f474fa127e808b7044e484e474ed2014ed2014e484e484e484e474e474ed2014e474ed2014e474e474e474e474e474e484e474e474e474ed2014e474e474e484e474e474e474ed2014ed2014ed2014e484e484ed2014e484ed2134e484e474e474e474e474e484e474e47514452444e474e47524451444e474e474e474e484e484e484e484e484e484e484e484e484e484d484d484d484d494d494de216


# 683a010022ff10b0045442544254cc0152435442544254425442544254cc01544254cc0153435442534254425442544254425442534254cc0153425442544254425442544254cc01544254cc015342544254cc01534353cc13504650465046534250d001504650464f474f464f474f474f474f474ed2014e474e474e484e484e484e484e474e474e484e484e484e484e474e474ed2014ed2014e484ed2014ea127ec08b404514551454ed2014e474e4851454e484e484e484ed2014e484ed2014e484e484e484e484e484e484e484e484e484ed2014e484e484e484d484d484d484dd3014dd3014dd3014d484d484dd3014d494dd2134d494d494d494d4c4a4b4a4b4a4b4a4c4a4c4a4b4a4b4a4c4a4c4a4b4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c494c494c494d4940465046da01461716
# 683a010022ef12b0045442544254cc0153435442544254425442544254cc01534354cc0153425442534254425442544254425442544254cc0153435442544254425442544253cd01534353cd015343544253cd01504653cb13534354425342544254cc015046534250455442514554425342534254cc01534354425343504653425046534250465342504650465046504650464fd1014fd1014f464fd1014f9f27e808b6044f474f474fd1014f474f474e474e474e474e474ed2014e484ed2014e474e474e484e474e474e484e484e484e484ed2014e474e474e484e474e474e474ed2014ed2014ed2014e484e484ed2014e474ed1134e484e474e474e474e484e484e474e474e474e474e484e474e474e474e474e474e474e474f474e474f475244524451445244514451444e484e484e484e484ed2014d0616
# 683a010022d524b0045441544154cb0153cd015243544254415441544254cc01544254cc0154425441544254415442544154415442544254cc0153425442544254425442544254cc01544254cc015442544254cc01534254ca13544254425442534254cc015342544253425343534353435342504653cd015343504650464f464f464f464f464f464f464f474f474f474f474e474ed1014ed2014e484e474e9f27e808b7044e484e474ed2014ed2014e484e474e474e474e474ed2014e484ed2014e484e474e474e484e474e484e474e474e474ed2014e484e474f474e474e474e474fd1014ed2014ed2014e4751444ed1014e484ed0134e47514451444e484e474e4751454e484e484e484e484e484e484e484e484e484e484e484e484e484d484e484d484d484d484d494d4b4a4b4a4b4a4c4a4c4a4c4af116
# 683a010022a510b1045442544254cc0153425442573f53425441544254cc01534254cc0153435442544154425442544154425441544254cc0153425442544253425442544254cc01534254cc015343544254cc01534353cb13544254425442534253cd015243534253425343544250465343504653cd015343534340464f4650464f464f474f464f474f474e474e474e474e474ed2014ed2014e484ed2014ea027e808b7044e484e474ed2014e484e474e474e474e474e484ed2014e484ed2014e484e484e474e474e474e474e474e474f474ed1014e475244524452444e474e4751cf014ed2014ed2014e4751444ed2014e484ed1134e4851444e484e484e484e484e484e484e484e484e484e484e484e484e484e484e484e484e484d484d484d484d484d494d4b4a4c4a4b4a4c4a4b4a4c4a4c4ad6014aa916
# 683a010022ac28b0045441544154cc0154cc01544154415442573f544254cc01534254cc0153425442544254425442544154425442544254cc0154425442544254425442544254cc01534254cc015442534253cc01534354cc13534354425342544253cd015343534253425343534353435046534350d001504640464f464f464f464f464f474f474f474d494e484e484e474e474ed2014ed2014e474e484ea127e808b7044e484e474ed2014ed2014e484e474e474e474e474ed1014e484ed2014e484e474f474e474f474f474e474f474e474fd1014f475144514451444e4751444ed2014ed2014ed2014e484e4851cf014e484ed1134e484e484e484e484e484e484e484e484e484e484e484e484e484e484d484d484d484e484d484d484d494d494d4b4a4b4a4c4a4b4a4c4a4c4a4c4a4c4a4c4a4c4acd16
# 683a0100228013b1045342544253cd0153425342544253425343534253cd01524453cd01534250465046534350464f464f4650464f464fd1014f474f474f474f474f474e474ed1014e484ed2014e484e474ed2014e474ed1134e484e484e474e474ed2014e474f474e47524452444e474f474e484ed2014e484e484e484e484e484e484e484d484d484d484d494d494d4b4a4b4ad6014ad6014a4b4ad6014aa527e408bb044a4c4a4c4ad6014a4c4a4c4a4c4a4c4a4c4a4c4ad6014a4c4ad6014a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4a4c4ad601494c494c494c494c494c494c49d60149d70149d701494c494d49d701494d49d81346504650465046504650464f464f464f465046504650465046504650464f465046504650465046504650464f46504650465046504650465046504650465046da0146a016

# 6863000022e608b7044249424a42494249424a4249424a424942d60142d70142d70141d70142d70142d60142d70142d70142d701424a42d601424a42d6014249424a424a424942d601424a42d601424942d60142d70142d70142ba27e8089d02420f16
# 6863000022e608b704424a424a4249424a424a424a424a424a42d60142d60142d60142d60142d60142d60142d60142d60142d601424a42d601424a42d601424a424a424a424a42d601424a42d601424a42d60142d60142d60142b827ea089902420a16
# 6863000022e608b704424a4249424a424a424a42494249424942d60142d60142d60142d70142d60142d60142d60142d60142d701424a42d601424a42d6014249424a424a424942d601424a42d601424a42d60142d60142d60142b927e8089c02420916


# 关机 26度， 静音， 制热 0010
# 683b010022ea08b20451454f474fd2014e484fd2014e484f474f474f474fd2014e484fd2014e484f474f474f484f474f484f474f4752444fd2014e484f474f474f474f474f474fd2014e484fd2014e484f474fd2014e484fce134e4852454f4752444f4852445244524452444f4752455145524452444f4752444f47524452445245524452445245524452445244524452cf014e485245524452cf014e9f27e508b6044e484f484fd2014e484fd2014e484e484e484e484ed3014e484ed3014e484e484e484e484e484e484e484e494e484ed3014e484e484e484e484e484e494ed3014ed3014ed3014e484e484ed3014e494ed0134d484e494e484e484e494e494e494ed5014b484e494e494e494e494e494e494d4c4b4c4b4c4b4c4a4c4bd6014a4c4a4c4a4d4a4d4a4d4a50475046da0146504650465046d916

# 开机 26度， 静音， 制热 0011
# 682f010022e908b40451494e494ed3014dd3014ed3014d494e494b4c4e494ed3014d494ed3014d494e494e494e494e484e494e494e494e494ed3014d494e494e484e494e494e494ed3014e494ed3014e484d494ed3014e484ecc1351484e494e494d494e484e494e494e494e494e484e494e494e484e494e494e494e494e484e484e484e4851455145524451454e484e484ed2014e494e484e484e484e9b27e308b9044a4c4a4c4bd6014ad6014ad6014a4c4a4c4a4c4a4c4ad6014a4c4ad6014a4c4a4d4a4d4a4d4a4d4a5047504650475046d70149504750465047504650465046d7014ad70149d7014a50465047d701495047d3134950474f475046504750474f475046d70149504650475046504650465046504650465343534353435343de014357405a395d3964337d195816
# 011010000100001000000001111111110010001000