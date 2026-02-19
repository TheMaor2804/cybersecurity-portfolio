# Active Directory Domain Lab & Security Hardening (Virtual Enterprise)

## 📌 Project Overview
This project demonstrates the design and implementation of a simulated enterprise Active Directory environment using VirtualBox.  
The lab includes a Windows Server Domain Controller (AD DS + DNS), a Windows 10 domain-joined client, and a Kali Linux machine connected through an isolated NAT network.

The objective was to gain hands-on experience with domain administration, identity management, and baseline security hardening aligned with SOC / Blue Team practices.

---

## 🧱 Lab Architecture
| Machine | OS | Role |
|--------|----|------|
| Server20 | Windows Server | Domain Controller (AD DS + DNS) |
| PC1 | Windows 10 | Domain-Joined Client |
| Kali | Kali Linux | Testing & Connectivity Validation |

All machines were connected using a VirtualBox NAT Network named **“Virtualization”**.

---

## ⚙️ Technologies & Tools
- Windows Server (Active Directory Domain Services)
- DNS Server
- Group Policy Management (GPO)
- VirtualBox
- Windows 10
- Kali Linux
- Windows Defender Firewall
- NAT Networking

---

## 🛠️ Implementation Steps
### 1. Virtual Environment Setup
- Created Windows Server, Windows 10, and Kali Linux virtual machines
- Installed Guest Additions and configured system resources
- Connected all VMs to a shared NAT Network for isolated lab simulation

### 2. Domain Controller Deployment
- Configured static IP on the Windows Server
- Set DNS to localhost (127.0.0.1)
- Installed Active Directory Domain Services (AD DS)
- Promoted the server to a Domain Controller

### 3. Domain Join & DNS Configuration
- Renamed Windows client to PC1
- Configured client DNS to point to the Domain Controller
- Successfully joined PC1 to the domain
- Created DNS record for domain client resolution

### 4. Identity & Access Management
- Created Organizational Units (OUs) for departments:
  - IT
  - HR
  - QA
  - Designers
  - Developers
- Created domain users and managed group memberships
- Delegated administrative privileges for lab testing

---

## 🔐 Security Hardening Implemented
- Account lockout policy after 3 failed login attempts
- Group Policy restrictions:
  - Blocked Command Prompt access for HR
  - Blocked Control Panel access for QA
- Role-based file access permissions (Designers & Developers only)
- Windows Firewall ICMP rule configuration for controlled testing

---

## 🧪 Validation & Testing
- Verified connectivity between all VMs using ping tests
- Confirmed domain authentication and login functionality
- Validated DNS resolution inside the domain environment
- Tested GPO enforcement across different user roles
- Confirmed restricted folder access based on group permissions

---

## 🎯 SOC / Blue Team Relevance
This lab simulates a real enterprise Windows domain environment, which is highly relevant for Security Operations Center (SOC) and Blue Team roles.  
It demonstrates practical skills in:
- Active Directory administration
- Security policy enforcement (GPO)
- Identity and access management
- Domain security baseline hardening
- Enterprise network environment simulation

---

## 📄 Project Report
Full documentation and screenshots:  
[**Report.pdf**](./Report.pdf)
