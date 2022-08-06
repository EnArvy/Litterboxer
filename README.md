# Catboxer
![Litterbox logo](https://litterbox.catbox.moe/resources/litterbox.png)


Upload files to LitteTemporary filehost) via Send to right click menu(Windows).

Written in python.

## Installation

Just paste the release file `Litterboxer.exe` in the following location:
`C:\Users\YourUserName\AppData\Roaming\Microsoft\Windows\SendTo\`

## Usage

* Right click on any file/folder.
* Choose `Send to`.
* Choose `Litterboxer.exe`.

The url of the upload will be displayed as well as copied to the clipboard automatically.

## Limitations

Files of sizes above 1GB are not allowed.

## Credits

[Litterbox](https://litterbox.catbox.moe/)

## Building from Source

* Clone this repository
* Run `pip install -r requirements.txt`
* Run `pyinstller --onefile -i Litterboxer.ico Litterboxer.py`