## Walking Through

This file will guide you through the steps outlined in the [Getting Started](README.md#getting-started) section of the 
[README.md](README.md). Make sure you have your environment installed and running before proceeding.

### Environment Setup

In this lab, we are using the following environment configuration:

**Ansible Server:**
- Name: AnsibleServer
- IP: 172.18.20.2
- Operating System: Linux CentOS/8

**Ansible Client:**
- Name: AnsibleClient
- IP: 172.18.20.3
- Operating System: Linux CentOS/8

### Steps

1. **Control Machine**
Install python 
Install [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-and-upgrading-ansible) package.
Install SSH.

### Configuring targets
Controller machine needs to connect with the targets (host clients).
When we connect in another host using SSH command, the command syntax is:
```commandline
ssh -i key_path username@ip_address
```

We need to provide the same info to Ansible.
Connect into the controller machine by ssh and create a get into the folder hosts_{}.

Create the inventory file:
Inventory file provides information about the targets.
- User name;
- Password;
- Login keys;
- Port number;
- Whatever you need to log in the target machine

If you are not writing a inventory file, Ansible will use /etc/ansible/hosts as default inventory. You can also specify
other inventories file specifying the path.
An example can be followed in [inventory.yaml](inventories/inventory.yaml) 
My lab:
```yaml
all:
  hosts:
    host:
      ansible_host: 172.17.8.103  # VM host provide by Vagrant
      ansible_user: vagrant       # Default user
      ansible_private_key_file: ~/.ssh/id_rsa
```

Define the user, password and private key parameter;
Obs: private key permission must be 600 - in AWS host 400
Obs: Disable ssh connection message:
** Create/Change in the Ansible control host a file called ansible.cfg **
- Go to /etc/ansible/ --> make a back of ansible.cfg to ansible.cfg_bkp
- Run the command: 
- 
```commandline
ansible-config init --disable -t all > ansible.cfg
```
It will create a new ansible.cfg file
- Open the ansible.cfg file --> search for "host_key_checking" uncomment and change it to False.
```text
host_key_checking=False
```
In my case I am using a vm CentOS 8 running a Jenkins docker.
Inside the Jenkins docker I can run Ansible and Python command which were built in the Jenkins image.
In order to make my environment I need to log in inside the CentOS 8 VM, change to user root and then change to user
jenkins:
```text
vagrant ssh vm-centos
sudo -i
su - jenkins
docker exec -u jenkins -it container_name bash
```
This way I can access the jenkins ssh private key. 
```text
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""
chmod 700 ~/.ssh
ssh-copy-id vagrant@your_target_host 
ssh vagrant@your_target_host
```

Test:
```commandline
ansible host -m ping -i invetory.yaml
```
If you get a fingerprint question, check the observation of ansible.cfg file above.
If you get UNREACHABLE permission error, change the private key permission to 400 (AWS host) 600 (VM host)

