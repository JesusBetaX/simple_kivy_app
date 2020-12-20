import os, sys
from kivy.resources import resource_add_path, resource_find

from kivy.app import App
from kivy.lang import Builder
from kivy import Config
from kivy.uix.screenmanager import ScreenManager

from app.home import Home
from app.login import Login
from model.user import User

class KivyApp(App):
    user = User() 

    def build(self):
        self.root = Builder.load_file("view/views.kv")
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Home(name='home'))

        return manager

    # def get_application_config(self):
    #     if(not self.user.username):
    #         return super(KivyApp, self).get_application_config()
    #
    #     conf_directory = self.user_data_dir + '/' + self.user.username
    #
    #     if(not os.path.exists(conf_directory)):
    #         os.makedirs(conf_directory)
    #
    #     return super(KivyApp, self).get_application_config(
    #         '%s/config.cfg' % (conf_directory)
    #     )

if __name__ == '__main__':
    os.environ['KIVY_GL_BACKEND'] = 'sdl2'  # 'glew' #angle_sdl2'
    Config.set('graphics', 'multisamples', '0')

    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))

    KivyApp().run()