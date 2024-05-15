# Redirects

## What are redirects?

Redirects allow a server to make the client call another server after calling the initial one. \
Redirecting is possible with the 'Location' header sent by the server.

## How to use them in BackPipe

Redirects are easy to use in BackPipe. \
One just needs to return redirect() instead of an Iterable in the response function. \
BackPipe automatically sends status ```301``` to indicate a redirection. \
The first parameter must be the destination URL with the scheme (http/https). \
The second one is the response body. \
The response body can only be seen by the client, when redirects don't work or are not allowed.

## Example

This example shows how to redirect a client to https://google.com if requested via the GET method. \
Otherwise send back a message saying 'Hello!'

```py
from backpipe import *

server = BackPipe()

def hello(r: Request):
    return (200, "Hello!")

@server.any()
def any_respond(r: Request):
    return hello(r)

@server.unknown()
def unknown_respond(r: Request):
    return hello(r)

@server.get()
def redirect_to_google(r: Request):
    return redirect("https://google.com", "Client does not allow redirects")

server.run()
```

## Congrats! 🎉

You have now learned how redirects work. \
If you want to learn what a BackPipe Config is, then flip over to the tab named 'Config'
