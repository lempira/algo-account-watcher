# Algorand Account Watcher Frontend Application

The directory contains the web application frontend

## Tech Used

| Lib or package    | Used for |
| :---------------- | :------: |
| Typescript        |   Language and typing   |
| Vite        |   Frontend Tooling   |
| React           |   Framework   |
| Tailwind    |  CSS Styling   |
| React Query |  State Management   |
| Jest |  Test   |
| ESLint |  Linting   |
| Prettier |  Formatting   |
| Docker |  Container Making   |
| GCP Cloud Run |  Deployment   |


## Local Development
The entry point for development is the package.json scrips. You start the development server with the following command

```
npm run dev
```

### Environmental Variables

```
# The local URL that points to the API.
VITE_API_URL=http://localhost:8000

# The URL that you want the app to run from. This can be localhost or something more specific as shown below
# If you choose to have something more specific, you will need to change your /etc/hosts file to map this to localhost
VITE_APP_URL=localhost.lempira.info

# Set only when running within a docker container in dev. (Used for docker compose)
VITE_DOCKER=false
```

## Running Tests

```
npm run test
```

## Deploy
There are many ways to deploy this application. The include DockerFile creates a repeatable environment image that can be pushed to you cloud platform of choice. I choose to deploy this to Google Cloud [Cloud Run](https://cloud.google.com/run/docs/deploying)

Create the Docker Image by running the following command from `frontend` folder.

```
docker build --file=src/deploy/Dockerfile.prod -t <your-tag> .
```