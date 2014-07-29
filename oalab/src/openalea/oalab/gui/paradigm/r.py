# -*- python -*-
#
#       R Manager applet
# 
#       OpenAlea.OALab: Multi-Paradigm GUI
#
#       Copyright 2013 INRIA - CIRAD - INRA
#
#       File author(s): Julien Coste <julien.coste@inria.fr>
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################
__revision__ = ""

from openalea.oalab.editor.text_editor import RichTextEditor as Editor
from openalea.oalab.editor.highlight import Highlighter
from openalea.oalab.model.r import RModel
from openalea.oalab.service.help import display_help
from openalea.oalab.control.manager import control_dict
import types

class RModelController(object):
    default_name = RModel.default_name
    default_file_name = RModel.default_file_name
    pattern = RModel.pattern
    extension = RModel.extension
    icon = RModel.icon

    def __init__(self, name="", code="", model=None, filepath=None, interpreter=None, editor_container=None, parent=None):
        self.filepath = filepath
        if model is not None:
            self.model = model
        else:
            self.model = RModel(name=name, code=code, filepath=filepath)
        self.name = self.model.name
        self.parent = parent
        self.editor_container = editor_container
        self._widget = None

    def instanciate_widget(self):
        self._widget = Editor(parent=self.parent)
        wid = self._widget
        Highlighter(wid.editor)
        wid.applet = self

        # Add method to widget to display help
        def _diplay_help(widget):
            doc = widget.applet.model.get_documentation()
            display_help(doc)
        wid.display_help = types.MethodType(_diplay_help, wid)

        wid.set_text(self.model.code)
        wid.replace_tab()
        return wid

    def run_selected_part(self, *args, **kwargs):
        code = self.widget().get_selected_text()
        if len(code) == 0:
            code = """%%R
""" + self.widget().get_text()
        return self.model.run_code(code, *args, **kwargs)

    def run(self, *args, **kwargs):
        controls = control_dict()
        self.model.ns.update(controls)
        code = self.widget().get_text()
        self.model.code = code
        return self.model(*args, **kwargs)

    def step(self, *args, **kwargs):
        controls = control_dict()
        self.model.ns.update(controls)
        code = self.widget().get_text()
        self.model.code = code
        return self.model.step(*args, **kwargs)

    def stop(self, *args, **kwargs):
        return self.model.stop(*args, **kwargs)

    def animate(self, *args, **kwargs):
        controls = control_dict()
        self.model.ns.update(controls)
        code = self.widget().get_text()
        self.model.code = code
        return self.model.animate(*args, **kwargs)

    def init(self, *args, **kwargs):
        controls = control_dict()
        self.model.ns.update(controls)
        code = self.widget().get_text()
        self.model.code = code
        return self.model.init(*args, **kwargs)

    def widget(self):
        """
        :return: the edition widget
        """
        return self._widget
