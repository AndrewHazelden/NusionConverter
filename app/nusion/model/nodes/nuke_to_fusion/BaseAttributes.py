# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this files is named to match the Nuke node.

def convert(node):
    """ Convert Nuke Base Attributes to Fusion Base Attributes

    Returns:
        dict with fusion formatted base attributes
    """
    fusion_base_attribs = {}

    for knob in node.base_attribs:
        value = node.base_attribs[knob]

        if knob == "name":
            fusion_base_attribs['name'] = value

        if knob == "xpos" or knob == "ypos":
            fusion_base_attribs["Pos"] = \
                f"Pos = {{ {node.base_attribs['xpos']}, {node.base_attribs['ypos']} }}"

        if knob == "disable":
            fusion_base_attribs['PassThrough'] = f"PassThrough = {value}"

        if knob == "postage_stamp":
            fusion_base_attribs['ShowPic'] = f"Flags = {{ ShowPic = {value} }}"

        if knob == "tile_color":
            rgb = hex_to_rgb(value)
            fusion_base_attribs['TileColor'] = \
                f"TileColor = {{ R = {rgb[0]}, G = {rgb[1]}, B = {rgb[2]} }}"

        if knob == "note_font_color":
            rgb = hex_to_rgb(value)
            fusion_base_attribs['TextColor'] = \
                f"TextColor = {{ R = {rgb[0]}, G = {rgb[1]}, B = {rgb[2]} }}"

        if knob == "useLifetime" and value == "true":
            fusion_base_attribs['EnabledRegion'] = \
                f"EnabledRegion = TimeRegion {{ " \
                f"{{ Start = {node.base_attribs['lifetimeStart']}, " \
                f"End = {node.base_attribs['lifetimeEnd']}, }} }}"

    return fusion_base_attribs


def hex_to_rgb(hex_value):
    """ Convert hex colour to RGB(A).

     Returns:
        tuple with R,G,B,A values (between 0 and 1 for fusion)
    """
    h = hex_value.lstrip('0x')
    if len(h) > 6: #Contains alpha channel
        return tuple(round(int(h[i:i+2], 16)/255, 15) for i in (0, 2, 4, 6))
    else:
        return tuple(round(int(h[i:i+2], 16)/255, 15)  for i in (0, 2, 4))


if __name__ == '__main__':
    help(convert)
