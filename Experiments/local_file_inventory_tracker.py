files = {
    '01 filename': {
        'size': 20,
        'last_modified_date': '2026-04-07'
        },
    '02 filename': 
        {'size': 20,
        'last_modified_date': '2026-04-07'
        }
         }

for filename,info in files.items():

    print(filename,'\t')

    for descriptor,metadata in info.items() :

        print(f'\t{descriptor}: {metadata}')

        
