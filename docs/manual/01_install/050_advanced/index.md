<!-- import AcceptCertificates from '../../_partials/acceptCertificates.md' -->

# Advanced Setup

The advanced setup is recommended for users who want to understand the internals of how the iR Engine's deployment stack works.
These instructions will explain how to manually setup iR Engine docker instances, client, server and/or instance-server.  

## 1. Install dependencies
```bash
cd path/to/ir-engine
npm install
```
_Note how you don't need to use sudo for any of these commands._

> If you find errors with mediasoup:
> - Follow the [Mediasoup Installation](https://mediasoup.org/documentation/v3/mediasoup/installation/) instructions
> - Check that your version of python is up to date: `python --version`
> - Make sure that the path where you installed iR Engine has no whitespaces

## 2. Start the MySQL database
Make sure you have a MySQL database installed and running. Our recommendation is `MariaDB`.

We provide a docker container for easily setting up the database. This command will create a Docker container of MariaDB named `ir-engine_db`:
```bash
npm run dev-docker
```
> Note: You must have docker installed on your machine for this script to work.  
If you do not have Docker installed, and do not wish to install it, you will have to manually create a MariaDB server.


The default database information is:
| | |
|-|-|
| Username | `server` |
| Password | `password` |
| Database | `ir-engine` |
| Hostname | `127.0.0.1` |
| Port     | `3306` |
> Note: If you have errors connecting to the local database, you might need to shut off your local firewall.


## 3. Start the server in database seed mode
Several tables in the database need to be seeded with default values.  
To do so, run:
- Unix: `npm run dev-reinit`
- Windows: `npm run dev-reinit-windows`

There should be no more logging after several seconds.  
If the database has been correctly seeded, some of the final lines should read like this:
```bash
Server Ready
Executing (default): SET FOREIGN_KEY_CHECKS = 1
Server EXIT
```

## 4a. Run all processes in separate tabs from script (optional)

You can start all of the processes in separate tabs with a single command. From the project root, run
```bash
npm run dev-tabs
```

This will start  agones, the client, the api server, the world and media instanceservers, and the local file server in separate tabs.

If you do this, you do not need to manually run steps 4b, 5, and 6, and can skip to step 7.


## 4b. Start Agones (if you did not run step 4a)
Open a new terminal and start the Agones sidecar in local mode
```bash
npm run dev-agones
```
Alternatively, you can also go to `ir-engine/vendor/agones/` and run:
- Linux: `./sdk-server.linux.amd64 --local`
- Windows: `sdk-server.windows.amd64.exe --local`
- Mac: `./sdk-server.darwin.amd64 --local`

## 5. Local file server configuration (Optional)
If the `.env.local` file you have has this line, the Scene Editor will save components, models, scenes, etc. locally, instead of storing them on the `S3` cloud server:  
```bash
STORAGE_PROVIDER=local
```
You will need to start a local server to serve these files and make sure that your `.env.local` file has this line:
```bash
LOCAL_STORAGE_PROVIDER="localhost:8642"
```
In a new terminal, go to `packages/server` and run
```bash
npm run serve-local-files
```
This will start up the `http-server` that will serve local files from `packages/server/upload` on `localhost:8642`.  
> Note: You may have to accept the invalid self-signed certificate in the browser the first time it is loaded. See the `Allow local file http-server connection with invalid certificate` section below.

## 6. Start the API server, two instanceservers, and client (if you did not run step 4a)
Open two/three separate terminals and run:
- Run `npm run dev` inside `packages/server`.  
  This will launch the API, world, media and file servers.  
  _Note: If you are not using instanceservers, you can instead run `npm run dev-api-server` inside the API server folder._
- Run `npm run dev` inside `packages/client`  
  _Note: If you are on windows you need to use `npm run dev-windows` instead of `npm run dev`._

## 7. Open the Engine
If everything went well, you can now open the engine by navigating to [this link](https://localhost:3000/location/default) in your browser.  

The database seeding process creates a default empty location called `default`, which can be accessed by opening `https://localhost:3000/location/default`.

## 8. Accept the Certificates
<!-- Start of partial: AcceptCertificates -->
When loading the engine's website for the first time you'll have to tell your browser to ignore insecure connections.  
1. Open the `Developer Tools` of your browser by clicking the side menu with three dots, then go to `More tools > Developer tools` (or use either `Ctrl+Shift+I` or `F12`) and then go to the `Console` tab.
2. You will see some errors in URL addresses starting with `wss`
    - Replace `wss` with `https` and open that URL in a new tab
    - Accept the certificate
    - Reload your iR Engine's tab
3. You will see some errors in URL addresses starting with `https://localhost:9000`
    - Open the URL linked in one of those errors
    - Accept the certificate
    - Reload your iR Engine's tab

You need to do this for the following domains:
- `wss://api-local.theinfinitereality.io` -> https://api-local.theinfinitereality.io
- `wss://instanceserver-local.theinfinitereality.io` -> https://instanceserver-local.theinfinitereality.io
- https://localhost:9000

> If the engine's website keeps displaying `loading routes` progress for a long time, it means that you have to allow the engine's certificates.  

Web browsers will throw warnings when navigating to pages with unknown certificates _(aka: insecure pages)_. You should be able to tell the browser to ignore these warnings by opening your browser's `advanced options`, but during development it is easier to just ignore the browser's warnings and accept the default certificates.  
> _Note: You will be able to create signed certificates to replace the default ones when you deploy your own iR Engine stack._

<!-- End of partial: AcceptCertificates -->

