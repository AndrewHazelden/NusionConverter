# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Nuke BackDropNode to Fusion Underlay

    Returns:
        dict with fusion formatted effect attributes.
    """

    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    # label "content"
    # note_font_size 38
    # bdwidth 331
    # bdheight 436

    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

        if value == "label":
            fusion_effect_attribs["\t\t\Comments"] = "Input { Value = '{value}', }"

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
