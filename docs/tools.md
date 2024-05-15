# Tools

## What are BackPipe tools?

BackPipe tools offer functionality already in Python, but with an easier syntax. \
BackPipe tools offer Base64 En-/Decoding, File handling, Hashing, HTML building, JSON parsing. 

## Guides for all tools

### Base64

Encoding is possible with ```tools.base64.encode()```. \
Decoding with ```tools.base64.decode()```. \
Both only take values of type ```bytes```. \
\
Example, which encodes and then decodes your ```bytes```.

```py
from backpipe import tools

MESSAGE = b"Hello World!"

ENCODED = tools.base64.encode(MESSAGE)

print(tools.base64.decode(ENCODED))
```

### File

File handling allows you to create, delete, write or append to files. \
All this is possible with the corresponding keywords under ```tools.file```. \
```.create()``` and ```.delete()``` only take filenames of type ```str``` as the only parameter. \
```.write()``` and ```.append()``` take a second one in addition to that, which takes the file contents, which must be of type ```str``` or ```bytes```.
\
Example, which deletes a file, creates a new one, writes to it and then appends text.

```py
from backpipe import tools

tools.file.delete("my_cool_file.txt")
tools.file.create("my_new_file.txt")
tools.file.write("my_new_file.txt", "Hello ")
tools.file.append("my_new_file.txt", "World!")
```

### Hashing

Hashing is a procedure, which allows to make a string of text into a new string, which can not be returned to its original form. \
This is possible due to a mathematical formular, which makes calculating the hashed string back impossible. \
Hashes are unique and algorythms having one hash for multiple strings are called unsafe. \
```sha1``` has been deemed unsafe due to that. \
\
BackPipe has the following hashing algorythms implemented:

- md5
- sha1
- sha224
- sha256
- sha384
- sha512

The functions under ```tools.hash``` have the same name as the algorythms. \
These functions accept text of type ```str``` or ```bytes```. \
And they return text of type ```bytes```. \
\
More complex example with the sha256 algorythm

```py
from backpipe import *

server = BackPipe()

def unsupported_method(r: Request):
    return (405, "Unsupported method, use POST")

@server.any()
def any_respond(r: Request):
    return unsupported_method(r)

@server.unknown()
def unknown_respond(r: Request):
    return unsupported_method(r)

@server.post()
def on_post(r: Request):
    if not r.path == "/hash-my-string"
        return (404, "Endpoint not found")
    return (200, tools.hash.sha256(r.body))

server.run()
```

### HTML

The HTML builder provided by BackPipe is not advanced. \
It is just there, to make simple HTML code. \
\
To get started, initialize a new HTML builder like this:

```py
from backpipe import tools

html = tools.html.HTML()
```

Then add HTML head tags with the ```.add_head_tag()``` method. \
This method takes a tag name, inner HTML and parameters, the first two must be of type ```str``` and the parameters of type ```dict```. \
\
You can also add elements within your HTML body with the ```.add_tag()``` method. \
It has the same structure as ```.add_head_tag()``` \
\
Add self-closing tags with the ```.add_tag_self_closing()``` method. \
The same for self-closing head tags with the ```.add_head_tag_self_closing()```. \
Self-closing tags don't take inner HTML as a parameter as they can't have it. \
\
Adding meta tags is made extra easy with the ```.add_meta_tag()``` method. \
This method takes two parameters, the first one the name of the meta data and the content of it. \
Both must be of type ```str```. \
\
Adding some CSS is possible with the ```.add_style()``` method. \
This method takes one parameter, which must be of type ```str```. \
\
After adding all of these elements, tags, style, you can get the pure HTML in text form with the ```.text()``` method. \
This method returns the HTML as a text of type ```str```. \
\
Simple Example:

```py
from backpipe import *

config.html(True)

server = BackPipe()

def unsupported_method(r: Request):
    html = tools.html.HTML()

    html.add_head_tag("title", "Unsupported method")
    html.add_tag("p", "Only accepting requests using the GET method.")
    html.add_tag_self_closing("br")
    html.add_tag("p", f"You used {r.method}")

    return (405, html.text())

@server.any()
def any_respond(r: Request):
    return unsupported_method(r)

@server.unknown()
def unknown_respond(r: Request):
    return unsupported_method(r)

@server.get()
def on_get(r: Request):
    html = tools.html.HTML()

    html.add_head_tag("title", "My HTML page")
    html.add_tag("p", f"Your IP address is: {r.address}")

    return (200, html.text())

server.run()
```

### JSON

BackPipe's JSON tool allows serializing and deserializing of dictionaries/strings containing JSON \
Both are done with the ```serialize()``` and ```deserialize()``` functions respectively.

## Congrats! 🎉

Although this was a bit to read, you did it. \
To learn more about BackPipe read the pages by clicking on their corresponding tabs.