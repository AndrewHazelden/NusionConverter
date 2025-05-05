``` 
    _   __              _                  ______                                 __             
   / | / /__  __ _____ (_)____   ____     / ____/____   ____  _   __ ___   _____ / /_ ___   _____
  /  |/ // / / // ___// // __ \ / __ \   / /    / __ \ / __ \| | / // _ \ / ___// __// _ \ / ___/
 / /|  // /_/ /(__  )/ // /_/ // / / /  / /___ / /_/ // / / /| |/ //  __// /   / /_ /  __// /    
/_/ |_/ \__,_//____//_/ \____//_/ /_/   \____/ \____//_/ /_/ |___/ \___//_/    \__/ \___//_/     
                                                                                                
```
Nusion is a Web app to convert nodes between Foundry's Nuke and Blackmagic's Fusion.

## Requirements

- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [Node.js](https://nodejs.org/en/)
- [NPM](https://www.npmjs.com/get-npm/)

## Installation

### Windows:

Use [pip](https://pip.pypa.io/en/stable/) and [NPM](https://www.npmjs.com/get-npm/) to install project dependencies.

```bash
pip install -r requirements.txt
```
```bash
npm install
```
Start the Flask development server.

```bash
python app/app.py
```

### macOS:

Install a recent version of Python 3.x from the official [Python org website](https://www.python.org/downloads/).

Create a virtual environment:

```bash
cd $HOME/
python3 -m venv nusion
source $HOME/nusion/bin/activate
```

Clone the repo and install the dependencies using the Homebrew and pip package managers:

```bash
brew install npm
pip3 install --upgrade pip
pip3 install flask
cd $HOME/
git clone https://github.com/AndrewHazelden/NukeToFusion.git
cd $HOME/NukeToFusion/
pip3 install -r requirements.txt
```

Activate the virtual environment and start the Flask app:

```bash
source $HOME/nusion/bin/activate
cd $HOME/NukeToFusion/app
flask run
```

Open a webbrowser session to view the web app:

```bash
open http://127.0.0.1:5000/

```

## License
[MIT](https://choosealicense.com/licenses/mit/)
                                                                  
