# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert ColorspaceGamut to Fusion GamutConvert

    Returns:
        dict with fusion formatted effect attributes.
    """

    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    # Set default values
    fusion_effect_attribs["\t\t\tToRed"] = "Input {Value = 5, }" # 5: Red BG
    fusion_effect_attribs["\t\t\tToGreen"] = "Input {Value = 6, }" # 6: Green BG
    fusion_effect_attribs["\t\t\tToBlue"] = "Input {Value = 7, }" # 7: Blue BG
    fusion_effect_attribs["\t\t\tToAlpha"] = "Input {Value = 8, }" # 8: Alpha BG

    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

        if knob == "channels":
            # This is a duplicate of the conversion found in CommonAttributes.
            # The fusion ChannelBoolean node will have the channels disabled in two places.
            # This may cause confusion for the user.
            # TODO: Raise minor warning about this.
            if value == "all":
                #TODO: Add support for fusion auxiliary channels.
                #TODO: Flag to user if there are any extra channels in the pipe.
                pass
            if value == "rgb":
                fusion_effect_attribs["\t\t\tToAlpha"] = "Input {Value = 4, }" # 4: Do Nothing
            if value == "alpha":
                fusion_effect_attribs["\t\t\tToRed"] = "Input {Value = 4, }" # 4: Do Nothing
                fusion_effect_attribs["\t\t\tToGreen"] = "Input {Value = 4, }" # 4: Do Nothing
                fusion_effect_attribs["\t\t\tToBlue"] = "Input {Value = 4, }" # 4: Do Nothing
            if value.startswith("{"): #individual channels selected
                if "-rgba.red" in value:
                    fusion_effect_attribs["\t\t\tToRed"] = "Input {Value = 4, }" # 4: Do Nothing
                if "-rgba.green" in value:
                    fusion_effect_attribs["\t\t\tToGreen"] = "Input {Value = 4, }" # 4: Do Nothing
                if "-rgba.blue" in value:
                    fusion_effect_attribs["\t\t\tToBlue"] = "Input {Value = 4, }" # 4: Do Nothing
                if "-rgba.alpha" in value or "rgba.alpha" not in value:
                    fusion_effect_attribs["\t\t\tToAlpha"] = "Input {Value = 4, }" # 4: Do Nothing

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
