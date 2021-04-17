import os

def download(url):
    comm = "annie.exe " + url
    for i in range(1,287):
        command = comm + str(i)
        print(command)
        os.system(command)
    print("ok!")

if __name__=='__main__':
    url = "https://www.bilibili.com/video/BV1FV411r7m8?p="
    download(url)