import base64,zlib,os,time,shutil
os.system("cls")

saves = ['CCGameManager.dat','CCLocalLevels.dat']

decrypted_save=""

for filename in os.listdir("levels"):
    file_path = os.path.join("levels", filename)
    if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)

def getLevelName(level,k):
    r = level.split(f"</s><k>k{k}</k>")[0]
    if (len(r)>20):
        return ""
    return r

def Xor(path,key):
    fr = open(path,'rb')
    data = fr.read()
    fr.close()
    
    res = []
    for i in data:
        res.append(i^key)
    return bytearray(res).decode()
 
def Decrypt(data):
    return zlib.decompress(base64.b64decode(data.replace('-','+').replace('_','/').encode())[10:],-zlib.MAX_WBITS)
def Encrypt(data):
    return zlib.compress(base64.b64encode(data.replace('+','-').replace('/','_').encode())[10:],-zlib.MAX_WBITS)

def FullDecrypt():
    os.system("cls")
    print("Decrypting...")
    fPath = os.getenv('localappdata')+'\\GeometryDash\\'
    res = Xor(fPath+saves[1],11)
    fin = Decrypt(res)

    fw = open(saves[1]+'.txt','wb')
    fw.write(fin)
    fw.close()

    print("Finished Decrpt.")
    s = open("CCLocalLevels.dat.txt","r")
    decrypted_save = s.read()
    time.sleep(2)
    os.system("cls")

    levels=[]

    id=1
    levelCount=0
    finished=False

    print("Finding levels...")
    time.sleep(2)
    os.system("cls")
    while not finished:
        clevel=""
        try: clevel = getLevelName(decrypted_save.split("<k>k2</k><s>")[id],4)
        except IndexError: 
            finished=True 
            continue
        
        if (clevel!=""):
            print(f"Found \"{clevel}\"...")
            id+=1
            levelCount+=1
            levels.append(clevel)
        else:
            id+=1
    os.system("cls")
    print(f"Levels: {levelCount}")
    print("""
    What would you like to do with these levels?
    [1] Decrypt specific level
    [2] Decrypt all levels
          
          """)
    a=input(">")
    if (a.lower()=="1"):
        l = input("level number (order in list) >")
        o = int(l)
        print(f"Decrypting \"{levels[o]}\"")
        encryptedld="H4sIAAAAAAAA"+decrypted_save.split("<s>H4sIAAAAAAAA")[1+o].split("</s>")[0]
        decryptedld=Decrypt(encryptedld)
        f = open(f"levels/{levels[o]}","wb")
        f.write(decryptedld)
        print(f"Decrypted \"{levels[o]}\"")
        exit()
    else:
        pass
    
    
    for i in levels:
        lname = levels[levels.index(i)]
        print(f"Decrypting \"{lname}\"...")
        encryptedld="H4sIAAAAAAAA"+decrypted_save.split("<s>H4sIAAAAAAAA")[1+levels.index(i)].split("</s>")[0]
        decryptedld=Decrypt(encryptedld)
        f = open(f"levels/{lname}","wb")
        f.write(decryptedld)

def EncryptIntoSave():
    os.system("cls")
    e = open("encrypt.txt","r")
    if e.read()=="":
        print("Please place level data into encrypt.txt")
        exit()
    encrypted = Encrypt(e.read())
    e.close()
    print(encrypted)

print("""
 ██████╗ ███████╗ █████╗ ███╗   ███╗███████╗████████╗██████╗ ██╗   ██╗  ██████╗  █████╗  ██████╗██╗  ██╗
██╔════╝ ██╔════╝██╔══██╗████╗ ████║██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝  ██╔══██╗██╔══██╗██╔════╝██║  ██║
██║  ██╗ █████╗  ██║  ██║██╔████╔██║█████╗     ██║   ██████╔╝ ╚████╔╝   ██║  ██║███████║╚█████╗ ███████║
██║  ╚██╗██╔══╝  ██║  ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██╗  ╚██╔╝    ██║  ██║██╔══██║ ╚═══██╗██╔══██║
╚██████╔╝███████╗╚█████╔╝██║ ╚═╝ ██║███████╗   ██║   ██║  ██║   ██║     ██████╔╝██║  ██║██████╔╝██║  ██║
 ╚═════╝ ╚══════╝ ╚════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝

 ██████╗ █████╗ ██╗   ██╗███████╗  ███╗   ███╗ █████╗ ███╗  ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██║   ██║██╔════╝  ████╗ ████║██╔══██╗████╗ ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
╚█████╗ ███████║╚██╗ ██╔╝█████╗    ██╔████╔██║███████║██╔██╗██║███████║██║  ██╗ █████╗  ██████╔╝
 ╚═══██╗██╔══██║ ╚████╔╝ ██╔══╝    ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║  ╚██╗██╔══╝  ██╔══██╗
██████╔╝██║  ██║  ╚██╔╝  ███████╗  ██║ ╚═╝ ██║██║  ██║██║ ╚███║██║  ██║╚██████╔╝███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ v1.0.0

[1] Decrypt levels into 'levels' directory
[2] Encrypt level data into CCLocalLevels.dat

      """)
a = input(">")
if (a.lower()=="1"):
    FullDecrypt()
elif (a.lower()=="2"):
    EncryptIntoSave()