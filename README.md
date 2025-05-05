``` 
    _   __              _                  ______                                 __             
   / | / /__  __ _____ (_)____   ____     / ____/____   ____  _   __ ___   _____ / /_ ___   _____
  /  |/ // / / // ___// // __ \ / __ \   / /    / __ \ / __ \| | / // _ \ / ___// __// _ \ / ___/
 / /|  // /_/ /(__  )/ // /_/ // / / /  / /___ / /_/ // / / /| |/ //  __// /   / /_ /  __// /    
/_/ |_/ \__,_//____//_/ \____//_/ /_/   \____/ \____//_/ /_/ |___/ \___//_/    \__/ \___//_/     
                                                                                                
```

Nusion is a Web app to convert nodes between Foundry's Nuke and Blackmagic Design's Fusion Studio compositing software.

## Screenshot

![Webapp](docs/images/screenshot.png)

## Supported Notes
Lots of supported nodes are on the way!

Nuke to Fusion

- Blur
- Transform
- Invert
- Premult
- Unpremult
- ColorCorrect (Coming soon!)

Fusion to Nuke

- (Coming soon!)

## Example Nuke Node Snippet

To test the nusion web app, you can copy/paste the following Nuke blur node snippet:

    Blur {
     inputs 1+1
     size 4
     name car_Dust_Blur
     xpos 950
     ypos 1330
    }

## License

- [MIT](https://choosealicense.com/licenses/mit/) Open-Source License

## Nusion Installation

### Requirements

- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [Node.js](https://nodejs.org/en/)
- [NPM](https://www.npmjs.com/get-npm/)

### Windows Install:

Use [pip](https://pip.pypa.io/en/stable/) and [NPM](https://www.npmjs.com/get-npm/) to install project dependencies.

```bash
pip install -r requirements.txt
```
```bash
npm install
```
Start the Flask development server.

```bash
cd NusionConverter/app
flask run
```

### macOS Install:

Install a recent version of Python 3.x from the official [Python org website](https://www.python.org/downloads/).

Install the Homebrew package manager:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Create a new Python virtual environment:

```bash
cd $HOME/
python3 -m venv nusion
source $HOME/nusion/bin/activate
```

Clone the repo and install the dependencies using Homebrew and Python pip package managers:

```bash
brew install npm
pip3 install --upgrade pip
pip3 install flask
cd $HOME/
git clone https://github.com/AndrewHazelden/NusionConverter.git
cd $HOME/NusionConverter/
pip3 install -r requirements.txt
```

Activate the Python virtual environment and start the Flask app:

```bash
source $HOME/nusion/bin/activate
cd $HOME/NusionConverter/app
flask run
```

Open a webbrowser session to view the web app:

```bash
open http://127.0.0.1:5000/
```

## cURL Usage

The Nusion Web app can use cURL from the terminal to process JSON encoded Nuke scripts.

The Nuke node data is stored in a "data" JSON key that is submitted by cURL via an HTTP post request.

```bash
curl 'http://127.0.0.1:5000/convert' -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Referer: http://127.0.0.1:5000/' -H 'Content-Type: application/json' -H 'Origin: http://127.0.0.1:5000' -H 'Connection: keep-alive' --data-raw '{"data":"Blur {\n inputs 1+1\n size 4\n name car_Dust_Blur\n xpos 950\n ypos 1330\n}","width":"1920","height":"1080","fromSoftware":"nuke"}'
```


cURL Terminal Result:

The Fusion formatted node data can be accessed using the "result" JSON key.

```json
{"result":"{\nTools = ordered() {\ncar_Dust_Blur = Blur {\nInputs = {\nXBlurSize = Input { Value = 1.43561, },\n},\nViewInfo = OperatorInfo {\nPos = { 950, 1330 },\n},\n}\n}\n}"}
```


