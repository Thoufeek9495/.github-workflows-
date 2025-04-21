# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from ai_coach_app import AICoach

class CoachUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)

        self.coach = AICoach()
        self.result_input = TextInput(hint_text="Enter result (3-18)", multiline=False, input_filter='int', font_size=24)
        self.result_display = Label(text="Awaiting input...", font_size=20)
        self.predict_btn = Button(text="Predict", on_press=self.predict_next, font_size=20)
        self.submit_btn = Button(text="Submit Result", on_press=self.submit_result, font_size=20)

        self.add_widget(self.result_input)
        self.add_widget(self.predict_btn)
        self.add_widget(self.submit_btn)
        self.add_widget(self.result_display)

    def predict_next(self, instance):
        prediction, confidence, number, reason = self.coach.predict_next()
        self.result_display.text = f"[PREDICTED] {prediction} | Number: {number} | Confidence: {confidence}%\n{reason}"

    def submit_result(self, instance):
        try:
            val = int(self.result_input.text)
            win, stake, round = self.coach.evaluate_result(val)
            summary = self.coach.get_summary()
            result = "✅ WIN!" if win else "❌ LOSS"
            self.result_display.text = f"{result} | Profit: ₹{summary['profit']} | Accuracy: {summary['accuracy']}%"
        except:
            self.result_display.text = "❌ Please enter a valid number between 3–18."

class RoyalWinAIApp(App):
    def build(self):
        return CoachUI()

if __name__ == '__main__':
    RoyalWinAIApp().run()
