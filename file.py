import os
cmd = "grep -i 'Denygroups server' /etc/ssh/sshd_config"
userdeny = os.system(cmd)
print(userdeny)
if userdeny != 0:
  f = open("/etc/ssh/sshd_config","a+")
  f.write("Denygroups server")
  print ("Provided access to server group\n")
  f.close()
else:
  print("Server group has already access\n")
