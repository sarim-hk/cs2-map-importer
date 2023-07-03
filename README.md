# [CS2] Map Import Tool
The tools provided by Valve for importing maps aren't very user friendly, this tool makes it easier to use by providing an interface for it, as well as providing some ease of use features.

## Features
- Saves directories between uses, for quickly importing multiple maps in the same directory.
- Utilises Windows File Explorer so you don't need to manually copy/paste the directory paths you're using.
- Less inputs needed; the tool only takes the `Counter-Strike Global Offensive` folder and figures out the rest for you (assuming correct directory structuring).
- Will create a temporary `/maps/` folder for any selected `.vmf` without one, as this is necessary for Valve's scripts to work correctly.

## Prerequisites
While this tools makes the porting process much easier, there's still some work you need to do yourself:

- Python must be installed (either `2.7.14` or `3.x`) and added to `PATH`.
- `python -m pip install colorama` is necessary for Valve's scripts to work with the tool.
- Make sure your `.vmf` isn't in your `Counter-Strike Global Offensive` folder. It can be anywhere, just not there.
- If you have any custom content in your map, make sure it's in your CS:GO's materials and models folders. This can be done by decompiling the map and copying the materials and models over.
- A CS2 addon needs to be created before importing the map.

## Support

- Read Valve's documentation [here](https://developer.valvesoftware.com/wiki/Source_2/Docs/Level_Design/Import_Tool_Documentation).
- Open an issue on GitHub.
- DM me on Twitter, [@hk_sarim](https://twitter.com/hk_sarim).
