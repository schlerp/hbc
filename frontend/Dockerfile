FROM node:12 AS build

WORKDIR /app

COPY package.json ./
RUN yarn install
COPY . ./
RUN yarn build

FROM nginx:1.19-alpine
COPY --from=build /app/public /usr/share/nginx/html
