# tsc ( Troubleshooting Scenarios Creator )

tsc ( Troubleshooting Scenarios Creator ) will help you create a variety of scenarios to go further on troubleshooting training and increase you skills.
It's easy to use and new scenarios can be attached easily by creating new plugins.

### Usage:

`tsc create -p <problem scenario>`

`tsc create -p xyz`

Multiple:

`tsc create -p xyz -p abc`

### New scenarios:

New scenarios can be easily added, you only need to follow some minor specifications so the plugin can be recognized.
They are primarily written either in Python or Shell Script, however, nothing stops you from using another language. Only keep in mind that you need to follow some simple specs.

See below an example of how a plugin looks like:

```
#!/bin/bash

# This script will change permissions from /bin/chmod binary making
# it not usable.

```

That's the most important line. It will specify the Linux Distribution.
If it applies for all, just use "All"

`OS=All`

In case it applies for only a few Distributions, you write it like below:

`OS="Ubuntu, Debian"`

Otherwise, if it's only applicable for one single distribution:

`OS=Ubuntu`

`/bin/chmod -x /bin/chmod || exit 1`




