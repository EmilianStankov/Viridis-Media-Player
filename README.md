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
