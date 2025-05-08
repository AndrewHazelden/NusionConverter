# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Nuke Transform to Fusion Transform

    Returns:
        dict with fusion formatted effect attributes.
    """

    nuke_effect_attribs = node.effect_attribs
    fusion_effect_attribs = {}

    fusion_effect_attribs["\t\t\tReferenceSize"] = "Input {Value = 1, }"
    fusion_effect_attribs["\t\t\tWidth"] = f"Input {{Value = {node.root_width}, }}"
    fusion_effect_attribs["\t\t\tHeight"] = f"Input {{Value = {node.root_height}, }}"

    shutter_offset = "None"

    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

        if knob == "rotate":
            fusion_effect_attribs["\t\t\tAngle"] = f"Input {{Value = {value}, }}"

        if knob == "scale":
            if value.startswith("{"): # Scale is not uniform.
                fusion_effect_attribs["\t\t\tUseSizeAndAspect"] = "Input {Value = 0, }"
                size_x, size_y = value.replace("{", "").replace("}", "").split(" ")
                fusion_effect_attribs["\t\t\tXSize"] = f"Input {{ Value = {size_x}, }}"
                fusion_effect_attribs["\t\t\tYSize"] = f"Input {{ Value = {size_y}, }}"
            else: # Scale is uniform.
                fusion_effect_attribs["\t\t\tSize"] = f"Input {{ Value = {value}, }}"

        if knob == "center":
            value = value.replace("{", "").replace("}", "").split(" ")
            nuke_center_x = float(value[0])
            nuke_center_y = float(value[1])
            fusion_center_x = nuke_center_x / node.root_width
            fusion_center_y = nuke_center_y / node.root_height
            fusion_effect_attribs["\t\t\tPivot"] = \
                f"Input {{Value = {{ {fusion_center_x}, {fusion_center_y} }}, }}"

        if knob == "translate":
            value = value.replace("{", "").replace("}", "").split(" ")
            nuke_translate_x = float(value[0])
            nuke_translate_y = float(value[1])
            fusion_translate_x = \
                ((node.root_width / 2) + nuke_translate_x) / node.root_width
            fusion_translate_y = \
               ((node.root_height / 2) + nuke_translate_y) / node.root_height
            fusion_effect_attribs["Center"] = \
                f"Input {{Value = {{ {fusion_translate_x}, {fusion_translate_y} }}, }}"

        if knob == "invert_matrix" and value == "true":
            fusion_effect_attribs["\t\t\tInvertTransform"] = "Input {Value = 1, }"

        if knob == "black_outside" and value == "false":
            fusion_effect_attribs["\t\t\tEdges"] = "Input {Value = 2, }"

        if knob == "filter":
            # These are the closest matching filters I could find between the packages.
            # TODO: Raise warning that it may not be 100%

            # Fusion FilterMethod list:
            #     0 - Nearest Neighbor
            #     1 - Box
            #     2 - Linear
            #     3 - Quadratic
            #     4 - Cubic
            #     5 - Catmull-Rom
            #     6 - Gaussian
            #     7 - Mitchell
            #     8 - Lanczos
            #     9 - Sinc
            #     10 - Bessel
            filter_selection = "None"

            if value in ("Impulse", "Keys"):
                filter_selection = "0"

            if value in "Cubic":
                filter_selection = "1"

            if value in ("Simon", "Rifman"):
                filter_selection = "5"

            if value in "Mitchell":
                filter_selection = "7"

            if value in ("Parzen", "Notch"):
                filter_selection = "6"

            if value in ("Lanczos4", "Lanczos6"):
                filter_selection = "8"

            if value in "Sinc4":
                filter_selection = "9"

            if filter_selection != "None":
                fusion_effect_attribs["\t\t\tFilterMethod"] = f"Input {{Value = {filter_selection}, }}"

        if knob == "motionblur":
            fusion_effect_attribs["\t\t\tMotionBlur"] = "Input {Value = 1, }"
            fusion_effect_attribs["\t\t\tQuality"] = f"Input {{ Value = {value}, }}"
            shutter_offset = "-1.0" # Nuke's default

        if knob == "shutteroffset":
            if value == "start":
                shutter_offset = "-1.0"

            if value == "end":
                shutter_offset = "1.0"

            if value == "centred":
                shutter_offset = "0"

        if knob == "shuttercustomoffset":
            shutter_offset = value

        if shutter_offset != "None":
            fusion_effect_attribs["\t\t\tCenterBias"] = f"Input {{Value = {shutter_offset}, }}"

        if knob == "shutter":
            shutter_degrees = float(value) * 360
            fusion_effect_attribs["\t\t\tShutterAngle"] = f"Input {{ Value = {shutter_degrees}, }}"

        if knob in ("skew", "skew_order"):
            # The default transform doesn't support this.
            #TODO: Add an additional node under the fusion transform to skew.
            pass

        if knob == "clamp":
            # The default transform doesn't support this.
            #TODO: Add an additional node under the fusion transform to clamp brightness.
            pass

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
