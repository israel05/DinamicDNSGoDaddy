# BASADO EN https://pypi.org/project/GoDaddyPy/
# Y EN LA ESTRUCTURA DE  PaulSidze/godaddyDDNS

from godaddypy import Client, Account
import json
import requests

#leo mi ip pública y la devuelvo en la función
def getMyWanIP():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)
    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()

    data = response.json()
    print("He encontrado que la pública es esta") 
    print (data['ip'])
    return data['ip']

def main():
    #del script anterior me quedo con la ip pública
    current_ip = getMyWanIP()
    my_acct = Account(api_key='TU CLAVE DE API CONSEGUIDA EN developer.godaddy.com/' , api_secret=' TU CLAVE SECRETA DEL MISMO SITIO')
    client = Client(my_acct)
    my_domains = client.get_domains()
    daddy_ip = client.get_records(' EL NOMBRE DE TU DOMINIO', record_type='A', name='@')
    if current_ip != daddy_ip:
        client.update_ip(current_ip, domains=[my_domains[0]])
        print("IP distintas, voy a actualizar")
    else:
        print("No era la ip diferente, se queda como esta")
# "Your Public IP is %s and GoDaddy A record is %s for the domain %s" % (current_ip,daddy_ip, my_domains[0])
if __name__ == '__main__':
    main()




