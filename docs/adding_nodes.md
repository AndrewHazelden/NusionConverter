# Add Support for New Nodes

One of Nusion's most powerful features is that you can add support for additional Nuke nodes with only a few small changes to the included Python scripts. This makes it possible to map any Nuke node to a corresponding Fusion native node, OpenFX plugin, FusionSDK plugin, DCTL, Fuse, or potentially to a custom Fusion macro.

## Create a new Node Entry

1. Start by creating a new Python script that has a filename prefix that matches the Nuke node name you want to add support for:

        app/nusion/model/nodes/nuke_to_fusion/<node-name>.py

For example, if the Nuke node name is "Write", then the Python script would be called "Write.py".

![New Nodes](images/new_nodes_py_script.png)

To make this task easier, there are existing node definition scripts in the "nuke_to_fusion" folder that you can copy and adapt.

![New Nodes](images/new_nodes_nuke_to_fusion_dir.png)

2. Nusion needs to be told to look for the newly added "&lt;node-name&gt;.py" python script. This is done by looking in the "nuke_to_fusion" folder and editing the "\_\_init\_\_.py" file. The file is located at:

        app/nusion/model/nodes/nuke_to_fusion/__init__.py

Start by adding the Nuke node name to the end of the import items on this line:

```py
from nusion.model.nodes.nuke_to_fusion import (
```
Also add the Nuke node name to the end of the items on this line:

```py
__all__ = (
```


![New Nodes](images/new_nodes_init.png)


3. Update the config.py file to define how the node names are mapped during the conversion process:

        app/nusion/model/config.py

Edit the "NUKE_TO_FUSION_NODE_NAMES = {" section to add the mapping from the original Nuke node name to the appropriate Fusion node name:

```py
"Write": "Saver",
```

![New Nodes](images/new_nodes_config.png)

## Update the HTML Docs

Finally, you can edit the Nusion Web app's HTML code to indicate the node is now a supported node type. The file is located at:

        app/templates/form.html

Look for the HTML code that starts on the line and then add your node to the list:

```html
<h2 class="uk-modal-title">Supported Nodes</h2>
```

![New Nodes](images/new_nodes_html.png)
