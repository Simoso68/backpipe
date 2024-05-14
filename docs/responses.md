# Responses

## What are responses?

Responses allow you to sent back information to the client. \
HTTP responses have some crucial parts, but BackPipe only focuses on the status code and response body. \
This can be configured by the developer. \
Each response function needs to return an iterable like a tuple or list. \
The first value needs to be an integer sent as the status code. \
The second value needs to be a string or bytes sent as the response body.

## What are response functions?

In BackPipe, response functions are being used to declare how the server answers to client requests. \
BackPipe supports GET, POST, PATCH, PUT and DELETE by default as HTTP methods. \
But you can extend the support by using the ```unknown()``` decorator. \
BackPipe will use the response function corresponding to the HTTP method used. \
If the method is not supported by BackPipe by default, it will be handled by the response function decorated with ```unknown()```.
Response functions need to take a Request object as a parameter. \
The Request object represents the values given in the client's request to the server.
## Full example with a GET method responder

```py
from backpipe import *

# Initialize server instance
server = BackPipe()

# On GET request
@server.get()
def respond(r: Request):
    return (200, "Hello World!") # send back 'Hello World!' with status code 200

# Run the server
server.run()
```

## Example with all the HTTP method decorators

```py
from backpipe import *

# Initialize server instance
server = BackPipe()

# Response function for all methods
def respond(r: Request):
    return (200, f"Hey, you are using the {r.method} method!")

# On GET request
@server.get()
def get_respond(r: Request):
    return respond(r)

# On POST request
@server.post()
def post_respond(r: Request):
    return respond(r)

# On PATCH request
@server.patch()
def patch_respond(r: Request):
    return respond(r)

# On PUT request
@server.put()
def put_respond(r: Request):
    return respond(r)

# On DELETE request
@server.delete()
def delete_respond(r: Request):
    return respond(r)

# On unknown request (Method not supported by default in BackPipe)
@server.unknown()
def unknown_respond(r: Request):
    return respond(r)

# Run the server
server.run()
```

## Make it shorter with ```any()```

The ```any()``` decorator is like the other decorators, but it covers GET, POST, PATCH, PUT & DELETE. \
It overrides every previously defined response function (except ```unknown()```). \
But defining another response function with a decorator like ```get()``` after the ```any()``` decorator will override the corresponding response function previously covered by the ```any()``` decorator. \
And so on and so forth.

```py
from backpipe import *

# Initialize server instance
server = BackPipe()

# Answering every request (except unknown)
@server.any()
def respond_to_any(r: Request):
    return (200, "Hey, you are not using GET")

# Configuring the response for requests, which are not using GET, POST, PATCH, PUT or DELETE
@server.unknown()
def respond_to_unknown(r: Request):
    return (405, "I don't know that one, but it is not GET")

# Configuring GET after any() to not be overridden
@server.get()
def respond_to_get(r: Request):
    return (200, "You are using GET")

# Run the server
server.run()
```

## Congrats! 🎉

You have made it through the basics of responses. \
But, you may have seen this Request object along the way. \
If you want to learn more about it, flip over to the tab called "Request Objects"