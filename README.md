# World Clock using appindicator

I recently switched to Manjaro XFCE. I choose XFCE because I loved it's snappy feeling. It however has some drawbacks. One of them was lack of a good world clock. As a freelancer it is quite handy to keep a track of the time at my client's place.
But I do mostly backend work and have no idea about in depth gtk or other GUI framework. I already had made a simple appindicator gtk app for another project. So I used that as a base and made the rest.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip3 install -r requirements.txt
```

The app also requires gi module of python which is usually installed. If it's not installed it can installed with:
```bash
sudo apt-get install python3-gi # Ubuntu/Debian
```
I am not sure how to use it on arch based distors as it was pre-installed in my distro (Manajro Xfce).

## Usage

The first time you run the app you have to open the timezones.txt file and remove the "#" from the beginning of the timezones you want to enable.
If you wish to generate a new timezones.txt ( thus deleting previously enabled timezones) run this command from the project folder.
```bash
python3 get_tz.py
```

To start it go to it's folder and run:
```bash
python3 main.py
```
There is also a desktop file which is Executable .desktop file included which can be used to run the application. The .desktop file can also be moved to ~/.config/autostart/ for auto starting the app when you log in.
** Make sure you change the <username> in line 4 of the .desktop file with your username before running it.

## Contributing
This was made as a quick alternative for a world clock. It can be improved in a lot of ways if that's worth it

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)