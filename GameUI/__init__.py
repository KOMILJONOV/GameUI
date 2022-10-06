from threading import Thread
import pygame as pg
from pygame._sdl2 import Window,Renderer
import signal




class GameUI(Window):
    def __init__(self, title:str="GameUI", size: tuple[int]=(640,480),resizeable:bool=True, position: tuple[int]=(0,0),render_fps:int=60, fullscreen:bool=False):
        super().__init__(title,size,position,fullscreen)
        self.resizable = resizeable
        self.render_fps = render_fps
        self.renderer = Renderer(self)
        self.clock = pg.time.Clock()
    
    def render(self):
        self.renderer.clear()
        # for x,y in self.dots:
        #     self.renderer.draw_color = (255,255,255,255)
        #     self.renderer.draw_point((x,y))
        #     self.renderer.draw_color = (0,0,0,0)
        self.renderer.present()
    
    def loop(self):
        while self.running:
            self.clock.tick(self.render_fps)
            self.render()
    
    def event_loop(self):
        while self.running:
            events = pg.event.get()

    
    def run(self):
        self.running = True
        self.render_thread = Thread(target=self.loop)
        self.render_thread.start()
        self.event_thread = Thread(target=self.event_loop)
        self.event_thread.start()
        signal.signal(signal.SIGINT,self.stop)
        self.render_thread.join()
        self.event_thread.join()
    

    def stop(self,*args):
        self.running = False