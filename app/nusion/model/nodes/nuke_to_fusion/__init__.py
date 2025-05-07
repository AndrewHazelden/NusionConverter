"""
Import all effects from the nodes folder to allow them to be easily called from
other scripts using the node's effect type attribute.
"""

from nusion.model.nodes.nuke_to_fusion import (
    BaseAttributes,
    CommonAttributes,
    Blur,
    ColorCorrect,
    Transform,
    Invert,
    Premult,
    Unpremult,
    Write,
    Dot,
)

__all__ = (
    "BaseAttributes",
    "CommonAttributes",
    "Blur",
    "ColorCorrect",
    "Transform",
    "Invert",
    "Premult",
    "Unpremult",
    "Write",
    "Dot",
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
