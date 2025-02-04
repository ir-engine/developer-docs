# Installing on macOS

## Introduction

This guide details the installation process for the iR Engine on macOS devices.

## Prerequisites

Ensure you have the following tools installed on your system before starting the installation:

- [Homebrew](https://brew.sh/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [nvm (Node Version Manager)](https://github.com/nvm-sh/nvm)
- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Installation instructions

Follow these steps to set up the iR Engine on your macOS device.

### Step 1: Prepare your project

First, generate a copy of the project by cloning the repository and navigate to the project directory:

::::workflow-block
:::workflow-block-item
Open your terminal
:::

:::workflow-block-item
Clone the repository by running:

```bash
git clone https://github.com/ir-engine/ir-engine.git
```
:::

:::workflow-block-item
Navigate to the directory of the cloned repository by running:

```bash
cd ir-engine
```
:::
::::

### Step 2: Set up environment variables

The iR Engine requires specific environment settings. Configure them by running:

```bash
cp .env.local.default .env.local
```

This command creates a copy of the default environment file, `.env.local.default`, renaming it to `.env.local` for use by the application.

### Step 3: Install and activate the recommended Node.js version

The iR Engine functions with a specific Node.js version, outlined in the `.nvmrc` file. To activate the recommended version, run:

```bash
nvm use
```

**Command output options**:

- **If the version is found (✅):** The system switches to the recommended Node.js version.
- **If the version is not found (❌):** The system returns a message indicating the missing version.

To resolve, run the following commands:

::::workflow-block
:::workflow-block-item
Install the missing version:

```bash
nvm install <version>
```
:::

:::workflow-block-item
Activate the version:

```bash
nvm use
```
:::
::::

### Step 4: Install dependencies

Install the required dependencies by running:

```bash
npm install
```

Upon completion, proceed to initialize and run your development environment.

## Run your development environment

This section contains the instructions to run your local development environment.

### Step 1: Start Docker and initialize the database

::::workflow-block
:::workflow-block-item
Open Docker Desktop
:::

:::workflow-block-item
Initialize the database by running:

```bash
npm run dev-reinit
```
:::
::::

### Step 2: Start the development environment

Launch the iR Engine development environment with:

```bash
npm run dev
```

:::hint{type="success"}
This command opens the application at [`https://localhost:3000/location/default`](https://localhost:3000/location/default) in your web browser.
:::

### Step 3: Open your development environment

Navigate to the [application's URL](https://localhost:3000/location/default) in your browser to start working with the iR Engine development environment.

### Step 4: Accept the certificates

When accessing the iR Engine for the first time, browsers block access due to **self-signed certificates**. This prevents you from accessing the Admin panel and the Editor. To bypass this, manually accept the certificates:

::::workflow-block
:::workflow-block-item
**Open Developer Tools**

- **Chrome/Edge:** Click the three-dot menu → *More tools* → *Developer tools*
- **Shortcut:** Press `Ctrl+Shift+I` or `F12`
- Navigate to the **Console** tab.
:::

:::workflow-block-item
**Identify certificate-related errors**

Check for network request errors related to:

- **WebSocket connections** (`wss://` URLs)
- **HTTPS requests to localhost**

The following addresses require certificate approval:

- `https://localhost:3030` – API server
- `https://localhost:8642` – File server
:::

:::workflow-block-item
**Bypass the security warning**

1. Open these URLs directly in your browser:
   - https\://localhost:3030
   - https\://localhost:3030
2. A **"Your connection is not private"** warning appears.
3. Click **Advanced** → **Proceed to localhost (unsafe)**.
4. Reload the engine’s website.
:::
::::

:::hint{type="success"}
Once completed, the iR Engine’s admin panel and editor will be fully accessible. 🚀
:::

:::hint{type="info"}
** Why bypassing security warnings?**
Browsers block connections to self-signed certificates by default to protect users from potentially unsafe sites. For local development, it's safe to bypass these warnings, but only if you trust the source—like your own machine or your team's local environment.
:::

