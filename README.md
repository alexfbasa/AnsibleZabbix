# AnsibleZabbix

AnsibleZabbix is a Git repository designed to simplify the deployment and configuration of Zabbix agents on Linux
hosts (VMs) using Ansible scripts. This project is intended to streamline the process of managing Zabbix monitoring for
your infrastructure and is integrated with a Jenkins pipeline for automated deployments.

## Table of Contents

- [Introduction](#ansiblezabbix)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
    - [Configuring Hosts](#configuring-hosts)
    - [Running the Ansible Playbook](#running-the-ansible-playbook)
- [Jenkins Pipeline Integration](#jenkins-pipeline-integration)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before using AnsibleZabbix, make sure you have the following prerequisites installed on your system:

- [Ansible](https://www.ansible.com/)
- [Zabbix Server](https://www.zabbix.com/) (Ensure the server is reachable from the hosts where Zabbix agents will be
  installed)
- [Jenkins](https://www.jenkins.io/) (For Jenkins pipeline integration)

### Installation

Clone the AnsibleZabbix repository to your local machine:

```bash
git clone https://github.com/your-username/AnsibleZabbix.git
cd AnsibleZabbix
```

## Usage

### Configuring Firewall Rules

Ensure that the Zabbix server and the hosts have appropriate firewall rules to allow communication between them. The
following ports are commonly used by Zabbix components:

- **Zabbix Server:**
    - Zabbix Server: Default port is 10051/TCP (can be configured in the Zabbix server settings).
    - Web Interface: Default port is 80/TCP or 443/TCP (if using HTTPS).

- **Zabbix Agents on Hosts:**
    - Default port is 10050/TCP (can be configured in the Zabbix agent settings).

Make sure to adjust your firewall rules accordingly to allow traffic on these ports. Failure to do so may result in
connectivity issues between the Zabbix server and the monitored hosts.

### Configuring Hosts

Edit the `hosts.yml` file to include the details of the Linux hosts where you want to install Zabbix agents.
Specify the host IP addresses, SSH credentials, and any other required information.

Example `hosts.yml`:

```yaml
zabbix_hosts:
  - name: example-host-1
    ip: 192.168.1.101
    user: your-ssh-user
    password: your-ssh-password
  - name: example-host-2
    ip: 192.168.1.102
    user: your-ssh-user
    password: your-ssh-password
```

### Running the Ansible Playbook

Execute the Ansible playbook to install Zabbix agents and configure the hosts:

```bash
ansible-playbook -i hosts.yml playbook.yml
```

This will deploy Zabbix agents on the specified hosts and automatically configure them within the Zabbix server.

## Jenkins Pipeline Integration

AnsibleZabbix is designed to work seamlessly with Jenkins pipelines. Configure a Jenkins pipeline job to trigger the
Ansible playbook automatically whenever changes are made to the repository.

Example Jenkinsfile:

```groovy
pipeline {
    agent any

    stages {
        stage('Deploy AnsibleZabbix') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'playbook.yml',
                        inventory: 'hosts.yml'
                    )
                }
            }
        }
    }
}
```

## Contributing

If you find issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
Contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

```

