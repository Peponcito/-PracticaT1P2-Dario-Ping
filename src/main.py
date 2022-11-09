import platform
import subprocess

def ping(host):
    parametro = '-n' if platform.system().lower() == 'windows' else'-c'
    comando = ['ping', parametro, '3', host]

    subprocess.call(comando)

ping('8.8.8.8')