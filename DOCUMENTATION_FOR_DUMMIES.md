# Documentation for dummies

Here's a little guide for all people, who are new to backpipe.

## Managing your installation of backpipe

**INSTALL:** 
```
pip install backpipe
```

**UPDATE:**
```
pip install --upgrade backpipe
```

## Creating a basic server

**Import the module**

```py
from backpipe import *
```

**Creating an instance of a server**

```py
server = BackPipe()
```

**Set the address and port**

```py
server = BackPipe(addr="", port=3000)
```

**Running your server**

```py
server.run()
```

That's how to make a server, which responses are not configured.

## Configuring responses and responding

### Basic GET-Request response

```py
from backpipe import *

server = BackPipe(addr="", port=3000)

@server.get()
def respond(r: Request):
    return (200, "Hello World!")

server.run()
```

> [!NOTE]  
> The same for POST, PATCH, PUT and DELETE requests.

### Example with POST:

```py
from backpipe import *

server = BackPipe(addr="", port=3000)

@server.post()
def respond(r: Request):
    return (200, "Hello World!")

server.run()
```

### Returned values explained

Each function, which is used as a request responder needs to return a tuple. \
The first value of the tuple is the HTTP status code and has to be an integer. \
The second value can be either a string or bytes, this is the body, that gets sent back to the client. 

**Example:**

```py
@server.get()
def respond(r: Request):
    return (200, "I'm the response body!")
```

Learn more about status code [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

### Responding the any request, that is GET, POST, PATCH, PUT, DELETE

> [!IMPORTANT]  
> @server.any overrides any other GET, POST, PATCH, PUT, DELETE responder \
> All of these need to be defined after the Any-Responder

```py
@server.any()
def respond(r: Request):
    return (200, "Try it with GET, POST, PATCH, PUT, DELETE and you'll get the same response!")
```

### Getting the method used

> [!TIP]  
> This might be useful when using @server.unknown, to know what method the client uses

```py
@server.any()
def respond(r: Request):
    return (200, f"You used the {r.method} method!")
```

### Working with methods, which are not officially supported.

```py
@server.any()
def respond(r: Request):
    return (200, "You used a supported method!")

@server.unknown()
def unknown_method_respond(r: Request):
    if r.method == "SECRET":
        return (200, "You found the secret method!")
    else:
        return (200, "You used an unsupported method!")
```

### Working with paths

**Responds with the path, you used to access the website**

```py
@server.get()
def respond(r: Request):
    return (200, f"Path: {r.path}")
```

**More complex example (full script)**

```py
from backpipe import *

server = BackPipe(addr="", port=3000)

@server.get()
def respond(r: Request):
    if r.path == "/":
        return (200, "Welcome to the Homepage")
    elif r.path == "/about":
        return (200, "Made with Backpipe")
    else:
        return (404, "Page does not exist")

server.run()
```
> [!NOTE]  
> HTTP Paths always start with a '/' as it is the root of the website.

### Reading the request's body

The request body is data sent by the client. \
The request body is usually in JSON or plain text format

> [!IMPORTANT]  
> Request.body is of type bytes

**Example, which sends back the request body**

```py
@server.get()
def respond(r: Request):
    return (200, r.body)
```

**More complex example (full script)**

> [!TIP]  
> Use the json tool to deserialize the JSON sent by the client

```py
from backpipe import *

server = BackPipe(addr="", port=3000)

stuff_list = []

@server.post()
def respond(r: Request):
    if r.path == "/api":
        data = tools.json.deserialize(r.body.decode())
        try:
            stuff = data["stuff"]
        except KeyError:
            return (400, "missing 'stuff' key in request body")
        my_list.append(stuff)
        return (200, "added 'stuff' to list")
    else:
        return (404, "API is located at path '/api'")
        
server.run()
```

### Getting request headers

**Request headers a part of the Request object.**
**They are stored as a dictionary.**

> [!IMPORTANT]  
> Raises KeyError, when trying to get value of a key, that does not exist

**Code, that returns the 'User-Agent' header**

```py
@server.post()
def respond(r: Request):
    try:
        return (200, r.headers["User-Agent"])
    except KeyError:
        return (400, "No 'User-Agent' header given!")
```

**More complex example (full script)**

```py
from backpipe import *

server = BackPipe(addr="", port=3000)

stuff_list = []

@server.post()
def respond(r: Request):
    try:
        if "Linux" in r.headers["User-Agent"]:
            return (200, "Seems like you are using Linux!")
        else:
            return (200, "Seems like, that you aren't using Linux!")
    except KeyError:
        return (400, "'User-Agent' header is missing.")
        
server.run()
```

### Getting the IP address of the client

**Example (What is my IP address?)**

```py
from backpipe import *

server = BackPipe(addr="", port=3000)

@server.get()
def respond(r: Request):
    return (200, r.address)

server.run()
```

### Getting the port used by the client to send the request

**Example (What port did I use to sent the request?)**

```py
from backpipe import *

server = BackPipe(addr="", port=3000)

@server.get()
def respond(r: Request):
    return (200, r.port)

server.run()
```

### Get path query

The path query is set by the path used by the client. 

<pre><code>http://local:3000/path<span style='color:red'>?query=value</span></code></pre>

**Getting a query**

```py
@server.get()
def respond(r: Request):
    return (200, f"{r.params}")
```

You can use the Request.params variable like any other provided by the Request class.

### Getting the full path

Using Request.path only gives the parsed path. \
Using Request.params only gives the parsed query. \
\
To get the raw path (which the client uses), \
you can use Request.raw_path. \
**This feature needs version 0.4.1 or higher!**

**How to implement it into a responder**

```py
@server.get()
def respond(r: Request):
    return (200, r.raw_path)
```

You can use the Request.raw_path variable like any other provided by the Request class.

### Redirecting

Redirecting is possible by returning the redirect() object in your response function. \
The redirect function returns a BackPipeRedirect() object, which specifies where the client should be redirected to and with what message.

**Full Example**

```py
from backpipe import *

config.html(True)

server = BackPipe()

@server.any()
def wrong_method(r: Request):
    return (405, f"method '{r.method}' is not allowed")

@server.unknown()
def unknown_method(r: Request):
    return (405, f"method '{r.method}' is not allowed")

@server.get()
def respond(r: Request):
    if r.path == "/github":
        return redirect("https://github.com/Simoso68/backpipe", "<p>Moved to </p><a href='https://github.com/Simoso68/backpipe'>GitHub</a>")
    else:
        return (200, "Hello this is my page.")

server.run()
```