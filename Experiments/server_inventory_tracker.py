servers = {
    'SV1': {
    'IP': '192.168.0.1',
    'status': 'Up',
    'OS': 'Ubuntu 22.04',
    'CPU': '4 Cores',
    'RAM' : '16GB',
    'Location': 'Data Center 1',
    'Environment': 'Production',
    'Last_Checked': '2026-04-07 09:30',
    'Uptime' : '72 Hours',
    'Services': ['nginx','docker', 'ssh'],
    'Tags': ['web','database'],
    'Notes': 'Critical: Handles billing API and payment processing. '
    'Do not restart during business hours.'    },
    'SV2': {
    'IP': '192.168.0.2',
    'status': 'Up',
    'OS': 'Ubuntu 22.04',
    'CPU': '4 Cores',
    'RAM' : '16GB',
    'Location': 'Data Center 1',
    'Environment': 'Production',
    'Last_Checked': '2026-04-07 09:30',
    'Uptime' : '72 Hours',
    'Services': ['nginx','docker', 'ssh'],
    'Tags': ['web','database'],
    'Notes': 'Hosts internal intranet frontend. Restart allowed after 18:00.'},
    'SV3': {
    'IP': '192.168.0.3',
    'status': 'Up',
    'OS': 'Ubuntu 22.04',
    'CPU': '4 Cores',
    'RAM' : '16GB',
    'Location': 'Data Center 1',
    'Environment': 'Production',
    'Last_Checked': '2026-04-07 09:30',
    'Uptime' : '72 Hours',
    'Services': ['nginx','docker', 'ssh'],
    'Tags': ['web','database'],
    'Notes': 'Backend service for intranet (user authentication).'
    'Depends on SV5 database.'
    },
    'SV4': {
    'IP': '192.168.0.4',
    'status': 'Up',
    'OS': 'Ubuntu 22.04',
    'CPU': '4 Cores',
    'RAM' : '16GB',
    'Location': 'Data Center 1',
    'Environment': 'Production',
    'Last_Checked': '2026-04-07 09:30',
    'Uptime' : '72 Hours',
    'Services': ['nginx', 'ssh'],
    'Tags': ['web','database'],
    'Notes': 'Load balancer for web services.'
    ' Routes traffic between SV2 and SV3.'    },
    'SV5': {
    'IP': '192.168.0.5',
    'status': 'Up',
    'OS': 'Windows Server 2019',
    'CPU': '4 Cores',
    'RAM' : '16GB',
    'Location': 'Data Center 1',
    'Environment': 'Production',
    'Last_Checked': '2026-04-07 09:30',
    'Uptime' : '72 Hours',
    'Services': ['iis','ssh'],
    'Tags': ['web','database'],
    'Notes': 'Windows server running IIS. '
    'Hosts internal database and legacy apps. Backup runs nightly.'    },

}


def get_notes():

    notes = []

    for server in servers.values() :

        message = f'{server['IP']}   {server['Notes']}'

        notes.append(message)

    return notes

notes = get_notes()    
for note in notes:

    print(note)