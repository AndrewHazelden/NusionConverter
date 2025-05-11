# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Nuke Sphere to Fusion Shape3D

    Returns:
        dict with fusion formatted effect attributes.
    """

    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

        if knob == "rotate":
            # rotate {45 45 0}

            if value.startswith("{"): # Multiple channels
                split_value = value.replace("{", "").replace("}", "").split(" ")
                # print("Rotation Values]")
                # print(len(split_value))
                if len(split_value) == 3:
                    fusion_effect_attribs["\t\t\t['Transform3DOp.Rotate.X']"] = \
                        f"Input {{Value = {split_value[0]}, }}"
                    fusion_effect_attribs["\t\t\t['Transform3DOp.Rotate.Y']"] = \
                        f"Input {{Value = {split_value[1]}, }}"
                    fusion_effect_attribs["\t\t\t['Transform3DOp.Rotate.Z']"] = \
                        f"Input {{Value = {split_value[2]}, }}"

    fusion_effect_attribs["\t\t\t['Shape']"] = f"Input {{ Value = FuID {{ 'SurfaceSphereInputs' }}, }}"

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
