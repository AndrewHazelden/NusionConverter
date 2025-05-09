"""
Configuration file
"""

NUKE_TO_FUSION_NODE_NAMES = {
    "Add": "ChannelBooleans",
    "AdjustBBox": "SetDomain",
    "Axis": "Locator3D",
    "Axis2": "Locator3D",
    "BackdropNode": "Underlay",
    "Blur": "Blur",
    "Card": "ImagePlane3D",
    "Card3D": "DVE",
    "Clamp": "BrightnessContrast",
    "ColorCorrect": "ColorCorrector",
    "ColorspaceGamut": "GamutConvert",
    "Constant": "Background",
    "Copy": "ChannelBoleans",
    "CopyBBox": "SetDomain",
    "Cube": "Shape3D",
    "Cylinder": "Shape3D",
    "Difference": "ChannelBoleans",
    "Divide": "ChannelBoleans",
    "Dot": "PipeRouter",
    "EdgeDetect": "Filter",
    "Expression": "Custom",
    "Framehold": "TimeStretcher",
    "GeometryExpression": "CustomVertex3D",
    "Grade": "ColorCorrector",
    "IDistort": "Displace",
    "Invert": "ChannelBoolean",
    "Keymix": "Dissolve",
    "Kronos": "Dimension.OpticalFlow",
    "Max": "ChannelBoolean",
    "Median": "RankFilter",
    "MergeExpression": "Custom",
    "MergeGeo": "Merge3D",
    "Min": "ChannelBoolean",
    "Minus": "ChannelBoolean",
    "Multiply": "ChannelBoolean",
    "NoOp": "PipeRouter",
    "Null": "PipeRouter",
    "ParticleExpression": "pCustom",
    "PositionToPoints": "ImagePlane3D",
    "Premult": "AlphaMultiply",
    "Radial": "Background",
    "Read": "Loader",
    "ReadGeo": "SurfaceFBXMesh",
    "Reconcile3D": "Camera3D",
    "Reformat": "BetterResize",
    "Retime": "Dimension.OpticalFlow",
    "ScanlineRender": "Renderer3D",
    "Scene": "Merge3D",
    "Shuffle": "ChannelBoolean",
    "Sphere": "Shape3D",
    "SphericalTransform": "PanoMap",
    "STMap": "Scale",
    "Text2": "TextPlus",
    "Tracker4": "Tracker",
    "Transform": "Transform",
    "TransformGeo": "Transform3D",
    "Unpremult": "AlphaDivide",
    "Write": "Saver",
    "WriteGeo": "ExporterFBX",
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
    "bdwidth",
    "bdheight",
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
    "Size",
    ]

FUSION_COLOR = [
    "TileColor",
    "TextColor",
    ]

FUSION_CLIP = [
    "Clip",
]