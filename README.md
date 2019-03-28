# ssh_automation

In this automation, we are assuming, Server has group which contains many users like mahesh.
WE can control user accounts by adding or removing users into this server group.

The complete creation of server group, mahesh user creation and modify /etc/ssh/sshd_config file as per our requirement.

I was just denying access to "server" group, similarly if we want , we can provide access to server group by adding "Allowgroups server" in /etc/ssh/sshd_config file
