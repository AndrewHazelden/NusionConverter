"""
Import all effects from the nodes folder to allow them to be easily called from
other scripts using the node's effect type attribute.
"""

from nusion.model.nodes.nuke_to_fusion import (
    BaseAttributes,
    CommonAttributes,
    Add,
    AdjustBBox,
    Axis,
    Axis2,
    BackdropNode,
    Blur,
    Card,
    Card3D,
    Clamp,
    ColorCorrect,
    ColorspaceGamut,
    Constant,
    Copy,
    CopyBBox,
    Cube,
    Cylinder,
    Difference,
    Divide,
    Dot,
    EdgeDetect,
    Expression,
    Framehold,
    GeometryExpression,
    Grade,
    IDistort,
    Invert,
    Keymix,
    Kronos,
    Max,
    Median,
    MergeExpression,
    MergeGeo,
    Min,
    Minus,
    Multiply,
    NoOp,
    Null,
    ParticleExpression,
    PositionToPoints,
    Premult,
    Radial,
    Read,
    ReadGeo,
    Reconcile3D,
    Reformat,
    Retime,
    Saturation,
    ScanlineRender,
    Scene,
    Shuffle,
    Sphere,
    SphericalTransform,
    StickyNote,
    STMap,
    Text2,
    Tracker4,
    Transform,
    TransformGeo,
    Unpremult,
    Write,
    WriteGeo,
)

__all__ = (
    "BaseAttributes",
    "CommonAttributes",
    "Add",
    "AdjustBBox",
    "Axis",
    "Axis2",
    "BackdropNode",
    "Blur",
    "Card",
    "Card3D",
    "Clamp",
    "ColorCorrect",
    "ColorspaceGamut",
    "Constant",
    "Copy",
    "CopyBBox",
    "Cube",
    "Cylinder",
    "Difference",
    "Divide",
    "Dot",
    "EdgeDetect",
    "Expression",
    "Framehold",
    "GeometryExpression",
    "Grade",
    "IDistort",
    "Invert",
    "Keymix",
    "Kronos",
    "Max",
    "Median",
    "MergeExpression",
    "MergeGeo",
    "Min",
    "Minus",
    "Multiply",
    "NoOp",
    "Null",
    "ParticleExpression",
    "PositionToPoints",
    "Premult",
    "Radial",
    "Read",
    "ReadGeo",
    "Reconcile3D",
    "Reformat",
    "Retime",
    "Saturation",
    "ScanlineRender",
    "Scene",
    "Shuffle",
    "Sphere",
    "SphericalTransform",
    "StickyNote",
    "STMap",
    "Tracker4",
    "Text2",
    "Transform",
    "TransformGeo",
    "Unpremult",
    "Write",
    "WriteGeo",
)

# Utility modules that shouldn't be treated as node converters
UTILITY_MODULES = {"BaseAttributes", "CommonAttributes"}

def convert(node):
    """Convert node based on its effect type"""
    base_attribs = BaseAttributes.convert(node)
    common_attribs = CommonAttributes.convert(node)
    
    if node.effect in __all__ and node.effect not in UTILITY_MODULES:
        # Use globals() to dynamically get the module by name
        converter = globals()[node.effect]
        return base_attribs, {**common_attribs, **converter.convert(node)}

    raise ValueError(f"Node effect '{node.effect}' not currently supported.")
