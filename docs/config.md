# Config

## What are BackPipe configs?

BackPipe configs allow you to change the default address and port of your BackPipe servers. \
They also allow enabling HTML by sending a header. \
Configs can be used with the ```config``` class in BackPipe. \
The ```.address()``` method only takes values of type ```str``` as input. \
The ```.port()``` method only takes values of type ```int``` as input. \
The ```.html()``` method only takes values of type ```bool``` as input.

```py
from backpipe import *

# Set default address to 'localhost'
config.address("localhost")

# Set default port to '80'
config.port(80)

# Enable HTML
config.html(True)
```

## Congrats! 🎉

That's it! \
As you see BackPipe configs really are not difficult nor complex. \
To learn about BackPipe tools, flip over to the tab named 'Tools'.