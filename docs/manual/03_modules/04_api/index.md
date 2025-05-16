# API documentation system

This section explains how to document APIs in the iR Engine codebase. It covers the API documentation system architecture, implementation guides, and best practices for creating and maintaining API documentation.

The iR Engine uses [Feathers.js](https://feathersjs.com/) and [feathers-swagger](https://github.com/feathersjs-ecosystem/feathers-swagger) to automatically generate OpenAPI documentation from service definitions and schema files.

## Quick navigation

::::link-array
:::link-array-item{headerImage headerColor}
[Documentation System](./01_documentationSystem.md)&#x20;

Learn about the API documentation architecture, key components, and generation process.
:::

:::link-array-item{headerImage headerColor}
[Documentation Guide](./02_documentationGuide.md)&#x20;

Step-by-step instructions for documenting API endpoints in the iR Engine codebase.
:::
::::

## Accessing the API documentation

The API documentation is served through Swagger UI at the `/openapi` endpoint:

- **Local development**: [https://localhost:3030/openapi](https://localhost:3030/openapi)
- **Development environment**: [https://api-ir-engine-mt-dev.theinfinitereality.io/openapi](https://api-ir-engine-mt-dev.theinfinitereality.io/openapi)

## Additional resources

- [Feathers-swagger API documentation](https://feathersjs-ecosystem.github.io/feathers-swagger/#/api) - Complete reference for all available options
- [OpenAPI Specification](https://swagger.io/specification/) - The official OpenAPI specification
- [Swagger UI](https://swagger.io/tools/swagger-ui/) - Documentation on the Swagger UI interface
