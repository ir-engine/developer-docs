# API documentation guide

This guide provides step-by-step instructions for documenting API endpoints in the iR Engine codebase.

## Introduction

This guide shows you how to document API endpoints in the iR Engine codebase. For an overview of how the API documentation system works, see the [Documentation System](./01_documentationSystem.md) guide.

## Documenting an API endpoint

Follow these steps to document a new API endpoint or improve documentation for an existing one:

### Step 1: Understand the schema files

Schema files define the data structure and available methods for a service. They are located in `packages/common/src/schemas/`.

Let's look at a complete example from `packages/common/src/schemas/cluster/build-status.schema.ts`:

```tsx
// Path definition - This becomes the API endpoint path
export const buildStatusPath = 'build-status'

// Methods definition - These determine which HTTP endpoints are available
// ['find', 'get', 'create', 'patch', 'remove'] maps to:
// GET /build-status (find - list all)
// GET /build-status/{id} (get - get one by id)
// POST /build-status (create - create new)
// PATCH /build-status/{id} (patch - update)
// DELETE /build-status/{id} (remove - delete)
export const buildStatusMethods = ['find', 'get', 'create', 'patch', 'remove'] as const

// Main data model schema
export const buildStatusSchema = Type.Object(
  {
    id: Type.Integer(),
    status: Type.String(),
    dateStarted: Type.String(),
    dateEnded: Type.String(),
    logs: Type.String(),
    commitSHA: Type.String(),
    createdAt: Type.String({ format: 'date-time' }),
    updatedAt: Type.String({ format: 'date-time' })
  },
  { $id: 'BuildStatus', additionalProperties: false }
)
```

Key elements in schema files:

1. **Path definition**:
   - `export const buildStatusPath = 'build-status'`
   - This defines the API endpoint path (`/build-status`)

2. **Methods definition**:
   - `export const buildStatusMethods = ['find', 'get', 'create', 'patch', 'remove'] as const`
   - This defines which HTTP methods are available for the endpoint
   - Each method maps to a specific HTTP operation:
     - `find` → `GET /build-status` (list all)
     - `get` → `GET /build-status/{id}` (get one by id)
     - `create` → `POST /build-status` (create new)
     - `patch` → `PATCH /build-status/{id}` (update)
     - `remove` → `DELETE /build-status/{id}` (delete)

3. **Schema definitions**:
   - Main schema (`buildStatusSchema`): Defines the complete data structure
   - Data schema (`buildStatusDataSchema`): Defines fields for creating new entries
   - Patch schema (`buildStatusPatchSchema`): Defines fields for updating entries
   - Query schema (`buildStatusQuerySchema`): Defines available query parameters

### Step 2: Enhance schema definitions with descriptions

To improve documentation, add descriptions to schema properties. Continuing with our `build-status` example:

```tsx
// Main data model schema with added descriptions
export const buildStatusSchema = Type.Object(
  {
    id: Type.Integer({
      description: 'Unique identifier for the build status record'
    }),
    status: Type.String({
      description: 'Current status of the build (e.g., "pending", "in_progress", "completed", "failed")'
    }),
    dateStarted: Type.String({
      description: 'Date and time when the build started'
    }),
    dateEnded: Type.String({
      description: 'Date and time when the build completed or failed'
    }),
    logs: Type.String({
      description: 'Build process logs'
    }),
    commitSHA: Type.String({
      description: 'Git commit SHA that triggered the build'
    }),
    createdAt: Type.String({
      format: 'date-time',
      description: 'When the build status record was created'
    }),
    updatedAt: Type.String({
      format: 'date-time',
      description: 'When the build status record was last updated'
    })
  },
  { $id: 'BuildStatus', additionalProperties: false }
)
```

### Step 3: Create or update the documentation file

Each service has a documentation file that provides additional details. These files are located in `packages/server-core/src/[category]/[name]/[name].docs.ts`.

Continuing with our `build-status` example, let's look at `packages/server-core/src/cluster/build-status/build-status.docs.ts`:

```tsx
import { createSwaggerServiceOptions } from 'feathers-swagger'
import {
  buildStatusDataSchema,
  buildStatusPatchSchema,
  buildStatusQuerySchema,
  buildStatusSchema
} from '@ir-engine/common/src/schemas/cluster/build-status.schema'

export default createSwaggerServiceOptions({
  schemas: {
    buildStatusDataSchema,
    buildStatusPatchSchema,
    buildStatusQuerySchema,
    buildStatusSchema
  },
  docs: {
    description: 'Build status service description',
    securities: ['all']
  }
})
```

To enhance the documentation, update the `docs` object with more detailed descriptions and parameter information:

```tsx
export default createSwaggerServiceOptions({
  schemas: {
    buildStatusDataSchema,
    buildStatusPatchSchema,
    buildStatusQuerySchema,
    buildStatusSchema
  },
  docs: {
    description: 'Service for tracking and managing the status of builds in the system',
    securities: ['all'],
    operations: {
      find: {
        description: 'Retrieves a list of build statuses based on query parameters',
        parameters: [
          {
            in: 'query',
            name: 'status',
            description: 'Filter builds by status (e.g., "pending", "in_progress", "completed", "failed")',
            type: 'string'
          },
          {
            in: 'query',
            name: 'commitSHA',
            description: 'Filter builds by commit SHA',
            type: 'string'
          }
        ]
      },
      get: {
        description: 'Retrieves a single build status record by ID'
      },
      create: {
        description: 'Creates a new build status record'
      },
      patch: {
        description: 'Updates an existing build status record'
      },
      remove: {
        description: 'Deletes a build status record'
      }
    }
  }
})
```

For a complete reference of all available options in the documentation file, see the [feathers-swagger documentation on serviceDocs](https://feathersjs-ecosystem.github.io/feathers-swagger/#/api?id=servicedocs).

### Step 4: Add examples and response documentation

For more comprehensive documentation, add examples of request and response data. Continuing with our `build-status` example:

```tsx
export default createSwaggerServiceOptions({
  schemas: {
    buildStatusDataSchema,
    buildStatusPatchSchema,
    buildStatusQuerySchema,
    buildStatusSchema
  },
  docs: {
    description: 'Service for tracking and managing the status of builds in the system',
    securities: ['all'],
    operations: {
      find: {
        description: 'Retrieves a list of build statuses based on query parameters',
        parameters: [
          {
            in: 'query',
            name: 'status',
            description: 'Filter builds by status (e.g., "pending", "in_progress", "completed", "failed")',
            type: 'string'
          },
          {
            in: 'query',
            name: 'commitSHA',
            description: 'Filter builds by commit SHA',
            type: 'string'
          }
        ],
        responses: {
          '200': {
            description: 'Successfully retrieved build statuses',
            content: {
              'application/json': {
                example: {
                  total: 2,
                  limit: 10,
                  skip: 0,
                  data: [
                    {
                      id: 1,
                      status: 'completed',
                      dateStarted: '2023-04-01T10:00:00Z',
                      dateEnded: '2023-04-01T10:15:00Z',
                      logs: 'Build completed successfully',
                      commitSHA: '8f4b3a1c5d6e7b2a9c0d1e2f3a4b5c6d7e8f9a0b',
                      createdAt: '2023-04-01T10:00:00Z',
                      updatedAt: '2023-04-01T10:15:00Z'
                    },
                    {
                      id: 2,
                      status: 'in_progress',
                      dateStarted: '2023-04-01T11:00:00Z',
                      dateEnded: null,
                      logs: 'Building...',
                      commitSHA: '7e8f9a0b8f4b3a1c5d6e7b2a9c0d1e2f3a4b5c6d',
                      createdAt: '2023-04-01T11:00:00Z',
                      updatedAt: '2023-04-01T11:00:00Z'
                    }
                  ]
                }
              }
            }
          }
        }
      },
      create: {
        description: 'Creates a new build status record',
        requestBody: {
          description: 'Data for the new build status',
          content: {
            'application/json': {
              example: {
                status: 'pending',
                dateStarted: '2023-04-01T12:00:00Z',
                commitSHA: '5d6e7b2a9c0d1e2f3a4b5c6d7e8f9a0b8f4b3a1c'
              }
            }
          }
        },
        responses: {
          '201': {
            description: 'Successfully created build status',
            content: {
              'application/json': {
                example: {
                  id: 3,
                  status: 'pending',
                  dateStarted: '2023-04-01T12:00:00Z',
                  dateEnded: null,
                  logs: '',
                  commitSHA: '5d6e7b2a9c0d1e2f3a4b5c6d7e8f9a0b8f4b3a1c',
                  createdAt: '2023-04-01T12:00:00Z',
                  updatedAt: '2023-04-01T12:00:00Z'
                }
              }
            }
          },
          '400': {
            description: 'Invalid data provided',
            content: {
              'application/json': {
                example: {
                  name: 'BadRequest',
                  message: 'Invalid data',
                  code: 400,
                  errors: [
                    { path: 'status', message: 'Status is required' },
                    { path: 'commitSHA', message: 'Commit SHA is required' }
                  ]
                }
              }
            }
          }
        }
      }
    }
  }
})
```

### Step 5: Register the service with documentation

Finally, make sure the documentation is included when registering the service:

```tsx
// In packages/server-core/src/cluster/build-status/build-status.ts
import { buildStatusMethods, buildStatusPath } from '@ir-engine/common/src/schemas/cluster/build-status.schema'
import { Application } from '../../../declarations'
import { BuildStatusService } from './build-status.class'
import buildStatusDocs from './build-status.docs'
import hooks from './build-status.hooks'

export default (app: Application): void => {
  const options = {
    name: buildStatusPath,
    paginate: app.get('paginate'),
    Model: app.get('knexClient'),
    multi: true
  }

  app.use(buildStatusPath, new BuildStatusService(options), {
    // A list of all methods this service exposes externally
    methods: buildStatusMethods,
    // You can add additional custom events to be sent to clients here
    events: [],
    docs: buildStatusDocs  // Include the documentation
  })

  const service = app.service(buildStatusPath)
  service.hooks(hooks)
}
```

## Special cases and advanced options

### Custom parameter names

For endpoints like `DELETE /authentication/{accessToken}` where the parameter name isn't the default `id`, use the `idNames` property. This is an object with path parameter names to customize the idName on operation/method level:

```tsx
// In packages/server-core/src/user/authentication.doc.ts
export default createSwaggerServiceOptions({
  schemas: {},
  docs: {
    description: 'Authentication service for user login and logout',
    idNames: {
      remove: 'accessToken'  // This defines the parameter name for DELETE
    },
    idType: 'string',
    securities: ['remove'],
    // ... other options
  }
})
```

For more details on customizing parameter names, see the [feathers-swagger documentation on idNames](https://feathersjs-ecosystem.github.io/feathers-swagger/#/api?id=servicedocs).

### Custom schemas

For services without standard schemas, define them directly in the documentation file:

```tsx
// In packages/server-core/src/cluster/logs-api/logs-api.docs.ts
export default createSwaggerServiceOptions({
  schemas: {},
  docs: {
    description: 'Service for logging API events',
    securities: ['all'],
    definitions: {
      ['logs-api']: {
        type: 'object',
        properties: {
          msg: {
            type: 'string',
            description: 'Log message'
          },
          level: {
            type: 'string',
            description: 'Log level (info, warn, error)'
          }
        },
        additionalProperties: { type: 'string' }
      }
    }
  }
})
```

For more information on custom schemas and other documentation options, see the [feathers-swagger documentation on serviceDocs](https://feathersjs-ecosystem.github.io/feathers-swagger/#/api?id=servicedocs).

## Complete examples

This section provides complete, real-world examples of API documentation in the iR Engine codebase. These examples demonstrate how to handle special cases and can be used as templates for your own documentation.

### Example: Authentication service (special case)

The authentication service is a special case because it uses custom parameter names:

```tsx
// In packages/server-core/src/user/authentication.doc.ts
export default createSwaggerServiceOptions({
  schemas: {},
  docs: {
    description: 'Authentication service for user login and logout',
    idNames: {
      remove: 'accessToken'  // This defines the parameter name for DELETE
    },
    idType: 'string',
    securities: ['remove'],
    schemas: {
      authRequest: {
        type: 'object',
        properties: {
          strategy: {
            type: 'string',
            default: 'jwt',
            description: 'Authentication strategy to use'
          },
          accessToken: {
            type: 'string',
            description: 'JWT access token for authentication'
          }
        }
      }
    },
    refs: {
      createRequest: 'authRequest',
      removeRequest: 'authRequest',
      createResponse: 'authResult',
      removeResponse: 'authResult'
    },
    operations: {
      create: {
        description: 'Authenticates a user and returns an access token'
      },
      remove: {
        description: 'Logs out a user by invalidating their access token'
      }
    }
  }
})
```

## Testing your documentation

After updating the documentation:

1. Start the server with `npm run dev`
2. Navigate to `https://localhost:3030/openapi` in your browser
3. Find your service in the UI
4. Verify that all descriptions, parameters, and examples are correct
5. Try out the API using the "Try it out" feature

Note that changes to the OpenAPI documentation require a server restart to be visible in the Swagger UI, as Feathers needs to rebuild the OpenAPI specification with your changes.

## Best practices

1. **Be consistent** in your terminology and formatting
2. **Use sentence case** for all headings and descriptions
3. **Use clear, concise language** that's easy to understand
4. **Include examples** for complex operations
5. **Document all parameters** with clear descriptions
6. **Include error responses** with helpful error messages
7. **Keep documentation up-to-date** when the API changes
8. **Think from the API consumer's perspective** - what would they need to know?

## Additional resources

- [API Documentation System](./01_documentationSystem.md) - Overview of the API documentation system
- [Feathers-swagger API documentation](https://feathersjs-ecosystem.github.io/feathers-swagger/#/api) - Complete reference for all available options
- [OpenAPI Specification](https://swagger.io/specification/) - The official OpenAPI specification
- [Swagger UI](https://swagger.io/tools/swagger-ui/) - Documentation on the Swagger UI interface
