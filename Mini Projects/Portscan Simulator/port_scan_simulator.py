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

    hosts = []
    user_input = input('Enter the hostname or IP address > ')

    user_input = user_input.split(',')
    for host in user_input:

        hosts.append(host.strip())

    user_input= input('Enter a portnumber > ')
    port = int(user_input)

    
    print('*'*20,'PORTSCAN RESULTS','*'*20)
    results = []
    for host in hosts:

        results.append(check_port(host,port))

    for result in results:

        print(result)
        print()

    




