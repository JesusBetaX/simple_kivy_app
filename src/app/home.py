from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

class Home(Screen):

    def do_logout(self):
        app = App.get_running_app()
        print(app.session['user'])
        del app.session['user']

        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()