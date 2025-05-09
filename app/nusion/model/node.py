from nusion.model import config
from nusion.model.nodes import nuke_to_fusion

class Node():
    """
    Parent class for common methods and attributes between NukeNode and FusionNode
    child classes.
    """

    def __init__(self, effect, base_attribs, effect_attribs, resolution):
        self.effect = effect
        self.base_attribs = base_attribs
        self.effect_attribs = effect_attribs
        self.resolution = resolution
        self.root_width = resolution["w"]
        self.root_height = resolution["h"]
        self.name = base_attribs["name"]

    @staticmethod
    def from_nuke(node_string, resolution):
        """
        Add a node with nuke script formatting.
        Assumes there may be extra data at the end of the node string and filters it out.

        Returns:
            Node class with all attributes from nuke string input.
        """
        node_raw = Node.extract_node_from_nuke(node_string)
        effect = node_raw[0].replace(" {", "")
        base_attribs, effect_attribs = Node.get_nuke_attribs(node_raw)
        return NukeNode(effect, base_attribs, effect_attribs, resolution)

    @staticmethod
    def extract_node_from_nuke(node_string):
        """
        Parse nuke input to extract a single node.

        Returns:
            single_node (list)
        """
        single_node = []
        for line in node_string:
            single_node.append(line.strip())
            if line == "}\n":
                break
        return single_node

    @staticmethod
    def get_nuke_attribs(node_raw):
        """
        Extract and seperate node attributes into dicts from a raw node list.

        Returns:
            base_attribs (dict), effect_attribs (dict)
        """
        base_attribs = {}
        effect_attribs = {}
        effect = node_raw[0].replace(" {", "")
        for item in node_raw[1:-1]:
            attrib = item.split(" ")[0]
            # print(effect, attrib)
            if attrib not in config.NUKE_IGNORE_ATTRIBUTES:
                if attrib in config.NUKE_BASE_ATTRIBUTES:
                    base_attribs[attrib] = item.replace(attrib, "").strip()
                else:
                    effect_attribs[attrib] = item.replace(attrib, "").strip()
        return base_attribs, effect_attribs



class NukeNode(Node):

    def __init__(self, effect, base_attribs, effect_attribs, resolution):
        super().__init__(effect, base_attribs, effect_attribs, resolution)
        self.software = "nuke"


    def to_fusion(self):
        """
        Convert the nuke node class to a fusion node class.
        """
        if self.software != "nuke":
            raise ValueError("Expected node from 'nuke' got '{}' instead".format(self.software))

        converted_base_attribs, converted_effect_attribs = nuke_to_fusion.convert(self)
        converted_effect = config.NUKE_TO_FUSION_NODE_NAMES[self.effect]
        return FusionNode(converted_effect, \
            converted_base_attribs, \
            converted_effect_attribs, \
            self.resolution)



class FusionNode(Node):

    def __init__(self, effect, base_attribs, effect_attribs, resolution):
        super().__init__(effect, base_attribs, effect_attribs, resolution)
        self.software = "fusion"

    def output(self):
        """
        Output the node in Fusion formatting.
        """
        output_effect_attribs = ""
        output_base_attribs = ""
        output_viewinfo_attribs = ""
        output_clip_attribs = ""
        output_color_attribs = ""
        output_nameset_attribs = ""
        for i, effect in enumerate(self.effect_attribs):
            output_effect_attribs += f"\t{effect} = {self.effect_attribs[effect]},"
            if i != len(self.effect_attribs)-1:
                #Add newline character if this is not the last effect attribute.
                output_effect_attribs += "\n"
        for i, attrib in enumerate(self.base_attribs):
            if attrib == "name":
                pass
            else:
                if attrib in config.FUSION_VIEWINFO:
                    output_viewinfo_attribs += f"{self.base_attribs[attrib]},\n"
                elif attrib in config.FUSION_CLIP:
                    output_clip_attribs += f"{self.base_attribs[attrib]},\n"
                elif attrib in config.FUSION_COLOR:
                    output_color_attribs += f"{self.base_attribs[attrib]},\n"
                else:
                    output_base_attribs += f"{self.base_attribs[attrib]},\n"

        if output_effect_attribs:
            output_effect_attribs = f"\t\t\tInputs = {{\n{output_effect_attribs}\n\t\t\t}},"
        if output_viewinfo_attribs:
            if self.effect == "Underlay":
                output_viewinfo_attribs = f"\t\t\tViewInfo = UnderlayInfo {{\n{output_viewinfo_attribs}\n\t\t\t}},"
            elif self.effect == "Note":
                output_viewinfo_attribs = f"\t\t\tViewInfo = StickyNoteInfo {{\n{output_viewinfo_attribs}\n\t\t\t}},"
            else:
                output_viewinfo_attribs = f"\t\t\tViewInfo = OperatorInfo {{\n{output_viewinfo_attribs}\n\t\t\t}},"
        if output_clip_attribs:
            output_clip_attribs = f"\t\tClips = {{\n{output_clip_attribs}\n\t\t}},"
        if output_color_attribs:
            output_color_attribs = f"\t\tColors = {{\n{output_color_attribs}\n\t\t}},"
        if self.effect == "Loader" or self.effect == "Saver":
            output_nameset_attribs = f"\t\t\tNameSet = true,\n"
        node_output = f"{self.name} = {self.effect} {{\n" \
                        f"{output_nameset_attribs}\n" \
                        f"{output_base_attribs}\n" \
                        f"{output_effect_attribs}\n" \
                        f"{output_viewinfo_attribs}\n" \
                        f"{output_clip_attribs}\n" \
                        f"{output_color_attribs}\n" \
                        f"}}"

        # Cleanup any empty lines caused by rogue newline character
        # being moved to the wrong place. Feels like unnecessary double parsing.
        # TODO: Not do this.
        lines = node_output.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]
        node_output = ""
        for i, line in enumerate(non_empty_lines):
            node_output += line
            if i != len(non_empty_lines)-1:
                node_output += "\n" #Add newline character if this is not the last line.

        return node_output
