# Dockerfile for React frontend
FROM node:18

# Set the working directory
WORKDIR /app/rssapp

# Install dependencies
ADD ./rssapp .
RUN npm install

# Build the React app
RUN npm run build

# Serve the React app
CMD ["npm", "start"]
