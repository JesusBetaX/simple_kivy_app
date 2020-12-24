from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

from model.user import User

class Login(Screen):

    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        user = User(username=loginText, password=passwordText)

        if user.valid():
            app.session['user'] = user

            self.ids['llogin'].text = "Login"
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'home'

        else:
            self.ids['llogin'].text = "Login (username or password incorrect)"


    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""