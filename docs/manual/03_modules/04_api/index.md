# API documentation

This section explains how to document APIs in the iR Engine codebase. The iR Engine uses [Feathers.js](https://feathersjs.com/) and [feathers-swagger](https://github.com/feathersjs-ecosystem/feathers-swagger) to automatically generate OpenAPI documentation from service definitions and schema files.

The guides below will help you understand the architecture and provide practical steps for creating effective API documentation.

## Quick navigation

::::link-array
:::link-array-item{headerImage headerColor}
[API architecture](./01_api_architecture.md)&#x20;

Learn about the API documentation architecture, key components, and generation process.
:::

:::link-array-item{headerImage headerColor}
[Documenting endpoints](./02_documenting_endpoints.md)&#x20;

Step-by-step instructions for documenting API endpoints in the iR Engine codebase.
:::
::::

## Accessing the API documentation

The API documentation is served through Swagger UI at the `/openapi` endpoint:

- **Local development**: [https://localhost:3030/openapi](https://localhost:3030/openapi)
- **Development environment**: [https://api-ir-engine-mt-dev.theinfinitereality.io/openapi](https://api-ir-engine-mt-dev.theinfinitereality.io/openapi)

## API development workflow

The iR Engine uses Feathers.js for API development, which provides a standardized workflow for creating and documenting API endpoints:

1. **Create schema files** to define data structures and available methods
2. **Implement service logic** using hooks for before, after, and error handling
3. **Add validators and resolvers** for data validation and transformation
4. **Create documentation files** with detailed descriptions and examples
5. **Register the service** with the application

This workflow ensures consistency across all API endpoints and makes it easier for developers to understand and maintain the codebase.

## Additional resources

- [Feathers.js documentation](https://feathersjs.com/api/) - Official Feathers.js documentation
- [Feathers-swagger API documentation](https://feathersjs-ecosystem.github.io/feathers-swagger/#/api) - Complete reference for all available options
- [OpenAPI specification](https://swagger.io/specification/) - The official OpenAPI specification
- [Swagger UI](https://swagger.io/tools/swagger-ui/) - Documentation on the Swagger UI interface
