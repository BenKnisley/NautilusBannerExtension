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

## License
Copyright (c) 2022 Ben Knisley (ben@knisley.co)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.