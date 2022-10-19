import requests
import threading
from colorama import Fore,init
init()
# colores C
rojo = Fore.RED
magenta = Fore.LIGHTMAGENTA_EX
verde = Fore.LIGHTGREEN_EX
blanco = Fore.LIGHTWHITE_EX
azul = Fore.LIGHTBLUE_EX
amarillo = Fore.LIGHTYELLOW_EX

lista_cedulas = input(f"{amarillo}INGRESA LA LISTA DE CEDULAS {magenta}=> {blanco}")
with open(lista_cedulas) as f_obj:
    lineas_cedulas = f_obj.readlines()

def consulta_cnt():
    for line in lineas_cedulas:
        cedulaCnt = line.strip()
        url = "https://www.cnt.com.ec/api/accounts"
        headers = {
         "User-Agent": 'Mozilla/5.0 (X11; Arch Linux; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
         "Content-Type": 'application/json',
        }
        payload = '{"id":"%s"}' % (cedulaCnt)
        respuesta = requests.post(url, headers=headers, data=payload)
        if respuesta.status_code == 200:
           if '{"respuesta":"1"}' in respuesta.text:
              print(f"{blanco}[{azul}S{blanco}] {verde}LA CEDULA {cedulaCnt} NO TIENE DEUDAS")
           elif '{"respuesta":"2"}' in respuesta.text:
              print(f"{blanco}[{rojo}D{blanco}] {rojo}LA CEDULA {cedulaCnt} TIENE DEUDAS EN CNT")
           elif '{"respuesta":"3"}' in respuesta.text:
              print(f"{blanco}[{magenta}N{blanco}] {blanco}LA CEDULA {cedulaCnt} NO ESTA REGISTRADA EN CNT")
           else:
              pass
        else:
           print(f"{rojo}ERROR RESPUESTA DE SERVIDOR {magenta}=> {verde}{respuesta.status_code}")


if __name__ == "__main__":
     hilos_cnt = list()
     for i in range(3):
         hilos = threading.Thread(target=consulta_cnt)
         hilos_cnt.append(hilos)
         hilos.start()

"""
[S] = SE ENCUENTRA EN CNT Y NO TIENE DEUDAS
[D] = SE ENCUENTRA EN CNT PERO TIENE DEUDAS
[N] = NO SE ENCUENTRA EN CNT/NO TIENE SERVICIOS

"""
