from traits.api import Int, HasTraits
from traitsui.api import View, Item


class App(HasTraits):
    value = Int()

    view = View(
        Item('value'),
        resizable=True,
        style='custom',
        width=0.5,
        height=0.5
    )

    def _value_default(self):
        return 42

    def _value_changed(self):
        print(self.value)
