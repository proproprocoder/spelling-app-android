import random
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import platform
from plyer import tts
from plyer import filechooser

# Set window size for desktop testing to mimic mobile
if platform not in ('android', 'ios'):
    Window.size = (400, 700)

class SpellingApp(App):
    def build(self):
        self.words = []
        self.used_words = []
        self.current_word = None
        
        # Main Layout
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Heading
        self.label_status = Label(
            text="Load a file to start", 
            font_size='24sp', 
            bold=True,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.label_status)
        
        # Word Display (Hidden initially)
        self.label_word = Label(
            text="", 
            font_size='32sp', 
            bold=True, 
            color=(0.2, 0.6, 1, 1),
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.label_word)
        
        # Buttons Layout
        buttons_layout = BoxLayout(orientation='vertical', spacing=15, size_hint=(1, 0.6))
        
        # Load File Button
        self.btn_load = Button(
            text="📂 Load Words File",
            font_size='20sp',
            background_color=(0.5, 0.5, 0.5, 1),
            on_press=self.load_file
        )
        buttons_layout.add_widget(self.btn_load)

        # Hear Button
        self.btn_play = Button(
            text="▶ Hear New Word",
            font_size='20sp',
            background_color=(0.1, 0.45, 0.9, 1),
            on_press=self.play_new_word,
            disabled=True
        )
        buttons_layout.add_widget(self.btn_play)
        
        # Replay Button
        self.btn_replay = Button(
            text="🔁 Replay",
            font_size='20sp',
            background_color=(0.9, 0.7, 0, 1),
            on_press=self.replay_word,
            disabled=True
        )
        buttons_layout.add_widget(self.btn_replay)
        
        # Show Button
        self.btn_show = Button(
            text="👁 Show Word",
            font_size='20sp',
            background_color=(0.2, 0.7, 0.3, 1),
            on_press=self.show_word,
            disabled=True
        )
        buttons_layout.add_widget(self.btn_show)
        
        self.layout.add_widget(buttons_layout)
        
        # Try to load default words.txt if exists
        if os.path.exists("words.txt"):
            self.load_words_from_path("words.txt")
            
        return self.layout

    def load_file(self, instance):
        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        if selection:
            self.load_words_from_path(selection[0])

    def load_words_from_path(self, path):
        try:
            with open(path, "r") as f:
                self.words = [line.strip() for line in f if line.strip()]
            random.shuffle(self.words)
            self.used_words = []
            self.current_word = None
            self.label_status.text = f"Loaded {len(self.words)} words"
            self.enable_buttons()
        except Exception as e:
            self.label_status.text = "Error loading file"

    def enable_buttons(self):
        self.btn_play.disabled = False
        self.btn_replay.disabled = True # Can't replay until played once
        self.btn_show.disabled = True   # Can't show until played once

    def get_next_word(self):
        if not self.words:
            if self.used_words:
                self.words = self.used_words
                self.used_words = []
                random.shuffle(self.words)
                self.label_status.text = "Restarting list..."
            else:
                self.label_status.text = "No words loaded."
                return None
        
        self.current_word = random.choice(self.words)
        self.words.remove(self.current_word)
        self.used_words.append(self.current_word)
        return self.current_word

    def play_new_word(self, instance):
        word = self.get_next_word()
        if word:
            self.label_word.text = "" # Hide word
            self.label_status.text = "Listen..."
            self.speak_word(word)
            self.btn_replay.disabled = False
            self.btn_show.disabled = False

    def replay_word(self, instance):
        if self.current_word:
            self.speak_word(self.current_word)

    def speak_word(self, word):
        try:
            tts.speak(word)
        except NotImplementedError:
            # Fallback for desktop testing where plyer.tts might not be fully supported
            print(f"Speaking: {word}")
            self.label_status.text = f"Speaking: {word} (TTS unavailable)"

    def show_word(self, instance):
        if self.current_word:
            self.label_word.text = self.current_word
            self.label_status.text = "This text is:"

if __name__ == "__main__":
    SpellingApp().run()