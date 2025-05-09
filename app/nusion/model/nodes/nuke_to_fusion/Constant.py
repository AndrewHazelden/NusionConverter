# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Constant to Fusion Background

    Returns:
        dict with fusion formatted effect attributes.
    """

    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    fusion_effect_attribs["\t\t\tUseFrameFormatSettings"] = f"Input {{Value = 1, }}"
    fusion_effect_attribs["\t\t\tWidth"] = f"Input {{Value = {node.root_width}, }}"
    fusion_effect_attribs["\t\t\tHeight"] = f"Input {{Value = {node.root_height}, }}"

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
