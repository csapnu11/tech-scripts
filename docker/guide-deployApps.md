### Guide to Deploy a Next.js Project in Docker

This guide will walk you through deploying a Next.js application using Docker.

### Prerequisites

1. **Docker**: Ensure Docker is installed on your machine.
2. **Next.js Project**: Have a Next.js project ready.

### Step 1: Create the Next.js Project (if not already created)

If you don't have a Next.js project, create one by running the following commands:

```bash
npx create-next-app@latest my-next-app
cd my-next-app
```

### Step 2: Set Up the Dockerfile

Create a `Dockerfile` in the root of your Next.js project directory. This file defines how Docker should build the application image.

#### Dockerfile

```Dockerfile
# Use official Node.js image as the base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy all other source code
COPY . .

# Build the Next.js project
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Start the Next.js app
CMD ["npm", "start"]
```

### Step 3: Create .dockerignore File

To prevent unnecessary files from being included in the Docker image, create a `.dockerignore` file in the root of your project.

#### .dockerignore

```dockerfile
node_modules
npm-debug.log
Dockerfile
.dockerignore
.next
```

### Step 4: Build the Docker Image

Now, you need to build the Docker image. Open your terminal and navigate to your project directory. Run the following command to build the Docker image:

```bash
docker build -t nextjs-app .
```

This command will create a Docker image with the name `nextjs-app`.

### Step 5: Run the Docker Container

After the image is built, run it using the following command:

```bash
docker run -p 3000:3000 nextjs-app
```

Run docker in detached mode(in background)

```bash
docker run -d -p 3000:3000 nextjs-app

```

This will start the Next.js app in the Docker container and expose it on port 3000.

### Step 6: Verify the Application is Running

Open a browser and visit `http://localhost:3000`. You should see the Next.js app running.

### Step 7: Clean Up (Optional)

To remove the Docker container after testing, use the following commands:

1. List running containers:

   ```bash
   docker ps
   ```

2. Stop the container:

   ```bash
   docker stop <container_id>
   ```

3. Remove the container:

   ```bash
   docker rm <container_id>
   ```

### Step 8: Push the Docker Image to Docker Hub (Optional)

If you want to push your image to Docker Hub for remote access, follow these steps:

1. Login to Docker Hub:

   ```bash
   docker login
   ```

2. Tag your image:

   ```bash
   docker tag nextjs-app your-dockerhub-username/nextjs-app:latest
   ```

3. Push your image to Docker Hub:

   ```bash
   docker push your-dockerhub-username/nextjs-app:latest
   ```

### Conclusion

You have successfully containerized your Next.js app using Docker. You can now deploy it to any environment that supports Docker, and it will run the same way every time.
