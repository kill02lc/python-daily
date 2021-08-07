# socket服务端
import socket
import struct
import json
def concect_put_file(host,port):
    sk = socket.socket()  # 创建socket对象
    sk.bind((host, port))  # 绑定IP和端口号
    sk.listen()  # 开启监听
    print("start listen")
    conn, address = sk.accept()  # 等待客户端连接 阻塞
    print("client conncet ok")
    header_len = conn.recv(4)
    header_bytes = conn.recv(struct.unpack('i', header_len)[0])  # 接收报头
    header = json.loads(header_bytes.decode("utf-8"))
    file_size = struct.unpack("i", conn.recv(4))[0]
    f = open(header['filename'], "wb") #写入文件
    while file_size > 0:
        msg = conn.recv(1024)
        f.write(msg)
        file_size -= len(msg)
    print("upload ok")
    conn.close()
    sk.close()
#获取内网ip
def get_local_ip():
    local_ip = ""
    try:
        socket_objs = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
        ip_from_ip_port = [(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in socket_objs][0][1]
        ip_from_host_name = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if
                             not ip.startswith("127.")][:1]
        local_ip = [l for l in (ip_from_ip_port, ip_from_host_name) if l][0]
    except (Exception) as e:
        print("get_local_ip found exception : %s" % e)
    return local_ip if ("" != local_ip and None != local_ip) else socket.gethostbyname(socket.gethostname())
if __name__ == '__main__':
    concect_put_file(get_local_ip(),8889)