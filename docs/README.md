# Welcome to Nusion Converter

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
- Dot
- Invert
- NoOp
- Null
- Premult
- Read
- StickyNote
- Transform
- Unpremult
- Write
- ColorCorrect (Coming soon!)

Fusion to Nuke

- (Coming soon!)

## Partial Support

The following nodes have partial conversion support:

### Add

### Difference

### Divide

### Max

### Min

### Minus

### Multiply

### Cube

### Cylinder

### Sphere

### Text2

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

The Nusion Web app was created by Jonty Pressinger. The Nusion integration for Fusion Studio was created by Andrew Hazelden.

- [MIT](https://choosealicense.com/licenses/mit/) Open-Source License

-------------------------

All trademarks, logos, and brand names are the property of their respective owners.
