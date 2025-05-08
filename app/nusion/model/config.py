"""
Configuration file
"""

NUKE_TO_FUSION_NODE_NAMES = {
    "Blur": "Blur",
    "ColorCorrect": "ColorCorrector",
    "Invert": "ChannelBoolean",
    "Premult": "AlphaMultiply",
    "Transform": "Transform",
    "Unpremult": "AlphaDivide",
    "Write": "Saver",
    "Read": "Loader",
    "Dot": "PipeRouter",
    }

#Invert NUKE_TO_FUSION dict
FUSION_TO_NUKE_NODE_NAMES = {v: k for k, v in NUKE_TO_FUSION_NODE_NAMES.items()}

############
### NUKE ###
############

NUKE_BASE_ATTRIBUTES = [
    "name",
    "disable",
    "xpos",
    "ypos",
    "note_font_color",
    "note_font",
    "note_font_size",
    "tile_color",
    "gl_color",
    "process_mask",
    "maskFrom",
    "maskChannelMask",
    "maskChannelInput",
    "maskChannel",
    "Mask",
    "mask",
    "invert_mask",
    "postage_stamp_frame",
    "postage_stamp",
    "useLifetime",
    "lifetimeStart",
    "lifetimeEnd",
    "file",
    ]

NUKE_IGNORE_ATTRIBUTES = [
    "selected",
    "channel", #duplicate of "channels"
    ]

##############
### FUSION ###
##############

FUSION_VIEWINFO = [
    "Pos",
    "ShowPic",
    ]

FUSION_COLOR = [
    "TileColor",
    "TextColor",
    ]

FUSION_CLIP = [
    "Clip",
]