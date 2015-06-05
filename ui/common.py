from Tkinter import mainloop, Frame, Canvas, PhotoImage, Button
from utils import create_button
from exceptions import BaseException


class PhotoImageFrame(Frame):
    """ This class is a thin wrapper over the PhotoImage
    and Frame classes, so that it provides simplistic use and integration.
    """

    def __init__(self, *args, **kwargs):
        self.parent = kwargs.get('parent')
        pass


class ButtonsFrame(Frame):
    """
    This class' purpose is to hold a set of buttons and wrap them into a Frame.
    """
    def __init__(self, parent, **kwargs):
        Frame.__init__(self, parent)
        self.__parent = parent
        self.buttons = []
        try:
            for button in kwargs['buttons']:
                self.buttons.append(create_button(self.get_parent(), button))
        except BaseException:
            pass
        self.place_buttons()

    def place_buttons(self):
        for button in self.buttons:
            button.grid()
    def get_parent(self):
        return self.__parent