CRITICAL_PORTS = {
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    67: 'DCHP-Server',
    68: 'DHCP-Client',
    80: 'HTTP',
    443: 'HTTPS',
    110: 'POP3',
    143: 'IMAP',
    3306: 'MySQL',
    3389: 'RDP',
    5900: 'VNC',
    5432:'PostgreSQL',
    6379: 'Redis',
    27017: 'MongoDB',
    514: 'Syslog',
    993: 'IMAPS',
    995: 'POPS'
    }

# Prepare different for categorising port numbers later
user_selected_ports = []
critical_ports = []
non_critical_ports = []

user_input = input('Type one or more port numbers separated by comma "," > ')

user_input = user_input.split(',')

for value in user_input:

    try:

        port = int(value)

        user_selected_ports.append(port)

    except ValueError:

        continue

# Check if user_input is a critical port

for port in user_selected_ports:

    if port in CRITICAL_PORTS:

        critical_ports.append((port,CRITICAL_PORTS[port]))
    
    else:
        non_critical_ports.append(port)


for port in critical_ports:

    message = f'Critical port: {port}'

    print(message)

print()

for port in non_critical_ports:

    message = f'Non-critical port: {port}'

    print(message)
