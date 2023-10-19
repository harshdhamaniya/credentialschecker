from flask import Flask, request, render_template
import paramiko
from smb.SMBConnection import SMBConnection
import os
import threading

app = Flask(__name__)

def check_smb(ip_address, username, password, smb_results):
    try:
        conn = SMBConnection(username, password, "myclient", "myserver", use_ntlm_v2=True)
        if conn.connect(ip_address, 139):
            # Check user access role
            user_info = conn.get_session_info()
            conn.close()
            smb_results.append(f"{ip_address} : SMB Login Successful. User Access Role: {user_info['User']['account_name']}")
        else:
            smb_results.append(f"{ip_address} : SMB Login Failed")
    except Exception as e:
        smb_results.append(f"{ip_address} : SMB Error - {str(e)}")

def check_ssh(ip_address, username, password, ssh_results):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_address, username=username, password=password)

        # Check user access role
        stdin, stdout, stderr = ssh.exec_command("whoami")
        user_access = stdout.read().decode().strip()
        ssh.close()

        ssh_results.append(f"{ip_address} : SSH Login Successful. User Access Role: {user_access}")
    except paramiko.AuthenticationException:
        ssh_results.append(f"{ip_address} : SSH Login Failed (Authentication Error)")
    except paramiko.SSHException as e:
        ssh_results.append(f"{ip_address} : SSH Error - {str(e)}")
    except Exception as e:
        ssh_results.append(f"{ip_address} : SSH Error - {str(e)}")

def check_multiple_ips(ip_addresses, username, password, smb_enabled, ssh_enabled):
    smb_results = []
    ssh_results = []
    threads = []

    for ip in ip_addresses:
        ip = ip.strip()  # Remove leading/trailing whitespace

        if smb_enabled:
            smb_thread = threading.Thread(target=check_smb, args=(ip, username, password, smb_results))
            threads.append(smb_thread)
            smb_thread.start()

        if ssh_enabled:
            ssh_thread = threading.Thread(target=check_ssh, args=(ip, username, password, ssh_results))
            threads.append(ssh_thread)
            ssh_thread.start()

        # Limit the number of threads to 10
        if len(threads) >= 10:
            for thread in threads:
                thread.join()
            threads = []

    # Wait for any remaining threads to finish
    for thread in threads:
        thread.join()

    return smb_results, ssh_results

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ip_addresses = request.form.get("ip_addresses").splitlines()
        username = request.form.get("username")
        password = request.form.get("password")
        smb_enabled = request.form.get("smb_enabled")
        ssh_enabled = request.form.get("ssh_enabled")

        smb_results, ssh_results = check_multiple_ips(ip_addresses, username, password, smb_enabled, ssh_enabled)

        return render_template("index.html", smb_results=smb_results, ssh_results=ssh_results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8015)
