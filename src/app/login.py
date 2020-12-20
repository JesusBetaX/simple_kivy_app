from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

class Login(Screen):
    
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.user.username = loginText
        app.user.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'home'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""