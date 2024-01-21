# Chose Base Image
FROM node:16

# Set working directory
WORKDIR /app

#install dependencies
COPY package.json package-lock.json* ./
RUN npm install

#Copy application code into container
COPY . .

#Build the app

#Production
# RUN npm run build
#For development, skip the build step

#Command to serve the app
#production:
# CMD ["serve", "-s", "build", "-l", "3000"]

#development
CMD ["npm", "start"]
