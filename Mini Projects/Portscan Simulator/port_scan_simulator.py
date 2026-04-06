import socket
from contextlib import closing
from datetime import datetime

def check_port(host,port,timeout=2):

    with closing(socket.socket(socket.AF_INET,socket.SOCK_STREAM)) as sock:

        sock.settimeout(timeout)

        if sock.connect_ex((host,port)) == 0:

            now = datetime.now()

            result = f'{now}    Port {port} on host {host} is OPEN'

            return result
        
        else:

            now = datetime.now()

            result = f'{now}    Port {port} on host {host} is CLOSED'

            return result

# Run the program

if __name__ == '__main__':  

    ip_addresses = []
    user_input = input('Please enter an IP address > ')

    user_input = user_input.split(',')
    for ip in user_input:

        ip_addresses.append(ip.strip())

    user_input= input('Please enter a portnumber > ')
    port = int(user_input)

    results = []
    for ip in ip_addresses:

        results.append(check_port(ip,port))

    for result in results:

        print(result)
        print()

    




