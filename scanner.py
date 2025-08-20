import socket  # This imports Python’s socket library, which allows us to create network connections.

def scan_ports(target, ports):
    print(f"\n[+] Scanning target: {target}\n")
    for port in ports:
        try:  # means attempt this, but don’t crash if it fails
            #create socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tells Python we’re using IPv4 addresses.And that wwe’re using TCP connections.
            sock.settimeout(1) # only wait 1 second per port

            result = sock.connect_ex((target, port))  #connect_ex tries to connect to the target’s port.
            if result == 0:  # If it returns 0, it means the connection was successful
                print(f"[OPEN] Port {port}")

                # try banner grabbing
                try:
                    sock.send(b"Hello\r\n")  #sending a small message (Hello\r\n) to the service running on that port.
                    banner = sock.recv(1024).decode().strip()
                    if banner:
                        print(f"    Banner:  {banner}")
                          
                except:
                    print("   Banner: Not available")
        
        except Exception:
            pass
        finally:
            sock.close()    


if __name__ == "__main__":          
    target_ip = input("Enter target IP/Domain: ")
    ports_to_scan = range(20, 1025)
    scan_ports(target_ip, ports_to_scan)
    
                