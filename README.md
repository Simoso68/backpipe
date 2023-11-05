<h1 align=center>Backpipe</h1>

<p align=center>Back-Ends simplified.</p>

<pre align=center><code>pip install</code></pre>

## Why the name?

The name 'Backpipe' is inspired by the english word 'Bagpipe'. \
I decided to call it 'Backpipe', because it is a **Back**-End Framework. \
It is just a little pun.

## Samples

### Hello World!

```python
import backpipe

server = backpipe.BackPipe()

@server.get
def hello_world(r: backpipe.Request):
    return (200, "Hello World")

server.run()
```

### What is my IP address?

```python
import backpipe

server = backpipe.BackPipe()

@server.get
def my_ip_address(r: backpipe.Request):
    return (200, r.address)

server.run()
```

### Complex Example

```python
import backpipe

server = backpipe.BackPipe()

@server.get
def wrong_method(r: backpipe.Request):
    return (405, "Wrong method, use POST.")

@server.put
def wrong_method(r: backpipe.Request):
    return (405, "Wrong method, use POST.")

@server.patch
def wrong_method(r: backpipe.Request):
    return (405, "Wrong method, use POST.")

@server.delete
def wrong_method(r: backpipe.Request):
    return (405, "Wrong method, use POST.")

@server.unknown
def unknown_method(r: backpipe.Request):
    return (405, "Unsupported method, use POST.")

@server.post
def login(r: backpipe.Request):
    try:
        if r.headers["key"] == "password1234":
            return (200, "Password correct!")
        else:
            return (304, "Password wrong!")
    except KeyError:
        return (400, "invalid request, 'key' header missing.")

server.run()
```

## License

Backpipe is licensed under the GNU GPL v3.