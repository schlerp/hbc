# HomeBrew Comps

It's an app for managing a homebrew club's competitions and user profiles etc.

## Architecture

The backend uses a microservices architecture where all internal calls between microservices are routed using rabbitMQ and any externally facing API's are implemented as REST API's running in containers. There are certain fields that are important for calling data between services they are shown in the data architecture below.

![HBC ERD](.assets/hbc_erd.svg)

The front end is written in react.

## Usage

```bash
git clone https://github.com/schlerp/hbc.git

cd hbc

docker-compose up

# navigate to http://localhost:3000 in browser
```

## authors

- Patrick Coffey (schlerp)
- Matt Elvey (melvey)
