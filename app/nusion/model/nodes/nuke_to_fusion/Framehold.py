# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Nuke Framehold to Fusion TimeStretcher

    Returns:
        dict with fusion formatted effect attributes.
    """

    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    # No attributes on this node other than channels which is converted in CommonAttributes.

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
