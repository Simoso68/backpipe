# Request Object

## What is the Request Object?

The Request object is an object representing the values given in the client's request to the server. \
It holds multiple variables as attributes helping you and the server to know more information about the client. \
This might be really useful when making APIs.

## Available variables/attributes

| Attribute | Represents                                  |
| --------- | ------------------------------------------- |
| address   | Client's IP address                         |
| port      | Port used by the client to connect          |
| method    | HTTP method used by the client              |
| path      | Parsed path (without query)                 |
| params    | Parsed path (only query)                    |
| raw_path  | Unparsed path                               |
| headers   | Dictionary holding client's request headers |

## Example, which responds with every information known

```py
from backpipe import *

# Initialize server instance
server = BackPipe()

# Response function for everything
def respond(r: Request):
    return (200, f"IP address: {r.address}\nPort: {r.port}\nMethod: {r.method}\nPath: {r.path}\nQuery: {r.params}\nUnparsed path: {r.raw_path}\nHeaders (Dictionary): {r.headers}")

# Set response function for any
@server.any()
def any_respond(r: Request):
    return respond(r)

# Set response function for unknown
@server.unknown()
def unknown_respond(r: Request):
    return respond(r)

# Run the server
server.run()
```

## Congrats! 🎉

You have made it through the basics of Request objects. \
Also want to learn how to redirect clients to another site? \
If you want to learn more about it, flip over to the tab called "Redirects"