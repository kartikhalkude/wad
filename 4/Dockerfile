# Use Node.js base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy files to container
COPY . .

# Install dependencies
RUN npm install

# Start the app
CMD ["npm", "start"]
