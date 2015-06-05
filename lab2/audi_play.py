# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *
import pygame
import tkFileDialog
from pydub import AudioSegment

class GUI:

	def __init__(self, parent):
		self.parent = parent
		self.init_ui()

	def init_ui(self):
		self.parent.title('Player')
		self.mainframe = Frame(self.parent, padding="30 30 30 30")
		self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		self.play = Button(self.mainframe, text='Play', command=pygame.mixer.music.play)
		self.play.grid(column=1, row=1, sticky=(N, W, E), padx=10)
		self.pause = Button(self.mainframe, text='Pause', command=pygame.mixer.music.pause)
		self.pause.grid(column=2, row=1, sticky=(N, W, E), padx=10)
		self.resume = Button(self.mainframe, text='Resume', command=pygame.mixer.music.unpause)
		self.resume.grid(column=3, row=1, sticky=(N, W, E), padx=10)
		self.stop = Button(self.mainframe, text='Stop', command=pygame.mixer.music.stop)
		self.stop.grid(column=4, row=1, sticky=(N, W, E), padx=10)
		self.open = Button(self.mainframe, text='Open File', command=self.open_file)
		self.open.grid(column=5, row=1, sticky=(N, W, E), padx=10)
		self.play_another_audio = Button(self.mainframe, text='Play another song', command=self.another_song)
		self.play_another_audio.grid(column=6, row=1, sticky=(N, W, E), padx=10)

	def open_file(self):
		try:
			filename = tkFileDialog.askopenfilename()
			self.init_sound(filename)
		except:
			pass

	def init_sound(self, filename):
		pygame.init()
		pygame.mixer.init()
		pygame.mixer.music.load(filename.encode('utf8'))

	def another_song(self):
		filename = tkFileDialog.askopenfilename()
		sound = AudioSegment.from_mp3(filename)
		sound.export("~/Desktop/music.wav", format="wav")
		if not pygame.mixer.init():
			pygame.mixer.init()
		snd1 = pygame.mixer.Sound("~/Desktop/music.wav")
		snd1.play()

if __name__ == '__main__':
	root = Tk()
	app = GUI(root)
	root.mainloop()