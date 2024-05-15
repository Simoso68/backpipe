# BackPipe Documentation

Welcome to the BackPipe Documentation! 👋 \
Use the tabs above to navigate through it. \
This documentation is made with [streamlit](https://streamlit.io). \
\
Check out the [PyPI Page](https://pypi.org/project/backpipe).

## Before that ...

You might want to install BackPipe

```
pip install backpipe
```

Or update it to the newest version

```
pip install --upgrade backpipe
```

## Importing backpipe

To use BackPipe, you need to import it first.

Either import it using the ```import``` keyword or ```from {module} import *```. \
Using the normal way to import helps against naming conflicts, but is longer to write. \
Using the ```from``` keyword makes your life easier, except you encounter naming conflicts.

### Using ```import {module}```

```py
import backpipe

# Your code goes here ...
```

### Using ```from {module} import *```

```py
from backpipe import *

# Your code goes here ...
```

## Note

This documentation will use the ```from {module} import *``` way. \
If you want to use the ```import {module}``` way, remember to put ```backpipe.``` in front of BackPipe's functions, classes, variables, etc.