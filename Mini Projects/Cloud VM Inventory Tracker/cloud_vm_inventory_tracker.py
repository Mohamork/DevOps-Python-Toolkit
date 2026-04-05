vms = {
    'vm1': {
        'ip': '10.10.0.1',
        'status': 'running'
        },
    'vm2': {
        'ip' : '10.10.0.2',
        'status': 'stopped'
        }, 
    'vm3': {
        'ip': '10.10.0.3',
        'status': 'running'
        },
    'vm4': {
        'ip' : '10.10.0.4',
        'status': 'stopped'
        },
    'vm5': {
        'ip': '10.10.0.5',
        'status': 'running'
        }  
}


running_vms = []
stopped_vms = []

for vm,info in vms.items():

    host = vm
    ip = info['ip']
    status = info['status']

    if status == 'running':
        
        message = f'Host: {host}\tip: {ip}\tstatus: {status}\n'

        running_vms.append(message)

    elif status == 'stopped':

        message = f'Host:{host}\tip: {ip}\tstatus: {status}\n'

        stopped_vms.append(message)


for vm_status in running_vms:

    print(vm_status)

count = len(running_vms)
print('Running vm count:',count)
print()

for vm_status in stopped_vms:

    print(vm_status)

count = len(stopped_vms)

print('Stopped vm count:',count)



    