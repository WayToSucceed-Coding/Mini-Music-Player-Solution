from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class MiniMusicApp(App):
    def build(self):
        Window.size = (800,600)
        self.title = "Mini Music Player"
        
        layout = FloatLayout()

        bg = Image(source='background.png', allow_stretch=True, keep_ratio=False,
                   size=Window.size, pos=(0,0))
        layout.add_widget(bg)

        sound = SoundLoader.load('song.mp3')

        btn_layout = BoxLayout(orientation='horizontal', size_hint=(0.3,0.2),
                               pos_hint={'center_x':0.5,'center_y':0.5}, spacing=20)
        layout.add_widget(btn_layout)

        play_btn = Button(background_normal = "play.png", border = (0,0,0,0), background_down = "play_pressed.png")
        stop_btn = Button(background_normal = "stop.png", border = (0,0,0,0), background_down = "stop_pressed.png")
        
        play_btn.bind(on_press = lambda x: sound.play() if sound else None)
        stop_btn.bind(on_press = lambda x: sound.stop() if sound else None)

        btn_layout.add_widget(play_btn)
        btn_layout.add_widget(stop_btn)

        return layout
        
MiniMusicApp().run()

