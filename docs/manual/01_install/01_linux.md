<!-- import CloneInstructions from '../_partials/cloneInstructions.md' -->
<!-- import AcceptCertificates from '../_partials/acceptCertificates.md' -->

# Installation on Linux

## Pre-Install Checklist
1. Ensure you have at least 16GB of RAM  
  _You may run int issues running the full development setup with less_
2. Clone the repository to a location whose path **contains no spaces**.
3. Install Node.js 22  
  _(versions earlier than 22 are not guaranteed to work)_
4. Install Python >=3.6, [PIP](https://pypi.org/project/pip/), C++, and other build tools  
  _See the [Mediasoup install instructions](https://mediasoup.org/documentation/v3/mediasoup/installation/) for full details._
5. Install Docker  
  _Optionally: If you're NOT using docker, install MariaDB, Redis and MinIO manually and update repo's `.env.local` accordingly._

You should now be ready to follow the [Quick Start](#quick-start) instructions.

### Clone the repository
A lot has changed during development, and our monorepo has gotten quite large.  
To avoid cloning everything, use this command:

<!-- Start of partial: CloneInstructions -->
```bash
git clone https://github.com/ir-engine/ir-engine --depth 1
```
> **Warning**:  
> Adding `--depth=1` will significantly reduce the amount of data downloaded when cloning, but it will also create a `Shallow Copy` of the engine's repository.  
If you need to download any branch other than `dev`, or go back in git history into an older commit, you will have to unshallow the repository first, or else any branches and older commits won't be accessible. The command to undo cloning with `--depth=N` is either `git fetch --unshallow` or `git pull --unshallow`

<!-- End of partial: CloneInstructions -->

### Ensure you are running Node 22
The engine to date has only been confirmed to work with Node 22.x.  
Earlier or later major versions are not guaranteed to work properly.

The best way to install and manage Node.js versions is by using a version manager:
1. Install [NVM](https://github.com/nvm-sh/nvm)
2. Install Node.js 22 with `nvm install 22`
3. _(Optional)_ Make Node.js 22 your default node version with `nvm alias default 22`

_Note: Polyglot [ASDF](https://github.com/asdf-vm/asdf) can also be used for managing node versions._

Please check the output of `node --version` before running the engine.  
If you are using a node version below 22, please update or nothing will work.   
You will know that you are having issues if you try to install packages at root with `npm install` and you get package dependency errors.

### Docker is your friend
You don't need to use [Docker](https://docs.docker.com/), but it will make your life much easier.  
If you don't wish to use Docker, you will need to setup mariadb and redis on your machine. You can find credentials in `/scripts/docker-compose.yml`

## Quick Start
If you are lucky, this will just work. However, you may encounter some issues.  
Make sure you are running Node 22, and check your dependencies.
```
cd path/to/ir-engine
cp .env.local.default .env.local
npm install
npm run dev-docker
npm run dev-reinit
npm run dev
```
Now run iR Engine in your browser by navigating to [https://localhost:3000/location/default](https://localhost:3000/location/default).  

### Accept Certificates
<!-- Start of partial: AcceptCertificates -->
### Step 4: Accept the certificates

When accessing the iR Engine for the first time, browsers block access due to **self-signed certificates**. This prevents you from accessing the Admin panel and the Editor. To bypass this, manually accept the certificates:

:::::workflow-block
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

::::workflow-block-item
**Bypass the security warning**

1. Open these URLs directly in your browser:
2. [https://localhost:3030](https://localhost:3030)
3. [https://localhost:8642](https://localhost:8642)
4. A **"Your connection is not private"** warning appears.
5. Click **Advanced** → **Proceed to localhost (unsafe)**.
6. Reload the engine’s website.

:::hint{type="info"}
** Why bypassing security warnings?**
Browsers block connections to self-signed certificates by default to protect users from potentially unsafe sites.&#x20;

For local development, it's safe to bypass these warnings, but only if you trust the source—like your own machine or your team's local environment.
:::
::::
:::::

:::hint{type="success"}
Once completed, the iR Engine’s admin panel and editor will be fully accessible. 🚀
:::

> _Note: You will be able to create signed certificates to replace the default ones when you deploy your own iR Engine stack._

<!-- End of partial: AcceptCertificates -->

### Admin System and User Setup
You can administrate many features from the admin panel found at the `/admin` route of your deployment.  
_eg: `https://localhost:3000/admin` when working in a local deployment._

To give administration rights to a user:
- Open any page in your iR Engine deployment
- Open the user menu _(icon at the top-right of the screen)_
- Click on `Show API key`
- Copy that key to your clipboard _(note: there is an icon to the right of this box for this purpose)_
- Open a terminal and go to the folder where EtherealEngine was cloned.
- Run the command `npm run make-user-admin -- --id={COPIED_USER_ID}` where `COPIED_USER_ID` is the key you just copied on the previous step.  
  Example: `npm run make-user-admin -- --id=c06b0210-453e-11ec-afc3-c57a57eeb1ac`

![image](../images/userid.png)

> Alternate Method:  
> Open the `User` table of your deployment's database and change `userRole` to `admin`  
_(It helps to use a graphical database explorer, we recommend [beekeeperstudio.io](https://beekeeperstudio.io/))_
The location of the database can be found in your `.env.local` file.

Test user Admin privileges by going to the `/admin` route of your deployment.


## Advanced Installation and Troubleshooting
If you run into any trouble with the Quick Start instructions:
- Please make sure you've followed the 
  [Mediasoup installation instructions](https://mediasoup.org/documentation/v3/mediasoup/installation/)
- Check your OS-specific instructions:
  - [Installing on Windows (10+)](./windows)
  - [Installing on Mac OS X](./macOSX)
- [Installation Troubleshooting](./advanced/troubleshooting)
- [Advanced Setup](./advanced)
- [Vite dev server is stalling](https://vitejs.dev/guide/troubleshooting.html#dev-server)

