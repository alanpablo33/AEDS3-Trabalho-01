# subprocess.call() é preferível a os.system()
# funciona em Python 2.7 e 3.4
# funciona em Linux, Mac OS, Windows
#pip install pyping


def ping(host):
   #Retorna True se o host responder a uma solicitação de ping
    import subprocess, platform

    # Parâmetros de ping como função do sistema operacional
    ping_str = "-n 5" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0

# test call
print(ping("8.8.8.8"))

