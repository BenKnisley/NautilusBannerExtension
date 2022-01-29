Nautilus Banner Extension
=
Nautilus extension that provides an way to display a custom text banner at the 
top of a Nautilus window. Scans each folder displayed by Nautilus for a file 
named '.banner', if found the text inside the file is displayed on the banner at
the top of the window.

## Install

Step 1. 
Install Nautilus Python Library
```sh
sudo apt install python3-nautilus
```

Step 2. 
Run Install Script
```sh
./install.sh
```
The install script will also reinstall the extension from source if ran again. Makes for easy development.

## Usage
Create a file named .banner in any directory, put some text in, and navigate to that directory in Nautilus. Enjoy the lovely banner at the top. 

Banner text supports some html tags, such as < b >, < i >, and even < a >.

Enjoy.