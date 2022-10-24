import sys
from threading import Thread
from time import sleep
import pygame as pg
from pygame._sdl2 import Window,Renderer
import signal
import random







class GameUI(Window):
    threads: list[Thread] = []
    def __init__(self, title:str="GameUI", size: tuple[int]=(640,480),resizeable:bool=True, position: tuple[int]=(100,100),render_fps:int=60, fullscreen:bool=False):
        super().__init__(title,size,position,fullscreen)
        self.resizable = resizeable
        self.render_fps = render_fps
        self.renderer = Renderer(self)
    
    def render(self):
        self.renderer.clear()

        self.renderer.present()

    
    def loop(self):
        while self.running:
            self.render()
    
    def event_loop(self):
        while self.running:
            events = pg.event.get()
    

    def onclick(self):
        for i in range(100):
            print(i)
            sleep(0.1)

    
    def run(self):
        self.running = True
        self.render_thread = Thread(target=self.loop,daemon=True)
        self.render_thread.start()
        signal.signal(signal.SIGINT, self.stop)
        while self.running:
            event = pg.event.wait()
            # for event in events:
            if event.type == pg.QUIT:
                # self.running = False
                self.stop()
            if event.type == pg.MOUSEBUTTONUP:
                thread = Thread(target=self.onclick)
                thread.setDaemon(True)
                self.threads.append(thread)
                thread.start()

    

    def stop(self,*args):
        self.running = False
        for thread in self.threads:
            thread.stop()
        pg.quit()
        sys.exit(0)