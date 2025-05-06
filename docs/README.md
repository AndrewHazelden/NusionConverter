# Welcome to Nusion Converter

Nusion is a Web app to convert nodes between Foundry's Nuke and Blackmagic Design's Fusion Studio compositing software. There is a Fusion Studio integration plugin that adds an "Edit &gt; Paste Nusion" menu item.

## Screenshots

Nusion can run from your webbrowser using a local Nusion Server session hosted on your workstation.

![Webapp](images/screenshot.png ':size=650')

If you have Blackmagic Fusion Studio, the "Paste Nusion" menu entry and Lua comp script allows you to convert a Foundry Nuke .nk node snippet into a BMD Fusion Studio native node. The result is pasted directly into your composite.

![Paste Nusion](images/paste_nusion.png ':size=650')

## Supported Nodes

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

To test the Nusion Web app, you can copy/paste the following Nuke blur node snippet:

    Blur {
     inputs 1+1
     size 4
     name car_Dust_Blur
     xpos 950
     ypos 1330
    }

## License

- [MIT](https://choosealicense.com/licenses/mit/) Open-Source License

-------------------------

All trademarks, logos, and brand names are the property of their respective owners.
