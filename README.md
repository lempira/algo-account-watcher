# Algorand Account Watcher

The Algorand Account Watcher is an application and REST API that tracks Algorand account balances for changes and allows you to see the current account balance as well as the account history. The demo apps are shown below but you can also run this locally or deploy to your platform of choice (See below)

## Demo Apps

The frontend and backend applications are deployed on [Google Cloud Run](https://cloud.google.com/run?hl=en)

### API Docs

The API documentation is provided via Swagger Open API, making it easy to explore, test, and integrate the various features offered by Algorand Account Watcher. To access the Swagger API docs, navigate to /docs endpoint of the application by clicking the link below

[View API Docs](https://algo-api-qjbijoctfa-uc.a.run.app/docs#/).

![image](https://storage.googleapis.com/algorand-account-watcher/algorand-account-watcher-api.png)

### Web Application

The web application interacts with the API to manage and see the accounts you are watching.

[Go To Web App](https://algo-app-qjbijoctfa-uc.a.run.app/).

![image](https://storage.googleapis.com/algorand-account-watcher/algorand-account-watcher-app.png)

## Running locally

In order to run both the backend API and frontend application locally you must first install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) on your machine. Once you have both installed run the following command at the same level as the docker-compose.yml file

```
docker compose up
```

The first time you run this will take a little while because it's building both the frontend and backend images. You'll know frontend and backend are ready from the text below

Web Application (frontend) Ready

```
algo-app-dev  | > frontend@0.0.0 dev
algo-app-dev  | > vite
algo-app-dev  |
algo-app-dev  |
algo-app-dev  |   VITE v5.3.3  ready in 339 ms
algo-app-dev  |
algo-app-dev  |   ➜  Local:   http://localhost:5173/
algo-app-dev  |   ➜  Network: http://192.168.144.2:5173/
```

API (backend) Ready

```
algo-api-dev  | INFO:     Loading config settings from the environment...
algo-api-dev  | INFO:     Started server process [7]
algo-api-dev  | INFO:     Waiting for application startup.
algo-api-dev  | INFO:     Creating a new application lifecycle context...
algo-api-dev  | INFO:     Checking the state of watched accounts...
algo-api-dev  | INFO:     Application startup complete.
algo-api-dev  | INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
algo-api-dev  | INFO:     Checking the state of watched accounts...
```

You can access the frontend application by going to `http://localhost:5173/`, You can access the backend api docs `http://localhost:8000/docs`

Run the following command to stop both applications

```
docker compose down
```

## Developing the application

See the READMEs of the individual backend and frontend folders for information on how to set up the applications for development individually and together. VsCode was used to develop the application and workspaces where used to keep the configurations specific to the frontend and backend applications

## Further Enhancements

Due to time constraints, these are some of the functionality that I didn't get to implement in the order I would implement them:

- Full test coverage - I wrote tests for both frontend and backend that ensure the major functionality was covered, but I didn't write tests for all of the functions and components
- Implement CI/CD - I have deployed these services manually to Cloud Run so any updates go through the manual process of linting, running tests, building the images, and deploying the app. A CI/CD pipeline would automate this process so that merges to main branch would automatically deploy a new version if all of checks pass. I would use Github Actions for the pipeline and then configure Cloud Run to listen for changes on the github repo.
- Swap the SQL Lite database for something more robust and can be managed separately with a cloud service (i.e. DB as a service) However, this decision would depend on the requirements for storing, processing, and retriving the data. Embedding databases like SQL Lite are quite robust and reduce the complexity of the apps quite a bit. There cases where [companies use SQL Lite in production](https://www.sqlite.org/famous.html).
- Use websockets for communciations with the backend - Currently, the web application relies on polling to get the current state. Web sockets would allow me to remove the refresh button by having the server push the notifications to the client.
- Break up the frontend and backend into separate repos - I put the repos for demonstration purposes only. Breaking up the repos would decouple the repods and make maintenance much easier.

![image](https://i.giphy.com/media/73oW01Plu9O5HAOdEH/giphy.gif)
