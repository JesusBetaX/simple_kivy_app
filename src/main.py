import os, sys, platform

from kivy import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.resources import resource_add_path, resource_find
from kivy.uix.screenmanager import ScreenManager

from app.home import Home
from app.login import Login


class KivyApp(App):
    session = {}

    def build(self):
        self.root = Builder.load_file("view/views.kv")
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Home(name='home'))

        return manager


if __name__ == '__main__':

    if platform.system() == 'Windows':
        os.environ['KIVY_GL_BACKEND'] = 'sdl2'  # 'glew' #angle_sdl2'
        Config.set('graphics', 'multisamples', '0')

    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))

    KivyApp().run()
