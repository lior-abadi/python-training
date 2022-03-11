import random
from turtle import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
import json, glob
from datetime import datetime
from pathlib import Path

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    
    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
            if uname in users and users[uname]["password"] == pword:
                print("Login Successful")
                self.manager.current = "login_screen_success"
            else: 
                self.ids.login_feedback.text = "Wrong username or password!"
        

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {"username": uname, "password": pword,
                        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("users.json", "w") as file:
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"  

class SignUpScreenSuccess(Screen):
    def go_to_login_screen(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class SignUpScreenSuccess(Screen):
    def go_to_login_screen(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
        
class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    
    def pick_mood(self, mood):
        available_feeligns = glob.glob("quotes/*txt")
        available_feeligns = [Path(filename).stem for filename in available_feeligns]
        if str(mood).lower() in available_feeligns:
            with open(f"quotes/{str(mood).lower()}.txt", encoding= "utf8") as file:
                quotes = file.readlines()
            self.ids.mood_feedback.text = random.choice(quotes)
        else:
            self.ids.mood_feedback.text = "Mood not available yet, try another one!"    
                


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()