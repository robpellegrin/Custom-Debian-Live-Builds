import socket
import sys
import subprocess

MANAGER_USERNAME = 'debian'
MANAGER_PASSWORD = 'password'

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    return local_ip

def listen_for_hostname():
    BROADCAST_PORT = 9999
    LOCAL_IP = get_local_ip()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', BROADCAST_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        hostname = data.decode()
        print(f"Received broadcast from {addr}: {hostname}")

        # Save the IP address to a file
        ip_address = addr[0]
        with open("manager.ipaddress", "w") as file:
            file.write(ip_address + "\n")
        print(f"Saved IP address {ip_address} to manager.ipaddress")

        # Mount the NFS volume from the manager node.
        mount_command = f"sudo mount {ip_address}:/home/{MANAGER_USERNAME}/MPI /home/user/MPI"
        try:
            subprocess.run(mount_command, shell=True, check=True)
            print(f"Successfully executed: {mount_command}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

        # Run ssh-keygen with default values
        try:
            subprocess.run("ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N ''", shell=True, check=True)
            print("Successfully generated SSH key.")
        except subprocess.CalledProcessError as e:
            print(f"Error generating SSH key: {e}")

        try:
            ssh_keyscan_command = f"ssh-keyscan -H {MANAGER_USERNAME}@{ip_address} >> ~/.ssh/known_hosts 2>/dev/null"
        except subprocess.CalledProcessError as e:
            print(f"An error has occurred: {e}")

        # Use sshpass to copy the SSH key, disabling strict host key checking.
        # From live to manager
        try:
            sshpass_command = f"sshpass -p '{MANAGER_PASSWORD}' ssh-copy-id -o StrictHostKeyChecking=no {MANAGER_USERNAME}@{ip_address}"
            subprocess.run(sshpass_command, shell=True, check=True)
            print("SSH key copied successfully")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

        # Use sshpass to copy the SSH key, disabling strict host key checking
        # From manager to live
        try:
            sshpass_command = f"ssh {MANAGER_USERNAME}@{ip_address} sshpass -p 'live' ssh-copy-id -o StrictHostKeyChecking=no user@{LOCAL_IP}"
            subprocess.run(sshpass_command, shell=True, check=True)
            print("SSH key copied successfully")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

        # Add an entry in the manager's allhost file with the username and ip address of the live distro.
        try:
            sshpass_command = f"ssh {MANAGER_USERNAME}@{ip_address} 'echo user@{LOCAL_IP} >> /home/{MANAGER_USERNAME}/allhosts'"
            subprocess.run(sshpass_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

        # Exit the script with status code 0
        sys.exit(0)

if __name__ == "__main__":
    listen_for_hostname()
