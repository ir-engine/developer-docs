When accessing the iR Engine for the first time, browsers block access due to **self-signed certificates**. This prevents you from accessing the Admin panel and the Editor. To bypass this, manually accept the certificates:

#### 1. Open Developer Tools

- **Chrome/Edge:** Click the three-dot menu → *More tools* → *Developer tools*
- **Shortcut:** Press `Ctrl+Shift+I` or `F12`
- Navigate to the **Console** tab.

#### 2. Identify certificate-related errors

Check for network request errors related to:

- **WebSocket connections** (`wss://` URLs)
- **HTTPS requests to localhost**

The following addresses require certificate approval:

- `https://localhost:3030` – API server
- `https://localhost:8642` – File server

#### 3. Bypass the security warning

1. Open these URLs directly in your browser:
    - [https://localhost:3030](https://localhost:3030/)
    - [https://localhost:8642](https://localhost:8642/)
2. A **"Your connection is not private"** warning appears.
3. Click **Advanced** → **Proceed to localhost (unsafe)**.
4. Reload the engine’s website.

:::hint{type="success"}
Once completed, the iR Engine’s admin panel and editor will be fully accessible. 🚀
:::