# Projects

This guide explains the project structure, configuration, and key functionalities.

***

## Overview

Projects in iR Engine are modular, **Git-based repositories** containing **custom code, assets, and scenes**. They enable developers to create, modify, and manage their own features, scenes, and content. Each project can be installed, updated, or removed independently, making it easy to **extend and customize** the engine.&#x20;

Projects are stored in the `/packages/projects/` directory and can be managed in both **production** and **local development** environments.

### Project management by environment

The way projects are managed differs between **production** and **local development** environments.

| **Environment**       | **Project Management**                                                                                                                       |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| **Production**        | Projects are installed based on the `projects` database table, and assets are downloaded from a **storage provider**.                        |
| **Local development** | The **local file system** is the source of truth. Any project folders added or removed are **automatically synchronized** with the database. |

By default, only the **default-project** is installed. In production environments, it is **read-only** and is located at:

```text
/packages/projects/default-project/
```

Each project is also a **Git repository**, allowing for version control and seamless collaboration.

***

## Project structure

Projects follow a **standardized folder structure** to ensure consistency and maintainability.

```text
/packages/projects/[github-org]/[your-project]/
│── assets/                # Uploaded files
│── src/                   # Source code for custom logic and components
│── tests/                 # Test files for automated testing
│── [sceneName].scene.json # Scene configuration file
│── [sceneName].thumbnail.png # Auto-generated scene preview
│── xrengine.config.ts     # Project configuration file
│── package.json           # Project metadata and dependencies
```

:::image{src="https://archbee-doc-uploads.s3.amazonaws.com/_ccd8qducXixEhn6az5xD/cOzkgVLoHf89Bqr087Jye_projects-folder.png" signedSrc="https://archbee-doc-uploads.s3.amazonaws.com/_ccd8qducXixEhn6az5xD/cOzkgVLoHf89Bqr087Jye_projects-folder.png" size="28" width="263" height="241" position="center" caption alt}

:::

### Key directories and files

Before diving into project configuration, let’s break down the essential directories and files inside a project.

| **Path**                    | **Description**                                            |
| :-------------------------- | :--------------------------------------------------------- |
| `assets/`                   | Stores **uploaded files** from the editor.                 |
| `src/`                      | Contains **source code** for project logic.                |
| `tests/`                    | Includes **test files** for validation.                    |
| `[sceneName].scene.json`    | Defines **scene data** and object positions.               |
| `[sceneName].thumbnail.png` | Stores an auto-generated **preview image** of a scene.     |
| `xrengine.config.ts`        | The **main project configuration file**.                   |
| `package.json`              | Defines **dependencies and compatibility** with iR Engine. |

### Code organization

To maintain optimal performance and efficient code-splitting, projects should follow these best practices:

- **Scene-related systems** must be stored in `/src/systems/` and **end with** `System.ts`.
  - This ensures that **Vite’s bundling process** properly handles dynamic imports.
- Dependencies from `@ir-engine/*` are **symlinked** and do not need to be explicitly listed.
  - However, **package managers like pnpm** may require them in `peerDependencies`.

***

## Project configuration (`xrengine.config.ts`)

The `xrengine.config.ts` file defines how a project interacts with the engine. It allows customization of **routes, services, database settings, and world behavior**.

### Configuration interface

Below is the structure of the configuration file:

```typescript
export interface ProjectConfigInterface {
  onEvent?: string
  thumbnail?: string
  routes?: {
    [route: string]: {
      component: () => Promise<{ default: (props: any) => JSX.Element }>
      props?: {
        [x: string]: any
        exact?: boolean
      }
    }
  }
  webappInjection?: () => Promise<{ default: (props: any) => void | JSX.Element }>
  worldInjection?: () => Promise<{ default: () => Promise<void> }>
  services?: string
  databaseSeed?: string
  settings?: Array<ProjectSettingSchema>
}
```

***

## Configuration properties

Each property inside `xrengine.config.ts` defines specific behaviors for the project.

### Event hooks (`onEvent`)

The `onEvent` property specifies a **relative path** to a file that defines project lifecycle hooks. These hooks allow developers to execute **custom logic** when a project is installed, updated, or removed.

```tsx
export interface ProjectEventHooks {
  onInstall?: (app: Application) => Promise<any>
  onLoad?: (app: Application) => Promise<any>
  onUpdate?: (app: Application) => Promise<any>
  onUninstall?: (app: Application) => Promise<any>
  onOEmbedRequest?: (app: Application, url: URL, currentOEmbed: OEmbed) => Promise<OEmbed | null>
}
```

| **Hook**          | **Trigger**                                                   |
| :---------------- | :------------------------------------------------------------ |
| `onInstall`       | When the project is **installed**.                            |
| `onLoad`          | When the project is **loaded**.                               |
| `onUpdate`        | When the project is **updated** (e.g., after saving a scene). |
| `onUninstall`     | When the project is **removed**.                              |
| `onOEmbedRequest` | When an **oEmbed preview** is requested for a project URL.    |

The **default iR Engine project** uses `onInstall` to install default avatars. You can find this implementation at:

```text
/packages/projects/default-project/projectEventHooks.ts
```

🔗 <a href="https://github.com/ir-engine/ir-engine/blob/dev/packages/projects/default-project/projectEventHooks.ts" target="_blank">Link to the file.</a>&#x20;

### Thumbnail (`thumbnail`)

The `thumbnail` property is used to specify a **URL to an image**, which will be displayed as the **project’s Studio thumbnail**.

Example:

```tsx
thumbnail: "/static/thumbnail.jpg"
```

***

### Custom routes (`routes`)

The `routes` property enables projects to define **custom web routes**, dynamically loading React components.

```typescript
routes: {
  '/': {
    component: () => import('@ir-engine/client/src/pages/index'),
    props: {
      exact: true
    }
  },
  '/admin': {
    component: () => import('@ir-engine/client/src/pages/admin')
  },
  '/location': {
    component: () => import('@ir-engine/client/src/pages/location/location')
  },
  '/studio': {
    component: () => import('@ir-engine/client/src/pages/editor')
  },
  '/room': {
    component: () => import('@ir-engine/client/src/pages/room')
  },
  '/capture': {
    component: () => import('@ir-engine/client/src/pages/capture')
  },
  '/chat': {
    component: () => import('@ir-engine/client/src/pages/chat/chat')
  }
}
```

| **Key**        | **Description**                                       |
| :------------- | :---------------------------------------------------- |
| **Route path** | The **URL path** for the route (must start with `/`). |
| **Component**  | A **React component** dynamically loaded on demand.   |

***

### Webapp injection (`webappInjection`)

The `webappInjection` property runs **before web routes are loaded**, allowing projects to initialize logic globally.

```typescript
**webappInjection: () => import('./webappInjection')**
```

***

### World injection (`worldInjection`)

The `worldInjection` property allows logic to be run every time a new world is created. This logic is loaded on all instances of the engine, such as a location and the editor.

An example use case of this property would be registering custom scene loader and editor prefabs.

```typescript
worldInjection: () => import('./src/Hello')
```

***

### Services (`services`)

The `services` property defines **Feathers.js services** for APIs and game logic.

It is a relative path that points to a file which must return the type `((app: Application) => Promise<any>)[]`. This return type will be run on all instance servers and api servers at startup.

```typescript
services: './services/services.ts'
```

***

### Database seeding (`databaseSeed`)

The `databaseSeed` property points to a **database seed file** for initial data population.

```typescript
databaseSeed: './services/seeder-config.ts'
```

***

## Internationalization (i18n)

Projects can support **multiple languages** using **i18n files** located in `/i18n/[language]/[namespace].json`.

Example structure:

```text
/i18n/en/admin.json
/i18n/fr/admin.json
```

You can find example i18n files in the [iR Engine i18n repository](https://github.com/ir-engine/ir-engine/tree/dev/packages/client-core/i18n).
