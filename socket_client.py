# socket客户端
import socket
import struct
import os
import json
def concect_upload_file(host,port,filename):
    client = socket.socket()
    ip_port = (host, int(port))
    client.connect(ip_port)
    buffer = 1024
    header = {  # 报头为dict类型
        "filename": filename,
        "filesize": 0,
    }
    file_path = os.path.join( header['filename'])
    file_size = os.path.getsize(file_path)
    header['filesize'] = file_size
    header_json = json.dumps(header)  # 报头序列化为json字符串
    header_bytes = header_json.encode("utf-8")  # 报头编码为bytes类型
    client.send(struct.pack('i', len(header_bytes)))  # 发送4个字节的报头大小
    client.send(header_bytes)  # 发送报头
    client.send(struct.pack("i", file_size))
    with open(filename, "rb") as f:
        print("uploading...")
        for line in f:
            client.send(line)

    print(f"{filename} upload ok")
    # with open(file_path, "rb") as f:
    #     while file_size:
    #         if file_size >= buffer:
    #             client.send(f.read(buffer))
    #             file_size -= buffer
    #             print(file_size, buffer, "第一次或中间的")
    #         else:
    #             client.send(f.read(buffer))
    #
    #             print(file_size, buffer, "最后一次")
    #             break
    client.close()
if __name__ == '__main__':
    host=input("please input ip:")
    port=input("please input port:")
    filename = input("please intput filename:")
    concect_upload_file(host,port,filename)