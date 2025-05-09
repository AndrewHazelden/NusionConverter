# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Nuke Text2 to Fusion TextPlus

    Returns:
        dict with fusion formatted effect attributes.
    """

    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

        if knob == "message":
            fusion_effect_attribs["\t\t\t['StyledText']"] = f"Input {{ Value = '{value}', }}"

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
