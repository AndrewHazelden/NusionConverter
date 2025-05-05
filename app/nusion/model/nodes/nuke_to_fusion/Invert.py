# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Nuke Invert to Fusion Channel Boolean

    Returns:
        dict with fusion formatted effect attributes.
    """

    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    # Create Channel Boolean set to Negative
    fusion_effect_attribs["Operation"] = "Input {Value = 10, }" # 10: Negative

    # Set default values
    fusion_effect_attribs["ToRed"] = "Input {Value = 5, }" # 5: Red BG
    fusion_effect_attribs["ToGreen"] = "Input {Value = 6, }" # 6: Green BG
    fusion_effect_attribs["ToBlue"] = "Input {Value = 7, }" # 7: Blue BG
    fusion_effect_attribs["ToAlpha"] = "Input {Value = 8, }" # 8: Alpha BG

    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

        if knob == "channels":
            # This is a duplicate of the conversion found in CommonAttributes.
            # The fusion ChannelBoolean node will have the channels disabled in two places.
            # This may cause confusion for the user.
            # TODO: Raise minor warning about this.
            if value == "all":
                #TODO: Add support for fusion auxilary channels.
                #TODO: Flag to user if there are any extra channels in the pipe.
                pass
            if value == "rgb":
                fusion_effect_attribs["ToAlpha"] = "Input {Value = 4, }" # 4: Do Nothing
            if value == "alpha":
                fusion_effect_attribs["ToRed"] = "Input {Value = 4, }" # 4: Do Nothing
                fusion_effect_attribs["ToGreen"] = "Input {Value = 4, }" # 4: Do Nothing
                fusion_effect_attribs["ToBlue"] = "Input {Value = 4, }" # 4: Do Nothing
            if value.startswith("{"): #individual channels selected
                if "-rgba.red" in value:
                    fusion_effect_attribs["ToRed"] = "Input {Value = 4, }" # 4: Do Nothing
                if "-rgba.green" in value:
                    fusion_effect_attribs["ToGreen"] = "Input {Value = 4, }" # 4: Do Nothing
                if "-rgba.blue" in value:
                    fusion_effect_attribs["ToBlue"] = "Input {Value = 4, }" # 4: Do Nothing
                if "-rgba.alpha" in value or "rgba.alpha" not in value:
                    fusion_effect_attribs["ToAlpha"] = "Input {Value = 4, }" # 4: Do Nothing

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
