# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this file is named to match the Nuke node.

def convert(node):
    """ Convert Nuke Saturation to Fusion ColorCorrector

    Returns:
        dict with fusion formatted effect attributes.
    """

    fusion_effect_attribs = {}
    nuke_effect_attribs = node.effect_attribs

    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

        if knob == "saturation":
             fusion_effect_attribs["\t\t\tWheelSaturation1"] = f"Input {{ Value = {value}, }}"

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
