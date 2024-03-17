def get_sum(data):
    return sum(data) & 0xFF


def length_to_char(dat, length):
    ret = bytearray()
    if length < 128:
        ret.append(length)
    elif length < 16384:
        ret.append((length % 128) | 0x80)
        ret.append(length >> 7)
    else:
        ret.append((length % 128) | 0x80)
        ret.append((length >> 7) | 0x80)
        ret.append(length >> 14)
    dat.extend(ret)
    return ret


def get_stg_data(data):
    buf = bytearray()
    buf.append(0x68)
    buf.extend(b'\x00\x00')  # Placeholder for length
    buf.extend(b'\xFF\x22')  # Module address and function code
    for time_period in data:
        tmp = bytearray()
        length_to_char(tmp, time_period // 8)
        buf.extend(tmp)
    checksum = get_sum(buf[3:])
    buf.append(checksum)
    buf.extend(b'\x16')
    buf[1:3] = len(buf).to_bytes(2, 'little')  # Update length bytes
    return bytes(buf)


def print_hex(data):
    print(' '.join(format(byte, '02X') for byte in data))
    # to binary
    print(''.join(format(byte, '08b') for byte in data))
    # print(''.join(format(byte, '02X') for byte in data))


def main(ir_data_hex):
    # 将十六进制字符串转换为字节数据
    # ir_data_hex = "683b010022ea08b20451454f474fd2014e484fd2014e484f474f474f474fd2014e484fd2014e484f474f474f484f474f484f474f4752444fd2014e484f474f474f474f474f474fd2014e484fd2014e484f474fd2014e484fce134e4852454f4752444f4852445244524452444f4752455145524452444f4752444f47524452445245524452445245524452445244524452cf014e485245524452cf014e9f27e508b6044e484f484fd2014e484fd2014e484e484e484e484ed3014e484ed3014e484e484e484e484e484e484e484e494e484ed3014e484e484e484e484e484e494ed3014ed3014ed3014e484e484ed3014e494ed0134d484e494e484e484e494e494e494ed5014b484e494e494e494e494e494e494d4c4b4c4b4c4b4c4a4c4bd6014a4c4a4c4a4d4a4d4a4d4a50475046da0146504650465046d916"
    ir_data = bytes.fromhex(ir_data_hex)

    # 将红外编码数据转换为外码
    external_code = get_stg_data(ir_data)

    # 输出结果
    print_hex(external_code)


if __name__ == "__main__":
    main("683b010022ea08b20451454f474fd2014e484fd2014e484f474f474f474fd2014e484fd2014e484f474f474f484f474f484f474f4752444fd2014e484f474f474f474f474f474fd2014e484fd2014e484f474fd2014e484fce134e4852454f4752444f4852445244524452444f4752455145524452444f4752444f47524452445245524452445245524452445244524452cf014e485245524452cf014e9f27e508b6044e484f484fd2014e484fd2014e484e484e484e484ed3014e484ed3014e484e484e484e484e484e484e484e494e484ed3014e484e484e484e484e484e494ed3014ed3014ed3014e484e484ed3014e494ed0134d484e494e484e484e494e494e494ed5014b484e494e494e494e494e494e494d4c4b4c4b4c4b4c4a4c4bd6014a4c4a4c4a4d4a4d4a4d4a50475046da0146504650465046d916")
    main("682f010022e908b40451494e494ed3014dd3014ed3014d494e494b4c4e494ed3014d494ed3014d494e494e494e494e484e494e494e494e494ed3014d494e494e484e494e494e494ed3014e494ed3014e484d494ed3014e484ecc1351484e494e494d494e484e494e494e494e494e484e494e494e484e494e494e494e494e484e484e484e4851455145524451454e484e484ed2014e494e484e484e484e9b27e308b9044a4c4a4c4bd6014ad6014ad6014a4c4a4c4a4c4a4c4ad6014a4c4ad6014a4c4a4d4a4d4a4d4a4d4a5047504650475046d70149504750465047504650465046d7014ad70149d7014a50465047d701495047d3134950474f475046504750474f475046d70149504650475046504650465046504650465343534353435343de014357405a395d3964337d195816")
