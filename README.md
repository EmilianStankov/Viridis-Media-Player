Viridis Media Player
====================

![alt tag](viridis.bmp)


What is this?
-------------

This is my project for the FMI course 'Programming with Python'.
It will be an all-purpose media player. That means it will be able to play the most common media formats such as `mp3`, `wav`, `avi` etc.

### Functionality

* Basics
	- Playback for different media formats
	- __Playlist__ editing
	- __Play/pause__ button
	- __Previous__ button
	- __Next__ button
	- __Time slider__
	- __Volume slider__
	- Switch between __fullscreen__ and __windowed__

* For the audio
	- You will be able to __rate__ songs
	- __Metadata(id3 tags) will be editable__. This includes:
		+ Performer
		+ Song title
		+ Album
		+ Year released
		+ Genre
		+ Maybe more?

Why viridis?
------------

Since this is a Python course I felt like naming my project after a subspecies of the Pythonidae family.
I chose viridis since my favourite color is green.

#### Fun fact

The logo is supposed to resemble a snake head.

Milestone
---------

For the second milestone I should have implemented most of the backend + tests to go with it.
This includes building two (__SQLite__) databases (for the _playlists_ and _rating_).
On second thought I think the _rating_ will be better off in the __id3 tags__. So just one database - to store the playlists in.

What's done so far?
-------------------
* A __song__ class, the methods inside it are focused around __ID3 tags__, so they work with `mp3`s only. This will not be a problem once the gui is implemented. They will just not be reachable for other formats.
* A __movie__ class. Similar to the song class, this one is for `mkv` files and its methods will be unreachable for other formats. (The player will still support other media formats like `avi` and `wav`, there just won't be any metadata for these formats.)
* A __playlist__ class, it generates a playlist object, and saves it to a __SQLite database__.There is also a function to generate a playlist from apreviously saved one.
* I tried writing to the files, to make my own tagging, but could not do it properly. I did manage to write, but could not figure out how to read the data I've just added to the files, so I scratched that idea (for now).
* You can now add _playlists_ with the help of the gui. You can also _load_ them.
* The __player__ itself is now ready. It is completely functional. It consists of:
	- A __Play/Pause__ button
	- A __time slider__
	- A __timer__
	- __Visualization field__ (of course)
* __Next__ / __Previous__ buttons added. They work as expected.
* You can switch to __Fullscreen__ using `F11` at any time.
* Splash screen(sort of)
* Custom button _icons_

#### Libraries used
* `sqlite3`
* `stagger`
* `enzyme`
* `PyQt4 + Phonon`