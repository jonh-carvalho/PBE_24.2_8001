from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class CalculadoraAreaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.base_input = TextInput(multiline=False)
        self.altura_input = TextInput(multiline=False)
        self.resultado_label = Label(text='Resultado:')
        calcular_button = Button(text='Calcular')
        calcular_button.bind(on_press=self.calcular_area)
        layout.add_widget(self.base_input)
        layout.add_widget(self.altura_input)
        layout.add_widget(calcular_button)
        layout.add_widget(self.resultado_label)
        return layout

    def calcular_area(self, instance):
        try:
            base = float(self.base_input.text)
            altura = float(self.altura_input.text)
            retangulo = Retangulo(base, altura)
            resultado = retangulo.calcular_area()
            self.resultado_label.text = f'A área é: {resultado}'
        except ValueError:
            self.resultado_label.text = 'Digite valores numéricos.'

if __name__ == '__main__':
    CalculadoraAreaApp().run()