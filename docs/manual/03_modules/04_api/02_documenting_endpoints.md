# Documenting endpoints

This guide provides step-by-step instructions for documenting API endpoints in the iR Engine codebase.

## Introduction

For an overview of how the API documentation system works, see the [API architecture](./01_api_architecture.md) guide.

### Why good documentation matters

While feathers-swagger automatically generates basic API documentation, the default output contains only generic placeholders like "Creates a new resource with data" that provide little practical value.

**Well-documented APIs are critical for developer experience.** Custom descriptions, examples, and parameter details transform generic documentation into a valuable resource that helps developers understand and use your API effectively.

### Generic vs. custom documentation example

#### Generic (auto-generated):
```json
{
  "description": "Authentication service",
  "operations": {
    "create": {
      "description": "Creates a new resource with data"
    },
    "remove": {
      "description": "Removes a resource with id from the service"
    }
  }
}
```

#### Improved documentation:
```json
{
  "description": "Authentication service for user login, token validation, and logout",
  "operations": {
    "create": {
      "description": "Authenticates a user with credentials and returns a JWT token",
      "requestBody": {
        "content": {
          "application/json": {
            "example": {
              "strategy": "local",
              "email": "user@example.com",
              "password": "password123"
            }
          }
        }
      }
    }
  }
}
```

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

This is an important step in creating useful API documentation. Without custom descriptions, your API documentation will only contain generic placeholders that provide little value to API consumers.

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
    description: 'Build status service description',  // Generic description
    securities: ['all']
  }
})
```

To enhance the documentation, update the `docs` object with more detailed descriptions and parameter information. Replace generic descriptions with meaningful, context-specific information:

```tsx
export default createSwaggerServiceOptions({
  schemas: {
    buildStatusDataSchema,
    buildStatusPatchSchema,
    buildStatusQuerySchema,
    buildStatusSchema
  },
  docs: {
    description: 'Service for tracking and managing the status of builds in the system',  // Specific, descriptive
    securities: ['all'],
    operations: {
      find: {
        description: 'Retrieves a list of build statuses based on query parameters',  // Better than generic "Retrieves a list of all resources"
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
        description: 'Retrieves a single build status record by ID'  // Specific to this resource
      },
      create: {
        description: 'Creates a new build status record to track a build process'  // Explains purpose, not just action
      },
      patch: {
        description: 'Updates an existing build status record, typically used to update status or add logs'  // Explains when/why to use
      },
      remove: {
        description: 'Deletes a build status record when it is no longer needed'  // Provides context
      }
    }
  }
})
```

### Step 4: Add examples and response documentation

For more comprehensive documentation, add examples of request and response data. Examples help API consumers understand how to use your API correctly. Continuing with our `build-status` example:

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

### Step 6: Test your documentation

After updating the documentation:

1. Start the server with `npm run dev`
2. Navigate to `https://localhost:3030/openapi` in your browser
3. Find your service in the UI
4. Verify that all descriptions, parameters, and examples are correct
5. Try out the API using the "Try it out" feature

Note that changes to the OpenAPI documentation require a server restart to be visible in the Swagger UI, as Feathers needs to rebuild the OpenAPI specification with your changes.

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

## Special case example: Authentication service

The authentication service demonstrates how to handle custom parameter names:

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

This example shows:
- Custom parameter naming with `idNames`
- Schema definition directly in the docs object
- Reference mapping with `refs`
- Clear operation descriptions

## Documentation organization

The folder structure in the codebase provides a natural way to organize API endpoints. Services are grouped by category in the `packages/server-core/src/` directory, which should be reflected in your documentation.

When documenting APIs, consider how they relate to each other based on their location in the folder structure. Services in the same category often serve related purposes and may be documented together for better context.

## Best practices

1. **Be specific and contextual** - Replace generic descriptions with meaningful, context-specific information
2. **Include examples** - Provide request and response examples for all operations
3. **Document parameters thoroughly** - Explain all parameters with clear descriptions
4. **Include error responses** - Document possible error cases with examples
5. **Use consistent terminology** - Be consistent in your naming and formatting
6. **Use sentence case** - For all headings and descriptions
7. **Be concise** - Use clear, simple language that's easy to understand
8. **Explain the "why"** - Describe the purpose and use cases, not just the mechanics
9. **Document edge cases** - Include limitations and special considerations
10. **Keep it updated** - Maintain documentation when the API changes
11. **Think like a user** - Consider what information would be most helpful to API consumers

## Additional resources

- [API architecture](./01_api_architecture.md) - Overview of the API documentation architecture
- [Feathers.js documentation](https://feathersjs.com/api/) - Official Feathers.js documentation
- [Feathers-swagger API documentation](https://feathersjs-ecosystem.github.io/feathers-swagger/#/api) - Complete reference for all available options
- [OpenAPI specification](https://swagger.io/specification/) - The official OpenAPI specification
- [Swagger UI](https://swagger.io/tools/swagger-ui/) - Documentation on the Swagger UI interface