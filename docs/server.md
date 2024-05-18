# BackPipe Server's

## What is a Server?

A server is a kind of software dedicated to respond to any request made by a client. \
A server can also be understood as a computer made to host server software. \
In BackPipe a server is a class, which represents the server software, that you create by using BackPipe. \
In the BackPipe module the class is named ```BackPipe()```

## Creating an instance

The BackPipe class can be initialized by creating a new instance of it. \
This is possible by calling it in any way. \
The best way is to save the class inside a new variable. \
This variable then holds a new instance of the BackPipe class.

```py
server = BackPipe()
```

## Specifying address & port

Address and port can be specified by passing the address and port parameters with their respective values. \
The address must be a value of type ```str```. \
The port must be a value of type ```int```. \
The address is set to ```""``` by default, which is another way to specify ```127.0.0.1``` \
Changing it is not recommended if one is not experienced. \
The port is set to ```3000``` by default.

```py
# Example with default address and port 8000
server = BackPipe(address="", port=8000)
```

## Running the server

After doing some small configuration, you may want to run your server. \
Running it on your local network is as easy as it gets! \
Just use the ```.run()``` method, which is part of the ```BackPipe()``` class. \
This will deploy the server on the specified port and address.

```py
# Creating server instance with specified port 8000
server = BackPipe(port=8000)

# Run the server
server.run()
```

## Congrats! 🎉

You now know how to create a basic server. \
But, you want to configure the responses sent to the client of it, do you? \
To learn this, flip over to the tab called "Responses"