from Tkinter import Button


def create_button(parent, btn_tuple):
    btn_text = btn_tuple[0]
    btn_command = btn_tuple[1]
    return Button(master=parent, text=btn_text, command=btn_command)
