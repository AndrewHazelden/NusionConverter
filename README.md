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

## Supported Nodes
Lots of supported nodes are on the way!

Nuke to Fusion

- Blur
- Dot
- Transform
- Invert
- Premult
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
