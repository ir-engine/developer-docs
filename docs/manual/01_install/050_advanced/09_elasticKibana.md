<!-- import AcceptCertificates from '../../_partials/acceptCertificates.md' -->

# Setup Elastic Search & Kibana

Elastic Search and Kibana will be automatically launched with `npm run dev` and will be running on `localhost` ports `9200` & `5601` respectively. This will automatically set up and run Redis/MariaDB docker containers, and iR Engine client/server/instance-server instances.

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
