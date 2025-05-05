# pylint: disable=invalid-name, missing-module-docstring
# Disable pylint invalid name warning as this file is named to match the Nuke node.

def convert(node):
    """ Convert Nuke ColorCorrect to Fusion ColorCorrector

    Returns:
        dict with fusion formatted effect attributes.
    """
    fusion_effect_attribs = {}
    nuke_effect_attribs = node.effect_attribs

    for knob in nuke_effect_attribs:
        value = nuke_effect_attribs[knob]

        if knob == "gain":
            if value.startswith("{"): # Multiple channels
                split_value = value.replace("{", "").replace("}", "").split(" ")
                fusion_effect_attribs["MasterRedGain"] = \
                    f"Input {{Value = {split_value[0]}, }}"
                fusion_effect_attribs["MasterGreenGain"] = \
                    f"Input {{Value = {split_value[1]}, }}"
                fusion_effect_attribs["MasterBlueGain"] = \
                    f"Input {{Value = {split_value[2]}, }}"
            else: #Master channel
                fusion_effect_attribs["MasterRGBGain"] = \
                    f"Input {{Value = {value}, }}"

        if ".gain" in knob:
            #TODO: Raise warning about ranges curve making this conversion not 100% accurate.
            fusion_knob = knob.split(".")[0].capitalize()
            if fusion_knob == "Midtones":
                fusion_knob = "MidTones" #Exception for Fusion's weird capitalisation
            if value.startswith("{"): # Multiple channels
                split_value = value.replace("{", "").replace("}", "").split(" ")
                fusion_effect_attribs[f"{fusion_knob}RedGain"] = \
                    f"Input {{Value = {split_value[0]}, }}"
                fusion_effect_attribs[f"{fusion_knob}GreenGain"] = \
                    f"Input {{Value = {split_value[1]}, }}"
                fusion_effect_attribs[f"{fusion_knob}BlueGain"] = \
                    f"Input {{Value = {split_value[2]}, }}"
            else: #Master channel
                fusion_effect_attribs[f"{fusion_knob}RGBGain"] = \
                    f"Input {{Value = {value}, }}"

        if knob == "gamma":
            if value.startswith("{"): # Multiple channels
                split_value = value.replace("{", "").replace("}", "").split(" ")
                fusion_effect_attribs["MasterRedGamma"] = \
                    f"Input {{Value = {split_value[0]}, }}"
                fusion_effect_attribs["MasterGreenGamma"] = \
                    f"Input {{Value = {split_value[1]}, }}"
                fusion_effect_attribs["MasterBlueGamma"] = \
                    f"Input {{Value = {split_value[2]}, }}"
            else: #Master channel
                fusion_effect_attribs["MasterRGBGamma"] = \
                    f"Input {{Value = {value}, }}"

        if ".gamma" in knob:
            #TODO: Raise warning about ranges curve making this conversion not 100% accurate.
            fusion_knob = knob.split(".")[0].capitalize()
            if fusion_knob == "Midtones":
                fusion_knob = "MidTones" #Exception for Fusion's weird capitalisation
            if value.startswith("{"): # Multiple channels
                split_value = value.replace("{", "").replace("}", "").split(" ")
                fusion_effect_attribs[f"{fusion_knob}RedGamma"] = \
                    f"Input {{Value = {split_value[0]}, }}"
                fusion_effect_attribs[f"{fusion_knob}GreenGamma"] = \
                    f"Input {{Value = {split_value[1]}, }}"
                fusion_effect_attribs[f"{fusion_knob}BlueGamma"] = \
                    f"Input {{Value = {split_value[2]}, }}"
            else: #Master channel
                fusion_effect_attribs[f"{fusion_knob}RGBGamma"] = \
                    f"Input {{Value = {value}, }}"

        if knob == "offset":
            if value.startswith("{"): # Multiple channels
                split_value = value.replace("{", "").replace("}", "").split(" ")
                fusion_effect_attribs["MasterRedBrightness"] = \
                    f"Input {{Value = {split_value[0]}, }}"
                fusion_effect_attribs["MasterGreenBrightness"] = \
                    f"Input {{Value = {split_value[1]}, }}"
                fusion_effect_attribs["MasterBlueBrightness"] = \
                    f"Input {{Value = {split_value[2]}, }}"
            else: #Master channel
                fusion_effect_attribs["MasterRGBBrightness"] = \
                    f"Input {{Value = {value}, }}"

        if ".offset" in knob:
            #TODO: Raise warning about ranges curve making this conversion not 100% accurate.
            fusion_knob = knob.split(".")[0].capitalize()
            if fusion_knob == "Midtones":
                fusion_knob = "MidTones" #Exception for Fusion's weird capitalisation
            if value.startswith("{"): # Multiple channels
                split_value = value.replace("{", "").replace("}", "").split(" ")
                fusion_effect_attribs[f"{fusion_knob}RedBrightness"] = \
                    f"Input {{Value = {split_value[0]}, }}"
                fusion_effect_attribs[f"{fusion_knob}GreenBrightness"] = \
                    f"Input {{Value = {split_value[1]}, }}"
                fusion_effect_attribs[f"{fusion_knob}BlueBrightness"] = \
                    f"Input {{Value = {split_value[2]}, }}"
            else: #Master channel
                fusion_effect_attribs[f"{fusion_knob}RGBBrightness"] = \
                    f"Input {{Value = {value}, }}"

    #Match nuke default process order (Gamma before levels)
    fusion_effect_attribs["ProcessOrder"] = "Input { Value = 0, }"

    #Match nuke default Ranges curve
    fusion_effect_attribs["ColorRanges"] = \
            "Input { Value = ColorCurves " \
            "{ Curves = { " \
            "{ Points = { { 0, 1 }, { 0.0288, 0.9956 }, { 0.0611, 0 }, { 0.09, 0 } } }, " \
            "{ Points = { { 0.5, 0 }, { 0.6772, 0 }, { 0.8189, 1 }, { 1, 1 } } } } }, }"

    return fusion_effect_attribs

if __name__ == '__main__':
    help(convert)
