``` 
    _   __              _                  ______                                 __             
   / | / /__  __ _____ (_)____   ____     / ____/____   ____  _   __ ___   _____ / /_ ___   _____
  /  |/ // / / // ___// // __ \ / __ \   / /    / __ \ / __ \| | / // _ \ / ___// __// _ \ / ___/
 / /|  // /_/ /(__  )/ // /_/ // / / /  / /___ / /_/ // / / /| |/ //  __// /   / /_ /  __// /    
/_/ |_/ \__,_//____//_/ \____//_/ /_/   \____/ \____//_/ /_/ |___/ \___//_/    \__/ \___//_/     
                                                                                                
```

Nusion is a "Nuke to Fusion" node converter that converts nodes between Foundry's Nuke and Blackmagic Design's Fusion Studio compositing software. Simply copy a node from your active Nuke composite, and allow Nusion to remap the Nuke node and its attributes into the nearest equivalent node available in Resolve Studio/Fusion Studio. Simple and easy.

Nusion is available as a self-hosted web app that runs directly in your web browser. The new plugin integration version of "Nusion for Fusion" can be installed in Resolve's Fusion page/Fusion Studio using the community maintained Reactor Package manager. The "Nusion for Fusion" plugin allows you to access a "Edit &gt; Paste Nusion" menu item. This will take a Foundry Nuke node from your clipboard and instantly translate it into the corresponding Fusion Studio node. The result is pasted directly into your Fusion flow, ready for use.

## Screenshots

Nusion can run from your web browser using a local Nusion Server session hosted on your workstation.

![Webapp](docs/images/screenshot.png ':size=650')

If you have Blackmagic Fusion Studio, the "Paste Nusion" menu entry and Lua comp script allows you to convert a Foundry Nuke .nk node snippet into a BMD Fusion Studio native node. The "Shift + N" hotkey can also be used to carry out the conversion task.

![Paste Nusion](docs/images/paste_nusion.png ':size=650')

## Supported Nodes

Lots of supported nodes are on the way!

Nuke to Fusion

- BackdropNode
- Blur
- Constant
- Dot
- Invert
- NoOp
- Null
- Premult
- Read
- Saturation
- StickyNote
- Transform
- Unpremult
- Write
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

The Nusion Web app was created by Jonty Pressinger. The Nusion integration for Fusion Studio was created by Andrew Hazelden.

- [MIT](https://choosealicense.com/licenses/mit/) Open-Source License

## For More Info

For Nusion installation and usage details check out the [Nusion Documention Site](https://andrewhazelden.github.io/NusionConverter/) or the "Install.md" file in the repository.
