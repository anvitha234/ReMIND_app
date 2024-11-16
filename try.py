from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

kv = """
ScreenManager:
    MainScreen:
    MemoryTrainingScreen:
    MedicationScreen:

<MainScreen@Screen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        canvas.before:
            Color:
                rgba: 0.95, 0.95, 0.95, 1  # Light gray background
            Rectangle:
                pos: self.pos
                size: self.size

        # Header Section with Emergency Button
        BoxLayout:
            size_hint_y: 0.1
            padding: 10
            spacing: 10
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [15, 15, 15, 15]

            Label:
                text: "📍 Current Location"
                font_size: "18sp"
                color: 0, 0, 0, 1
                size_hint_x: 0.6

            Button:
                text: "🚨 Emergency"
                size_hint_x: 0.4
                background_color: 1, 0.3, 0.3, 1
                on_press: print('Emergency contacts notified')

        # Welcome and Status Section
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.15
            padding: 20
            spacing: 5
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [15, 15, 15, 15]

            Label:
                text: "Welcome Back, Harry!"
                font_size: "24sp"
                color: 0, 0, 0, 1
                bold: True

            Label:
                text: "Today is Monday, November 16, 2024"
                font_size: "16sp"
                color: 0.4, 0.4, 0.4, 1

        # Quick Actions Grid
        GridLayout:
            cols: 2
            size_hint_y: 0.25
            spacing: 10
            padding: 5

            # Memory Training Button
            Button:
                text: "🧠\\nMemory\\nTraining"
                background_color: 0.6, 0.3, 1, 1
                on_press: root.manager.current = 'memory_training'
                font_size: "18sp"
                halign: 'center'
                valign: 'middle'
                text_size: self.size
                padding: 10, 10

            # Medication Reminder
            Button:
                text: "💊\\nMedication\\nReminder"
                background_color: 0.3, 0.7, 1, 1
                on_press: root.manager.current = 'medication'
                font_size: "18sp"
                halign: 'center'
                valign: 'middle'
                text_size: self.size
                padding: 10, 10

        # Today's Schedule
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.4
            padding: 10
            spacing: 10
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [15, 15, 15, 15]

            Label:
                text: "Today's Schedule"
                font_size: "20sp"
                color: 0, 0, 0, 1
                size_hint_y: 0.2
                bold: True

            BoxLayout:
                orientation: 'vertical'
                spacing: 5

                BoxLayout:
                    spacing: 10
                    CheckBox:
                        size_hint_x: 0.1
                    Label:
                        text: "9:00 AM - Take morning medication"
                        color: 0, 0, 0, 1
                        text_size: self.size
                        halign: 'left'
                        valign: 'center'

                BoxLayout:
                    spacing: 10
                    CheckBox:
                        size_hint_x: 0.1
                    Label:
                        text: "10:30 AM - Memory training exercise"
                        color: 0, 0, 0, 1
                        text_size: self.size
                        halign: 'left'
                        valign: 'center'

                BoxLayout:
                    spacing: 10
                    CheckBox:
                        size_hint_x: 0.1
                    Label:
                        text: "2:00 PM - Video call with family"
                        color: 0, 0, 0, 1
                        text_size: self.size
                        halign: 'left'
                        valign: 'center'

        # Bottom Navigation
        BoxLayout:
            size_hint_y: 0.1
            spacing: 10
            padding: 5
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [15, 15, 15, 15]

            Button:
                text: "🏠\\nHome"
                background_normal: ''
                background_color: 0.6, 0.3, 1, 1
                on_press: root.manager.current = 'main'

            Button:
                text: "🎮\\nGames"
                background_normal: ''
                background_color: 0.3, 0.7, 1, 1

            Button:
                text: "👥\\nContacts"
                background_normal: ''
                background_color: 0.3, 0.7, 1, 1

            Button:
                text: "⚙️\\nSettings"
                background_normal: ''
                background_color: 0.3, 0.7, 1, 1

<MemoryTrainingScreen@Screen>:
    name: 'memory_training'
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        canvas.before:
            Color:
                rgba: 0.95, 0.95, 0.95, 1
            Rectangle:
                pos: self.pos
                size: self.size

        # Header
        BoxLayout:
            size_hint_y: 0.1
            padding: 10
            spacing: 10
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [15, 15, 15, 15]

            Button:
                text: "← Back"
                size_hint_x: 0.2
                on_press: root.manager.current = 'main'

            Label:
                text: "Memory Training"
                font_size: "20sp"
                bold: True
                color: 0, 0, 0, 1

        # Memory Games Grid
        GridLayout:
            cols: 2
            spacing: 10
            padding: 10

            Button:
                text: "🎴\\nCard Matching"
                font_size: "18sp"
                background_color: 0.6, 0.3, 1, 1

            Button:
                text: "🎯\\nPattern Recognition"
                font_size: "18sp"
                background_color: 0.3, 0.7, 1, 1

            Button:
                text: "📝\\nWord Association"
                font_size: "18sp"
                background_color: 0.3, 0.7, 1, 1

            Button:
                text: "🧩\\nPuzzle Solving"
                font_size: "18sp"
                background_color: 0.6, 0.3, 1, 1

<MedicationScreen@Screen>:
    name: 'medication'
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        canvas.before:
            Color:
                rgba: 0.95, 0.95, 0.95, 1
            Rectangle:
                pos: self.pos
                size: self.size

        # Header
        BoxLayout:
            size_hint_y: 0.1
            padding: 10
            spacing: 10
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [15, 15, 15, 15]

            Button:
                text: "← Back"
                size_hint_x: 0.2
                on_press: root.manager.current = 'main'

            Label:
                text: "Medication Schedule"
                font_size: "20sp"
                bold: True
                color: 0, 0, 0, 1

        # Medication List
        BoxLayout:
            orientation: 'vertical'
            padding: 10
            spacing: 10
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [15, 15, 15, 15]

            # Morning Medications
            Label:
                text: "Morning Medications"
                font_size: "18sp"
                color: 0, 0, 0, 1
                bold: True
                size_hint_y: None
                height: 40

            BoxLayout:
                spacing: 10
                size_hint_y: None
                height: 40
                CheckBox:
                    size_hint_x: 0.1
                Label:
                    text: "Donepezil - 1 tablet"
                    color: 0, 0, 0, 1
                    text_size: self.size
                    halign: 'left'
                    valign: 'center'

            # Evening Medications
            Label:
                text: "Evening Medications"
                font_size: "18sp"
                color: 0, 0, 0, 1
                bold: True
                size_hint_y: None
                height: 40

            BoxLayout:
                spacing: 10
                size_hint_y: None
                height: 40
                CheckBox:
                    size_hint_x: 0.1
                Label:
                    text: "Memantine - 1 tablet"
                    color: 0, 0, 0, 1
                    text_size: self.size
                    halign: 'left'
                    valign: 'center'
"""

class MainScreen(Screen):
    pass

class MemoryTrainingScreen(Screen):
    pass

class MedicationScreen(Screen):
    pass

class MemoryBoxApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    MemoryBoxApp().run()