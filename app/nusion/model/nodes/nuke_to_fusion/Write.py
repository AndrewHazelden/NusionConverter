# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Nuke Write to Fusion Saver

    Returns:
        dict with fusion formatted effect attributes.
    """
    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

#         if knob == "file":
#             # This is masked by the BaseAttribute implementation
#             fusion_effect_attribs["Clip"] = f"Input {{ Value = Clip {{ Filename = '{value}', }} }}"
#         if knob == "_jpeg_quality":
#             fusion_effect_attribs["\t\t\t['JpegFormat.Quality']"] = f"Input {{ Value = {value}, }}"
#         if knob == "_jpeg_sub_sampling":
#             fusion_effect_attribs["\t\t\t['JpegFormat.ChromaSubsampling']"] = f"Input {{ Value = 1, }}"

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
