# Step 1: Build the Svelte application
# Use a node image to build the app
FROM node:14 as build-stage

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the source code
COPY . .

# Build the app
RUN npm run build

# Step 2: Serve the app using a lightweight node image
FROM node:14-alpine

# Install a simple http server for serving static content
RUN npm install -g serve

# Set environment variable for Azure to assign port
ENV PORT=5000

# Copy the built app from the previous stage
COPY --from=build-stage /app/public /public

# The port the app runs on
EXPOSE 5000

# Serve the app
CMD serve -s public -l tcp://0.0.0.0:${PORT}