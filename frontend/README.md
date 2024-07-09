# Algorand Account Watcher Frontend Application

The directory contains the web application frontend

## Tech Used

| Lib or package |      Used for       |
| :------------- | :-----------------: |
| Typescript     | Language and typing |
| Vite           |  Frontend Tooling   |
| React          |      Framework      |
| Tailwind       |     CSS Styling     |
| React Query    |  State Management   |
| ViTest         |        Test         |
| ESLint         |       Linting       |
| Prettier       |     Formatting      |
| Docker         |  Container Making   |
| GCP Cloud Run  |     Deployment      |

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

## Linting and Formatting

The frontent uses eslint and prettier for linting and formatting. You can run the following command to lint and format the entire codebase. In additionl you should install the [eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) and [prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) plugins so you can lint and format as you go.

```
npm run lint
```

```
npm run format
```

## Running Tests

There are several ways to run frontend test.

```
npm run test # Normal Way
npm run test:ui # A more pleasant UI interface for test
```

### Test Coverage

You can run test coverage with the following command

```
npm run test:coverage
```

Below is a sample of the current (2024-07-09) coverage. You can see it's pretty absymal :/. Given more time, I would focus on improving the frontend testing.

```
% Coverage report from v8
-----------------------------|---------|----------|---------|---------|-------------------
File                         | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
-----------------------------|---------|----------|---------|---------|-------------------
All files                    |   46.24 |    69.04 |   46.42 |   46.24 |
 frontend                    |       0 |        0 |       0 |       0 |
  postcss.config.mjs         |       0 |        0 |       0 |       0 | 1-14
  tailwind.config.ts         |       0 |        0 |       0 |       0 | 1-15
 frontend/src                |   13.95 |        0 |       0 |   13.95 |
  App.tsx                    |       0 |        0 |       0 |       0 | 1-16
  Container.tsx              |       0 |        0 |       0 |       0 | 1-24
  constants.ts               |     100 |      100 |     100 |     100 |
  main.tsx                   |       0 |        0 |       0 |       0 | 1-8
 frontend/src/components     |   52.57 |    77.14 |   54.54 |   52.57 |
  AccountBar.tsx             |   68.83 |      100 |      40 |   68.83 | 21-34,38-49
  AccountHistory.tsx         |     100 |      100 |     100 |     100 |
  AddressInput.tsx           |       0 |        0 |       0 |       0 | 1-97
  ComponentErrorBoundary.tsx |     100 |      100 |     100 |     100 |
  HelpText.tsx               |       0 |        0 |       0 |       0 | 1-25
  Navbar.tsx                 |       0 |        0 |       0 |       0 | 1-32
  NotificationTable.tsx      |   96.51 |    73.33 |     100 |   96.51 | 64,73-74
  RefreshAddresses.tsx       |     100 |      100 |     100 |     100 |
  WatchedAddresses.tsx       |       0 |        0 |       0 |       0 | 1-61
  api.ts                     |   30.76 |      100 |       0 |   30.76 | 5-7,10-14,17-18
 frontend/src/scripts        |       0 |      100 |     100 |       0 |
  setupProxy.ts              |       0 |      100 |     100 |       0 | 7-24
 frontend/src/utils          |     100 |      100 |     100 |     100 |
  test-utils.tsx             |     100 |      100 |     100 |     100 |
-----------------------------|---------|----------|---------|---------|-------------------
```

## Deploy

There are many ways to deploy this application. The include DockerFile creates a repeatable environment image that can be pushed to you cloud platform of choice. I choose to deploy this to Google Cloud [Cloud Run](https://cloud.google.com/run/docs/deploying)

Create the Docker Image by running the following command from `frontend` folder. Be sure to run the `npm run lint` and `npm run check-types` prior to building the image. The image will fail if these do not pass.

```
docker build --file=src/deploy/Dockerfile.prod -t <your-tag> .
```
