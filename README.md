# Pythonic Garage Band
Author: Richard Whitehead Version: 1.0.2

Overview
Program which uses Python classes to model a Band made up of different kinds of musicians like Guitarist,Bassist, and Drummer. Musician base class used to handle common functionality which particular kinds of musicians will inherit.

Getting Started
In terminal navigate to the folder with the pythomic_garage_band.py.
Run command "python .py".
Architecture
Python 3.8.2
Pytest

# API

class Musician: creates instances of the Musicians
class Guitarist(Musician): inherits properties of Musician class
class Bassist(Musician): inherits properties of Musician class
class Drummer(Musician): inherits properties of Musician class
class Band: creates instances of the Band from the provided data_file

# Change Log

06/10/2020 1612 - initial set up
06/10/2020 1800 - Musician instance and Guitarist instance created
06/10/2020 21:30 - Musician class created
06/11/2020 1500 - Musician instance and Guitarist instance created
06/10/2020 1900 - function play_solos() added

*still working through a few bugs and will resubmit when complete

