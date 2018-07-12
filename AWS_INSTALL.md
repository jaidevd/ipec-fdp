1. Install jupyterhub
2. Add a user to act as admin (jaidevd by default)
3. Gather a list of non-admin users and create users as follows:

```bash
for uname in $(cat users.txt); do
    useradd -m -s /bin/bash -N $uname
    echo $uname:$uname | chpasswd
done
```

4. Log into the admin panel of the JupyterHub and add all users from the file.
5. Each user needs to copy notebooks to his / her home directory from the terminal.
