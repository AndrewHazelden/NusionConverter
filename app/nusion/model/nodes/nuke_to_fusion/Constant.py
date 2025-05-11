# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Constant to Fusion Background

    Returns:
        dict with fusion formatted effect attributes.
    """

    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

        if knob == "color":
            # color {0.151711 0.404132 0.704158 1}
            
            if value.startswith("{"): # Multiple channels
                split_value = value.replace("{", "").replace("}", "").split(" ")
                print("Color Values]")
                print(len(split_value))
                if len(split_value) >= 3:
                    fusion_effect_attribs["\t\t\tTopLeftRed"] = \
                        f"Input {{Value = {split_value[0]}, }}"
                    fusion_effect_attribs["\t\t\tTopLeftGreen"] = \
                        f"Input {{Value = {split_value[1]}, }}"
                    fusion_effect_attribs["\t\t\tTopLeftGreen"] = \
                        f"Input {{Value = {split_value[2]}, }}"
                if len(split_value) >= 4:
                    fusion_effect_attribs["\t\t\tTopLeftAlpha"] = \
                        f"Input {{Value = {split_value[3]}, }}"
            # channels {rgba.red rgba.green rgba.blue rgba.alpha}

    fusion_effect_attribs["\t\t\tUseFrameFormatSettings"] = f"Input {{Value = 1, }}"
    fusion_effect_attribs["\t\t\tWidth"] = f"Input {{Value = {node.root_width}, }}"
    fusion_effect_attribs["\t\t\tHeight"] = f"Input {{Value = {node.root_height}, }}"

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
