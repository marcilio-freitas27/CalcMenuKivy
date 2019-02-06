import kivy
import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_string("""
<Button@Button>:
    font_size:32
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding:0
        spacing:20
        canvas:
            Color:
                rgb: (0,1,1)
            Rectangle:
                size: self.size
                pos: self.pos
        Label:
            text: '[b]Bem vindos ao MiniCalc![/b]'
            markup: True
            font_size: 55
            color: (0,0,1,1)
        AnchorLayout:
            Button:
                text: 'Go calc!'
                on_release: root.manager.current = 'settings'
                background_color:[0,0,1,1]                
                font_size: 50
                size_hint_y: 0.5
                size_hint_x: 0.5
        AnchorLayout:
            Button:
                text: 'Sair'
                on_release: root.manager.current = 'quit'
                background_color:[0,0,1,1]
                font_size: 50
                size_hint_y: 0.5
                size_hint_x: 0.5
        AnchorLayout:
            Button:
                text: 'Sobre'
                on_release: root.manager.current = 'about'
                background_color:[0,0,1,1]
                font_size: 50
                size_hint_y: 0.5
                size_hint_x: 0.5
<SettingsScreen>:
    GridLayout:
        rows:10
        orientation: 'vertical'
        padding:0
        spacing:20
        canvas:
            Color:
                rgb: (1,1,1)
            Rectangle:
                size: self.size
                pos: self.pos
        ActionBar:
            ActionView:
                canvas:
                    Color:
                        rgb: (0.5, 0.5 , 0.5)
                    Rectangle:
                        size: self.size
                        pos: self.pos
                ActionPrevious:
                    title:'Calc'
                    on_release:app.root.current = 'menu'
                ActionGroup:
                    mode: 'spinner'
                    ActionButton:
                        text: 'Sobre'
                        on_release: root.manager.current = 'about'
                ActionSeparator:
                    background_image: ''
                ActionButton:
                    minimum_width: '200sp'
                    text:'Sair'
                    on_release:root.manager.current = 'quit'
                ActionSeparator:
                    background_image: ''
        TextInput:
            text: ' '
            id: l
            font_size: 50
            color: (0,0,0,1)
        BoxLayout:
            spacing: 10
            Button:
                text: "7"
                on_release: l.text += self.text
                background_color:[0,1,0,1]
            Button:
                text: "8"
                on_release: l.text += self.text
                background_color:[0,1,0,1]
            Button:
                text: "9"
                on_release: l.text += self.text
                background_color:[0,1,0,1]
            Button:
                text: ":"
                on_release: l.text += '/'
                background_color:[0,1,0,1]
        BoxLayout:
            spacing: 10
            Button:
                text: "4"
                on_release: l.text += self.text
                background_color:[0,1,0,1]
            Button:
                text: "5"
                on_release: l.text += self.text
                background_color:[0,1,0,1]
            Button:
                text: "6"
                on_release: l.text += self.text
                background_color:[0,1,0,1]
            Button:
                text: "-"
                on_release: l.text += '-'
                background_color:[0,1,0,1]
        BoxLayout:
            spacing: 10
            Button:
                text: "1"
                on_release: l.text += self.text
                background_color:[0,1,0,1]
            Button:
                text: "2"
                on_release: l.text += self.text
                background_color:[0,1,0,1]
            Button:
                text: "3"
                on_release: l.text += self.text
                background_color:[0,1,0,1]
            Button:
                text: "x"
                on_release: l.text += '*'
                background_color:[0,1,0,1]
        BoxLayout:
            spacing: 10
            Button:
                text: "0"
                on_release: l.text += self.text
                background_color:[0,1,0,1]
            Button:
                text: "="
                on_release: l.text = str(eval(l.text))
                background_color:[0,1,0,1]
            Button:
                text: "AC"
                on_release: l.text = ''
                background_color:[1,0,0,1]
            Button:
                text: "+"
                on_release: l.text += '+'
                background_color:[0,0,0,1]
<Quit>:
    BoxLayout:
        orientation:'vertical'
        padding:200
        spacing:20
        canvas:
            Color:
                rgb: (1,0.5,0)
            Rectangle:
                size: self.size
                pos: self.pos
        Label:
            text: '[b]Quer mesmo sair?[/b]'
            markup: True
            font_size: 65
            color: (1,0,0,1)
        AnchorLayout:
            Button:
                text: 'Yes'
                font_size : 50
                background_color:[1,0.5,0,0.5]
                on_release: root.sair(self)
                size_hint_y: 0.75
                size_hint_x: 0.75
        AnchorLayout:
            Button:
                text: 'No'
                font_size : 50
                background_color:[1,0.5,0,0.5]
                on_release: root.manager.current = 'menu'
                size_hint_y: 0.75
                size_hint_x: 0.75
<Sobre>:
    BoxLayout:
        orientation:'vertical'
        padding:0
        spacing:0
        canvas:
            Color:
                rgb: (0,0,1)
            Rectangle:
                size: self.size
                pos: self.pos
        ActionBar:
            ActionView:
                canvas:
                    Color:
                        rgb: (0, 0, 0.5)
                    Rectangle:
                        size: self.size
                        pos: self.pos
                ActionPrevious:
                    title:'Info'
                    on_release:app.root.current = 'menu'
                ActionGroup:
                    mode: 'spinner'
                    ActionButton:
                        text: 'Calc'
                        on_release: root.manager.current = 'settings'
                ActionSeparator:
                    background_image: ''
                ActionButton:
                    minimum_width: '200sp'
                    text:'Sair'
                    on_release:root.manager.current = 'quit'
                ActionSeparator:
                    background_image: ''
        ScrollView:
            Label:
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text: 'MiniCalc v1.0.0 é um simples app feito com a linguagem Python e o framework Kivy.'
                font_size: 50
""")

app = App()
# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class Quit(Screen):
    def sair(self, obj):
        app.stop()
        os._exit(0)

class Sobre(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Quit(name='quit'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(Sobre(name='about'))

class TestApp(App):
    def build(self):
        return sm

TestApp().run()
