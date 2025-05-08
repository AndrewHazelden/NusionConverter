import re
from nusion.model.node import Node

class Project:
    """
    This class will serve as the equivelent of a project file. A project
    file can contain multiple nodes, represented by the Node class. Node input
    and output connections are managed in this class.
    """

    def __init__(self, data):
        self.resolution = {"w": int(data["width"]), "h": int(data["height"])}
        self.raw_data = data["data"]

    def convert_copy_paste(self):
        raw_lines = self.raw_data.splitlines()
        for i, line in enumerate(raw_lines):
             if re.match(r"[A-Z]\w+\s\{", line):
                nuke_node = Node.from_nuke(raw_lines[i:], self.resolution)
                fusion_node = nuke_node.to_fusion()
                result = f"{{\n\tTools = ordered() {{\n\t\t{fusion_node.output()}\n\t}}\n}}"
                return(result)
