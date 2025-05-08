# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Nuke common effect attributes to Fusion

    Returns:
        dict with fusion formatted common attributes.
    """
    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}
    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

        if knob == "mix":
            fusion_effect_attribs["\t\t\tBlend"] = f"Input {{ Value = {value}, }}"

        if knob == "channels":
            if value == "all":
                #Fusion only supports RGBA channel processing
                #TODO: Flag to user if there are any extra channels in the pipe.
                pass
            if value == "rgb":
                fusion_effect_attribs["\t\t\tProcessAlpha"] = "Input {Value = 0, }"
            if value == "alpha":
                fusion_effect_attribs["\t\t\tProcessRed"] = "Input {Value = 0, }"
                fusion_effect_attribs["\t\t\tProcessGreen"] = "Input {Value = 0, }"
                fusion_effect_attribs["\t\t\tProcessBlue"] = "Input {Value = 0, }"
            if value.startswith("{"): #individual channels selected
                fusion_effect_attribs["\t\t\tProcessAlpha"] = "Input {Value = 1, }"
                if "-rgba.red" in value:
                    fusion_effect_attribs["\t\t\tProcessRed"] = "Input {Value = 0, }"
                if "-rgba.green" in value:
                    fusion_effect_attribs["\t\t\tProcessGreen"] = "Input {Value = 0, }"
                if "-rgba.blue" in value:
                    fusion_effect_attribs["\t\t\tProcessBlue"] = "Input {Value = 0, }"
                if "-rgba.alpha" in value or "rgba.alpha" not in value:
                    fusion_effect_attribs["\t\t\tProcessAlpha"] = "Input {Value = 0, }"

        if knob == "label":
            fusion_effect_attribs["\t\t\tComments"] = f"Input {{ Value = {value}, }}"

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
