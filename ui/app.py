from Tkinter import Tk, Frame, BOTH

DEFAULT_GEOMETRY = '250x150+300+300'


class App(object):
    """
    The purpose of this class is to wrap the
    Tkinter pipeline into an intuitive application
    management class.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs: a dict that contain any kwargs,
            that will define the behaviour of the app.
        :return: An App object.
        """
        self.name = kwargs.get('name', 'SM_LAB')
        self.__root = Tk()
        self.main_frame = kwargs.get('root')
        if not self.main_frame:
            self.main_frame = BlankFrame(self.get_root(), **kwargs)
        self.__geometry = kwargs.get('geometry', DEFAULT_GEOMETRY)
        self.get_root().geometry(self.get_geometry())

    def run(self):
        """ Invoke this method to start the main loop of the app.
        """
        self.get_root().mainloop()

    def get_root(self):
        return self.__root

    def get_geometry(self):
        return self.__geometry


class BlankFrame(Frame):
    """
    This class is used to initialize the main window.
    """
    def __init__(self, parent, **kwargs):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack(fill=BOTH, expand=1)
