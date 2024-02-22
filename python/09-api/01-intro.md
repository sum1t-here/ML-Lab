# API - Application Programming interface

Use-case:

- Interoperability
- Reusability
- Security
- Scalablity

Types:

- Web Api (Restful api)
- Library Api (Tensorflow)
- HardWare Api (Api that can access camera and all)

# WEB API vs API

## API (Application Programming Interface)

### Definition

- **API (Application Programming Interface)** is a set of rules and protocols that allow different software applications to communicate with each other.
- It defines the methods and data formats that developers can use to interact with the software component.

### Characteristics

- **Internal or External:** APIs can be internal (used within an organization) or external (exposed to third-party developers).
- **Functionality:** APIs provide access to specific functionalities or services of a software system.
- **Language Agnostic:** APIs are often language-agnostic, meaning they can be used with different programming languages.
- **Examples:** Database APIs (like JDBC for Java), operating system APIs, library APIs (like jQuery for JavaScript), etc.

## Web API

### Definition

- **Web API (Web Application Programming Interface)** is a type of API that is accessed or consumed over the internet using HTTP/HTTPS protocols.
- It provides interoperability between different software applications running on different platforms or devices.

### Characteristics

- **Internet-Based:** Web APIs are accessed over the internet, making them accessible from anywhere with an internet connection.
- **Use of HTTP/HTTPS:** Web APIs use HTTP or HTTPS protocols for communication, making them platform-independent and language-agnostic.
- **Standardized Formats:** Web APIs often use standardized data formats such as JSON (JavaScript Object Notation) or XML (eXtensible Markup Language) for data exchange.
- **Examples:** RESTful APIs, SOAP APIs, GraphQL APIs, etc.

## Key Differences

1. **Access Method:**

   - **API:** Can be accessed locally or remotely, typically through function calls or library imports.
   - **Web API:** Accessed over the internet using HTTP/HTTPS protocols, usually through URLs.

2. **Protocol:**

   - **API:** Can use various protocols, including proprietary protocols specific to the software or platform.
   - **Web API:** Uses HTTP/HTTPS protocols for communication, ensuring interoperability across different platforms.

3. **Data Format:**

   - **API:** Data exchange format can vary depending on the software or platform, often relying on binary formats.
   - **Web API:** Uses standardized data formats like JSON or XML, promoting interoperability and ease of integration.

4. **Usage Scope:**
   - **API:** Can be used for internal integration within an organization or for third-party integration.
   - **Web API:** Primarily used for external integration, allowing third-party developers to access services or functionalities over the internet.

# REST vs SOAP Architecture

## REST (Representational State Transfer)

### Definition

- **REST (Representational State Transfer)** is an architectural style for designing networked applications.
- It emphasizes simplicity, scalability, and modifiability of components, making it ideal for distributed systems and web services.

### Characteristics

- **Stateless Communication:** RESTful services are stateless, meaning each request from a client to the server contains all the information necessary to understand and process the request.
- **Resource-Oriented:** REST uses resources (identified by URIs) and standard HTTP methods (GET, POST, PUT, DELETE) to manipulate the state of these resources.
- **Lightweight:** RESTful services use lightweight data formats like JSON or XML for data exchange, making them efficient and easy to implement.
- **Uniform Interface:** REST relies on a uniform interface between components, promoting simplicity and decoupling of client and server implementations.

## SOAP (Simple Object Access Protocol)

### Definition

- **SOAP (Simple Object Access Protocol)** is a protocol for exchanging structured information in the implementation of web services.
- It uses XML for message formatting and relies on additional standards like WSDL (Web Services Description Language) and UDDI (Universal Description, Discovery, and Integration) for service description and discovery.

### Characteristics

- **XML-Based:** SOAP messages are formatted using XML, which provides a standardized way to structure and exchange data.
- **Protocol-Heavy:** SOAP relies on a comprehensive set of protocols and standards, including XML, WSDL, and SOAP itself, which can result in more complex and verbose implementations.
- **Stateful Communication:** SOAP supports stateful communication through features like sessions and transactions, which can be useful for certain types of applications.
- **Strict Contract:** SOAP services define a strict contract between the client and server using WSDL, specifying the operations, message format, and communication protocols.

## Key Differences

1. **Communication Style:**

   - **REST:** Uses stateless communication over HTTP, focusing on resources and standard methods.
   - **SOAP:** Relies on XML-based messages exchanged over various protocols, including HTTP, SMTP, and others.

2. **Message Format:**

   - **REST:** Typically uses lightweight data formats like JSON or XML for message exchange.
   - **SOAP:** Uses XML for message formatting, which can result in larger message sizes and more overhead.

3. **Flexibility and Simplicity:**

   - **REST:** Emphasizes simplicity and flexibility, making it easier to implement and integrate with other systems.
   - **SOAP:** Provides a comprehensive set of features and standards, which can offer more functionality but also adds complexity.

4. **Statelessness:**
   - **REST:** Stateless communication simplifies server-side implementation and scaling, as each request contains all necessary information.
   - **SOAP:** Supports stateful communication through features like sessions and transactions, which can be beneficial for certain use cases but adds complexity.

# RESTful API

## Definition

RESTful API (Representational State Transfer API) is an architectural style for designing networked applications. It is based on the principles of REST, emphasizing simplicity, scalability, and modifiability of components.

## Characteristics

### 1. Stateless Communication

RESTful APIs are stateless, meaning each request from a client to the server contains all the information necessary to understand and process the request. The server does not store any client context between requests.

### 2. Resource-Oriented

RESTful APIs use resources, identified by URIs (Uniform Resource Identifiers), to represent entities or data. These resources are manipulated using standard HTTP methods such as GET, POST, PUT, DELETE, and PATCH.

### 3. Uniform Interface

RESTful APIs have a uniform interface between components, promoting simplicity and decoupling of client and server implementations. This interface typically includes standard HTTP methods, resource identifiers (URIs), representation formats (JSON, XML), and hypermedia links (HATEOAS).

### 4. Lightweight Data Formats

RESTful APIs use lightweight data formats like JSON (JavaScript Object Notation) or XML (eXtensible Markup Language) for data exchange. These formats are platform-independent, easy to parse, and human-readable.

### 5. Statelessness

Stateless communication simplifies server-side implementation and scaling, as each request contains all necessary information. Servers do not need to maintain client state between requests, improving reliability and scalability.

### 6. Cacheability

RESTful APIs leverage the HTTP protocol's built-in caching mechanisms to improve performance and scalability. Responses can be cached at various levels (client, intermediary, server) to reduce latency and bandwidth usage.

## Principles

### 1. Client-Server Separation

RESTful APIs enforce a clear separation of concerns between clients and servers, allowing them to evolve independently. Clients are not concerned with the internal implementation of servers, and servers are not concerned with the state of clients.

### 2. Layered System

RESTful APIs are built on a layered architecture, where each component (client, server, intermediary) interacts only with adjacent layers. This separation of concerns promotes scalability, reliability, and interoperability.

### 3. Uniform Interface

The uniform interface of RESTful APIs promotes simplicity, consistency, and reusability. It includes standard HTTP methods, resource identifiers (URIs), representation formats (JSON, XML), and hypermedia links (HATEOAS).

### 4. Statelessness

Stateless communication simplifies server-side implementation and scaling, as servers do not need to maintain client state between requests. Each request contains all necessary information for the server to process it.

### 5. Cacheability

RESTful APIs leverage the HTTP protocol's built-in caching mechanisms to improve performance and scalability. Responses can be cached at various levels (client, intermediary, server) to reduce latency and bandwidth usage.

## Conclusion

RESTful APIs offer a flexible and scalable approach to building networked applications. By adhering to the principles of REST, developers can design APIs that are simple, reliable, and interoperable, enabling seamless communication between clients and servers.
