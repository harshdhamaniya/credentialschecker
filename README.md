# **Credentials Checker SSH/SMB**

Credentials Checker SSH/SMB is a powerful and user-friendly GUI tool designed for bulk credential verification across SSH and SMB services. With the ability to check credentials over custom ports, this tool streamlines the process of verifying username and password combinations, making it an essential addition to any security professional's toolkit.

## **Features**

### **1. Bulk Credential Verification**

Easily verify username and password combinations for multiple IP addresses, saving you time and effort in the credential validation process.

### **2. SSH and SMB Support**

Credentials Checker SSH/SMB supports both SSH and SMB services, allowing you to check credentials for a wide range of systems and network shares.

### **3. Custom Port Support**

You have the flexibility to specify custom ports for credential checks, making it suitable for systems that don't use the standard SSH (22) and SMB (445) ports.

### **4. User-Friendly GUI**

The graphical user interface (GUI) provides an intuitive and user-friendly experience, making it accessible to both security experts and novices.

### **5. Detailed Reporting**

Generate detailed reports of the credential verification results, providing clear insights into the status of each IP address and associated credentials.

### **6. Bulk Input**

Upload a list of IP addresses and their associated username and password combinations in a user-friendly format, making bulk credential verification a breeze.

## **Installation**

### **Host via Python**
```
git clone "https://github.com/harshdhamaniya/credentialschecker.git"
sudo pip install -r requirements.txt
python app.py
```
- Web Based Application can be accessible at `http://localhost:8015/` OR `http://127.0.0.1:8015/`
- If you're hosting the application on VPS, you can access it via `http://<VPSIP Address>:8015/`

### **Windows Standalone**

Credentials Checker SSH/SMB is easy to install and runs on major operating systems. To get started, follow these steps:

1. Download the tool from [GitHub Releases](https://github.com/harshdhamaniya/credentialschecker/releases).
2. Install the tool on your system following the installation guide provided in the repository.

## **Usage**

Once installed, launch the tool and follow these steps:

1. Open the application.
2. Load a list of IP addresses and associated credentials.
3. Configure custom ports (if necessary).
4. Start the credential verification process.
5. Review the detailed report to identify successful and unsuccessful credential checks.

## **License**

Credentials Checker SSH/SMB is licensed under the [MIT License](https://github.com/harshdhamaniya/credentialschecker/blob/main/LICENSE), ensuring that it remains open and accessible to all.
