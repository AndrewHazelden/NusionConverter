# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Nuke Axis2 to Fusion Locator3D

    Returns:
        dict with fusion formatted effect attributes.
    """

    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    # translate {X Y Z}
    # rotate {X Y Z}
    
    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
