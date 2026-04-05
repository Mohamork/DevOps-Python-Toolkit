import ipaddress

user_input = input('Type an ip addres > ')

try:

    ip_address =  ipaddress.ip_address(user_input)
        
    print('IP Address:',ip_address)

    if ip_address.is_link_local:

        print(' Is Link-Local:',ip_address.is_link_local)

    elif ip_address.is_private:
        
        print(' Is Private:',ip_address.is_private)

    elif ip_address.is_global:  

        print(' Is Global:',ip_address.is_global)


except Exception as e:   

    print(e)

