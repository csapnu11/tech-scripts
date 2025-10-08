

## Step-by-Step: Create a Non-Sudo SSH User on Ubuntu

### **1. Create the New User (Without Sudo Access)**

```bash
sudo adduser username
```

* Replace `username` with the desired username.
* This will:

  * Create the user.
  * Create `/home/username`.
  * Assign a default shell (`/bin/bash`).
  * Prompt for password and user info.

---

### **2. Verify the User Is Not in the `sudo` Group**

```bash
groups username
```

* If it lists `sudo`, remove the user:

```bash
sudo deluser username sudo
```

---

### **3. (Optional but Recommended) Disable Password Login for This User**

If you're planning to use **SSH key authentication**, do this:

#### a. Become the new user

```bash
sudo su - username
```

#### b. Create `.ssh` directory and add your public key

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
```

* Paste your **public SSH key** (from your local machine: `~/.ssh/id_rsa.pub`).
* Save and exit (`Ctrl+O`, `Ctrl+X`).

#### c. Set permissions

```bash
chmod 600 ~/.ssh/authorized_keys
exit
```

---

### **4. Confirm SSH Configuration Allows User Login**

Open the SSH daemon config:

```bash
sudo nano /etc/ssh/sshd_config
```

Check or add the following lines:

```text
PermitRootLogin no
PasswordAuthentication yes      # (or no, if using keys only)
AllowUsers username
```

* `AllowUsers` restricts SSH login to specified users (optional but more secure).
* Restart SSH to apply changes:

```bash
sudo systemctl restart ssh
```

---

### **5. Test SSH Login**

From another machine:

```bash
ssh username@your_server_ip
```
