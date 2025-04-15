FROM node:23-alpine


WORKDIR /app
COPY package.json .
RUN npm install

COPY . .

EXPOSE 5500

CMD ["/usr/local/bin/npm", "run", "docker"]

# CMD ["npm ", "run", "dev"]
