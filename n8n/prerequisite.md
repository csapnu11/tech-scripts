

## n8n installation via docker

### Create user dedicate for docker use


Here’s how you can create a dedicated user for Docker:

1. **Create a new user**:
   You can create a new user specifically for running Docker commands:

   ```bash
   sudo useradd -m -s /bin/bash dockeruser
   ```

   This command creates a new user named `dockeruser` with a home directory and a shell for login.

2. **Add the new user to the Docker group**:
   Next, add the `dockeruser` to the `docker` group so they can run Docker commands without `sudo`:

   ```bash
   sudo usermod -aG docker dockeruser
   ```

3. **Verify the new user**:
   You can verify that `dockeruser` is in the Docker group by running:

   ```bash
   getent group docker
   ```

   This should show the `docker` group and list the `dockeruser` as a member.

4. **Test the user**:
   Log in as the new user (or use `su` to switch to the new user) and run a Docker command to verify everything is working:

   ```bash
   su - dockeruser
   docker ps
   ```

   This should allow `dockeruser` to run Docker commands without `sudo`.




### Creation of directories

- **Create main dir**
```
sudo mkdir /<path>/n8n-server
```


- **Create ENV file**
```env
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=<your-user>
N8N_BASIC_AUTH_PASSWORD=<your-password>
N8N_HOST=<your-host-ip>
N8N_PORT=5678
N8N_PROTOCOL=http
N8N_SECURE_COOKIE=false
NODE_ENV=production
GENERIC_TIMEZONE="Asia/Taipei"
TZ="Asia/Taipei"
N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true
N8N_RUNNERS_ENABLED=true


```


- **Create docker volume**
```
docker volume create n8n_data
```


- **Create and run docker**
```
docker run -it --rm -d --name n8n -p 5678:5678 --env-file .env -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n

```

-- rm : auto remove container

-d : detached mode

-i (interactive): Keeps stdin open so that you can interact with the container

-t (tty): Allocates a pseudo-terminal, which allows you to run interactive commands like a shell inside the container
