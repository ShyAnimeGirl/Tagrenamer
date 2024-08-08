# Tagrenamer
A small script which takes in an audio file and renames it based on the embedded ID3 title tag.

### Useage
This is how I use this script:
```
find . -type f -name '*.ogg' -exec python3 tagrename.py {} \;
```
This command will find all ogg files recursively within a folder and automatically feed them into tagrename.

### Requirements
Install the following modules:

[tinytag](https://github.com/tinytag/tinytag)
```
python3 -m pip install tinytag
```

### Possible Issues
This script currently does NO checking to see if the filename is valid, so theoretically an audio file could contain characters in its title tag which could possibly break the program or cause some kind of data loss. This is assuming tinytag does not convert things like “/” into alternate file system safe characters, which it might already do? 

It also does not check for existing files with the same name, so if you have multiple files with the same title tag it may overwrite them.
