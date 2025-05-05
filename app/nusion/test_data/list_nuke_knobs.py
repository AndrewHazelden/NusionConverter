# pylint: skip-file
"""
Run in nuke script editor to list all knobs on selected node.
"""

already_known_list = [
    "name",
    "xpos",
    "ypos",
    "disable",
    "postage_stamp",
    "tile_color",
    "note_font_color",
    "note_font_size",
    "useLifetime",
    "lifetimeStart",
    "lifetimeEnd",
    "mix",
    "channels",
    "label",
    "help",
    "dope_sheet",
    "hide_input",
    "onCreate",
    "updateUI",
    "rootNodeUpdated",
    "knobChanged",
    "note_font",
    "bookmark",
    "selected",
    "autolabel",
    "onDestroy",
    "indicators",
    "icon",
    "enable",
    "postage_stamp_frame",
    "panel",
    "cached",
    "gl_color"
    ]

for knob in nuke.selectedNode().knobs():
    if knob not in already_known_list:
        print(knob)