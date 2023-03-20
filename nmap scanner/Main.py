import nmap

scanner = nmap.PortScanner()

print("""
    
   _   _ ___ ____  ____  _____ _   _   ______        _____  ____  ____  
| | | |_ _|  _ \|  _ \| ____| \ | | / ___\ \      / / _ \|  _ \|  _ \ 
| |_| || || | | | | | |  _| |  \| | \___ \\ \ /\ / / | | | |_) | | | |
|  _  || || |_| | |_| | |___| |\  |  ___) |\ V  V /| |_| |  _ <| |_| |
|_| |_|___|____/|____/|_____|_| \_| |____/  \_/\_/  \___/|_| \_\____/
    
[*]Hello Welcome to HiDDEN SWORD Toolkit    [*]
                 Authors:[Void & Farzad13]    
[*]please dont use for illegal activity     [*]
[*]github:https://github.com/mamadsf        [*]
    
    """)

Ip_Address = input("Lotfan ip Target type konid : ")
print("IP ke vared kardi ine >>" , Ip_Address)
type(Ip_Address)

resp  = input("""\nlotfan on mode ke mikhayd bahash scan konid ro type konid
                    1)SYN ACK Scan
                    2)UDP scan
                    3)Comprehensive Scan \n




""")
print("you have selected option: ", resp)

if resp == '1':
    print("Nmap version",  scanner.nmap_version())
    scanner.scan(Ip_Address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[Ip_Address].state())
    print(scanner[Ip_Address].all_protocols())
    print("open ports", scanner[Ip_Address]['tcp'].keys()) 
elif resp == '2':
    print("Nmap version",  scanner.nmap_version())
    scanner.scan(Ip_Address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[Ip_Address].state())
    print(scanner[Ip_Address].all_protocols())
    print("open ports", scanner[Ip_Address]['udp'].keys())
elif resp == '3':
    print("Nmap version",  scanner.nmap_version())
    scanner.scan(Ip_Address, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[Ip_Address].state())
    print(scanner[Ip_Address].all_protocols())
    print("open ports", scanner[Ip_Address]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option")