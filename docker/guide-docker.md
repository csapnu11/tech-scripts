# Docker Cheat Sheet

## 1. Basic Docker Commands

### Start/Stop/Restart Containers
- **Start a container**:  
  `docker start <container_name_or_id>`
- **Stop a running container**:  
  `docker stop <container_name_or_id>`
- **Restart a container**:  
  `docker restart <container_name_or_id>`

### Manage Containers
- **List all running containers**:  
  `docker ps`
- **List all containers (including stopped ones)**:  
  `docker ps -a`
- **View logs of a container**:  
  `docker logs <container_name_or_id>`
- **Access a running container's shell**:  
  `docker exec -it <container_name_or_id> /bin/bash`
- **Remove a container**:  
  `docker rm <container_name_or_id>`
- **Remove all stopped containers**:  
  `docker container prune`

### View Container Stats
- **Monitor container resource usage**:  
  `docker stats`

---

## 2. Docker Images Commands

### Build Images
- **Build an image from a Dockerfile**:  
  `docker build -t <image_name> <path_to_dockerfile>`

### Manage Images
- **List all images**:  
  `docker images`
- **Pull an image from Docker Hub**:  
  `docker pull <image_name>`
- **Remove an image**:  
  `docker rmi <image_name_or_id>`
- **Remove unused images**:  
  `docker image prune`

### Tagging and Pushing Images
- **Tag an image**:  
  `docker tag <source_image> <target_image>`
- **Push an image to a Docker registry**:  
  `docker push <image_name>`

---

## 3. Docker Networking Commands

### Network Commands
- **List networks**:  
  `docker network ls`
- **Create a new network**:  
  `docker network create <network_name>`
- **Inspect a network**:  
  `docker network inspect <network_name>`
- **Connect a container to a network**:  
  `docker network connect <network_name> <container_name_or_id>`
- **Disconnect a container from a network**:  
  `docker network disconnect <network_name> <container_name_or_id>`

---

## 4. Docker Volumes Commands

### Manage Volumes
- **List volumes**:  
  `docker volume ls`
- **Create a volume**:  
  `docker volume create <volume_name>`
- **Inspect a volume**:  
  `docker volume inspect <volume_name>`
- **Remove a volume**:  
  `docker volume rm <volume_name>`
- **Remove unused volumes**:  
  `docker volume prune`

---

## 5. Docker Compose Commands

### Manage Compose Applications
- **Start all services in a Compose file**:  
  `docker-compose up`
- **Start services in the background (detached mode)**:  
  `docker-compose up -d`
- **Stop services**:  
  `docker-compose down`
- **Build services (if changes made to Dockerfile)**:  
  `docker-compose build`
- **View logs of services**:  
  `docker-compose logs`
- **Execute command inside a running service container**:  
  `docker-compose exec <service_name> <command>`

### Compose Scaling
- **Scale services**:  
  `docker-compose up --scale <service_name>=<number_of_instances>`

---

## 6. Dockerfile Related Commands

### Common Dockerfile Instructions
- **FROM**: Specifies the base image to use.
- **RUN**: Execute commands during the image build.
- **COPY**: Copy files from your local system into the container.
- **CMD**: Default command to run when a container starts.
- **ENTRYPOINT**: The command that always runs when the container starts.

Example:
```dockerfile
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y curl
COPY . /app
CMD ["python", "/app/app.py"]

```


## 7. Docker System Commands

### Clean Up Resources
- **Remove unused containers, networks, images, and build cache**:  
  `docker system prune -a`
- **Remove unused data (containers, images, networks, volumes)**:  
  `docker system prune`

### Check Docker System Usage
- **Display system-wide information**:  
  `docker info`
- **Show disk usage**:  
  `docker system df`

---

## 8. Docker Container Logs and Debugging

### Log Commands
- **Show logs of a container**:  
  `docker logs <container_name_or_id>`
- **Follow logs in real-time**:  
  `docker logs -f <container_name_or_id>`
- **Tail logs**:  
  `docker logs --tail <number> <container_name_or_id>`

### Debugging Containers
- **Inspect container details**:  
  `docker inspect <container_name_or_id>`
- **Display the container's environment variables**:  
  `docker exec <container_name_or_id> env`

---

## 9. Docker Health Checks

### Health Check in Dockerfile
To add a health check in a Dockerfile:
```dockerfile
HEALTHCHECK CMD curl --fail http://localhost:8080/health || exit 1
```

## 10. Docker Security Commands

### Running Containers with User Permissions
- **Run container as a specific user**:  
  `docker run --user <user_id>:<group_id> <image_name>`

### Limit Container Resources
- **Limit CPU**:  
  `docker run --cpus="1.5" <image_name>`
- **Limit Memory**:  
  `docker run --memory="500m" <image_name>`

---

## 11. Docker Registries

### Log in to Docker Registry
- **Log in to Docker Hub or a private registry**:  
  `docker login <registry_url>`

### Tag and Push Images to Custom Registry
- **Tag image for custom registry**:  
  `docker tag <image_name> <registry_url>/<image_name>:<tag>`
- **Push image**:  
  `docker push <registry_url>/<image_name>:<tag>`

---

## Miscellaneous Docker Commands

- **Show system-wide Docker events**:  
  `docker events`
- **Check for potential security vulnerabilities in images**:  
  `docker scan <image_name>`


- **To delete all containers including its volumes use,**:
  
  `docker rm -vf $(docker ps -aq)`

- **To delete all the images,**:
  
  `docker rmi -f $(docker images -aq)`
