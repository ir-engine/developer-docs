# API Documentation System

This guide explains how the API documentation system works in the iR Engine codebase, including its architecture and key components.

## Overview

The iR Engine uses [feathers-swagger](https://github.com/feathersjs-ecosystem/feathers-swagger) to automatically generate OpenAPI documentation from service definitions and schema files. The documentation is served through Swagger UI at the `/openapi` endpoint. For a complete reference of all available options, see the [feathers-swagger API documentation](https://feathersjs-ecosystem.github.io/feathers-swagger/#/api).

## API documentation architecture

The API documentation system in iR Engine consists of several key components that work together to generate the OpenAPI documentation. This architecture allows for a declarative approach to API documentation, where the documentation is generated automatically from the code rather than maintained separately.

## Key components

1. **Schema files** (`packages/common/src/schemas/[category]/[name].schema.ts`):
   - Define data structures, available methods, and validation rules
   - Example: `packages/common/src/schemas/cluster/build-status.schema.ts`
   - Contains path definitions, method lists, and data schemas

2. **Documentation files** (`packages/server-core/src/[category]/[name]/[name].docs.ts`):
   - Provide additional documentation details like descriptions, examples, and parameter information
   - Example: `packages/server-core/src/cluster/build-status/build-status.docs.ts`
   - Use `createSwaggerServiceOptions()` to define documentation options

3. **Service registration** (`packages/server-core/src/[category]/[name]/[name].ts`):
   - Connect schemas and documentation to services
   - Example: `packages/server-core/src/cluster/build-status/build-status.ts`
   - Include documentation when registering the service with `app.use()`

4. **OpenAPI configuration** (`packages/server-core/src/createApp.ts`):
   - Set up the Swagger UI and define global OpenAPI settings
   - Configures the `/openapi` endpoint that serves the documentation

## Documentation generation process

The OpenAPI documentation in iR Engine is generated through the following process:

1. **Schema definition**: Each service has a schema file that defines its data structure and available methods
2. **Documentation enhancement**: Each service also has a documentation file that provides additional details
3. **Service registration**: When a service is registered, it includes its documentation
4. **Automatic generation**: The `feathers-swagger` package automatically generates the OpenAPI documentation based on these components
5. **Documentation serving**: The documentation is served at the `/openapi` endpoint (`localhost:3030/openapi` in your local deployment)

This process ensures that the API documentation stays in sync with the actual implementation, as it's generated directly from the code.

## OpenAPI configuration

The global OpenAPI configuration is set up in `packages/server-core/src/createApp.ts`. This is where you can configure the Swagger UI and define global settings for your API documentation:

```tsx
export const configureOpenAPI = () => (app: Application) => {
  app.configure(
    swagger({
      ui: swagger.swaggerUI({
        docsPath: '/openapi'
      }),
      specs: {
        info: {
          title: 'Infinite Reality Engine API Surface',
          description: 'APIs for the Infinite Reality Engine application',
          version: packagejson.version
        },
        schemes: ['https'],
        components: {
          securitySchemes: {
            BearerAuth: {
              type: 'http',
              scheme: 'bearer'
            }
          }
        },
        security: [{ BearerAuth: [] }]
      },
      idType: 'string',
      ignore: {
        paths: ['oauth', 'knex_migrations']
      }
    })
  )
  return app
}
```

For more information on configuring the OpenAPI documentation, see the [feathers-swagger documentation on swaggerOptions](https://feathersjs-ecosystem.github.io/feathers-swagger/#/api?id=swaggeroptions).

## Additional resources

- [Feathers-swagger API documentation](https://feathersjs-ecosystem.github.io/feathers-swagger/#/api) - Complete reference for all available options
- [OpenAPI Specification](https://swagger.io/specification/) - The official OpenAPI specification
- [Swagger UI](https://swagger.io/tools/swagger-ui/) - Documentation on the Swagger UI interface
- [API Documentation Guide](./02_documentationGuide.md) - Step-by-step guide for documenting API endpoints
