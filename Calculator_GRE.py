#! python3
import random

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

from kivy.core.clipboard import Clipboard

# global variables
memory = '0'
current_equation = ''
main_display_text = '0'


class CalculatorDisplay(Label):
	def on_size(self, *args):
		self.canvas.before.clear()
		with self.canvas.before:
			Color(1, 1, 1, 1)
			Rectangle(pos=self.pos, size=self.size, size_hint_y=None, text_size=self.setter('texture_size'),
			          halign='right', valign='middle',  multiline=False,
			          width=lambda *x: self.setter('text_size')(self, (self.width, None),
		texture_size=lambda *x: self.setter('height')(self.canvas, self.texture_size[1])))


class Button_With_Value(Button):
	def on_size(self, button_value='', *args):
		self.canvas.before.clear()
		self.bind(size=self.setter('texture_size'))
		with self.canvas.before:
			Color(1, 1, 1, 1)
			Rectangle(pos=self.pos, size=self.size, size_hint_y=None, size_hint_x=None, font=160,#text_size=(self.width, None),
			          height=0.9*self.texture_size[1], width=0.5*self.texture_size[0])


class CalculatorScreen(GridLayout):
	current_equation = '100'
	main_display_text = '100'
	memory = '0'

	def update(self):
		self.main_display.text = main_display_text
		self.equation_display.text = current_equation

	def send_digit(self, sending_button):
		global main_display_text
		global current_equation
		if main_display_text == '0':
			main_display_text = ''
		if current_equation == '0':
			current_equation = ''
		if ' ' in main_display_text:
			main_display_text = ''
			current_equation = ''
		main_display_text += sending_button.text
		current_equation += sending_button.text
		self.update()

	def send_operator(self, sending_button):
		global main_display_text
		global current_equation
		if main_display_text == '0':
			main_display_text = ''
		if current_equation == '':
			current_equation = '0'
		main_display_text = '0'
		current_equation += sending_button.button_value
		self.update()

	def send(self, sending_button):
		global main_display_text
		global current_equation
		if main_display_text == '0':
			main_display_text = ''
		if current_equation == '0':
			current_equation = ''
		main_display_text += sending_button.text
		current_equation += sending_button.text
		self.update()

	def evaluate(self, sending_button):
		global main_display_text
		global current_equation
		try:
			total = round(eval(current_equation), 7)
			if abs(total) > 10000000:
				main_display_text = 'GRE Error'
				current_equation = ''
			else:
				if total != '0':
					main_display_text = str(total).strip('0')
					current_equation = str(total)
				else:
					main_display_text = '0'
					current_equation = ''
		except ZeroDivisionError:
			main_display_text = 'Zero div Error '
			current_equation = ''
		except TypeError:
			main_display_text = 'type Error '
			current_equation = ''
		except SyntaxError:
			main_display_text = 'syntax Error '
			current_equation = ''
		self.update()

	def clear_all(self, sending_button):
		global main_display_text
		global current_equation
		global memory
		try:
			main_display_text = '0'
			memory = '0'
			current_equation = ''
		except ZeroDivisionError:
			main_display_text = 'Zero division error '
			current_equation = ''
		except TypeError:
			main_display_text = 'Script error '
			current_equation = ''
		except SyntaxError:
			main_display_text = 'Syntax error '
			current_equation = ''
		self.update()

	def plus_minus(self, sending_button):
		global main_display_text
		global current_equation
		try:
			current_equation = str(eval('-1*' + current_equation))
			main_display_text = current_equation
		except ZeroDivisionError:
			main_display_text = 'Zero division error '
			current_equation = ''
		except TypeError:
			main_display_text = 'Script error '
			current_equation = ''
		except SyntaxError:
			main_display_text = 'Syntax error '
			current_equation = ''
		self.update()

	def root(self, sending_button):
		global main_display_text
		global current_equation
		try:
			main_display_text = str(round(eval(current_equation + '**(1/2.0)'), 7)).strip('0')
			current_equation = main_display_text
		except ZeroDivisionError:
			main_display_text = 'Zero division error '
			current_equation = ''
		except TypeError:
			main_display_text = 'Script error '
			current_equation = ''
		except SyntaxError:
			main_display_text = 'Syntax error '
			current_equation = ''
		self.update()

	def mem_add(self, sending_button):
		global main_display_text
		global current_equation
		global memory
		memory = str(eval(current_equation) + float(memory)).strip('0')
		main_display_text = '0'
		current_equation = ''
		self.update()

	def mem_clear(self, sending_button):
		global memory
		memory = '0'
		self.update()

	def mem_recall(self, sending_button):
		global main_display_text
		global current_equation
		global memory
		current_equation = str(eval(current_equation + '+' + memory)).strip('0')
		main_display_text = current_equation
		current_equation = ''
		self.update()

	def clear_entry(self, sending_button):
		global main_display_text
		global current_equation
		try:
			main_display_text = '0'
			current_equation = ''
		except ZeroDivisionError:
			main_display_text = 'Zero division error '
			current_equation = ''
		except TypeError:
			main_display_text = 'Script error '
			current_equation = ''
		except SyntaxError:
			main_display_text = 'Syntax error '
			current_equation = ''
		self.update()

	def __init__(self, **kwargs):
		global current_equation
		global main_display_text
		# initial set up of vertical screen setup
		super(CalculatorScreen, self).__init__(**kwargs)
		self.orientation = 'vertical'
		self.cols = 1


		# create title label at top of screen
		# self.main_label = Label(text='\n[b]Work in progress[/b]\n', markup=True)
		# self.main_label.size_hint_y = None
		# self.main_label.font_size = 30
		# self.main_label.bind(texture_size=self.main_label.setter('size'))
		# self.add_widget(self.main_label)

		# set hidden Label object with actual expression being evaluated
		self.equation_display = CalculatorDisplay(text=current_equation)
		# self.add_widget(self.equation_display)
		# self.equation_display.size_hint_y = None
		# self.equation_display.color = (1, 0, 0, 1)
		# self.equation_display.font_size = 30

		# Add Box Layout for display
		self.box_display = BoxLayout(orientation='horizontal')
		self.add_widget(self.box_display)
		self.cols = 1
		self.box_display.size_hint_y = None

		# Add M label to left side of display
		self.labelM = CalculatorDisplay(text='M', size_hint_x=.2)
		self.labelM.color = (0, 0, 0, 1)
		self.labelM.size_hint_y = None
		self.labelM.font_size = 30
		self.box_display.add_widget(self.labelM)

		# create main display for generated expressions
		self.main_display = CalculatorDisplay(size_hint_x=.8, halign='right', valign='middle')
		# self.name.bind(texture_size=self.name.setter('text_size'))
		self.main_display.multiline = False
		self.main_display.text = main_display_text
		self.main_display.font_size = 30
		self.main_display.size_hint_y = None
		self.main_display.color = (0, 0, 0, 1)
		self.box_display.add_widget(self.main_display)


		# create horizontal box for two side by side buttons
		self.buttonGrid = GridLayout()
		self.add_widget(self.buttonGrid)
		self.buttonGrid.cols = 5

		# tuple of (ID, button symbol, BOOLEAN is digit, digit value to send, function command)
		tuple_of_buttons = (
			(0, 'MR', False, 'NA', self.mem_recall),
			(1, 'MC', False, 'NA', self.mem_clear),
			(2, 'M+', False, 'NA', self.mem_add),
			(3, '(', True, '(', self.send_operator),
			(4, ')', True, ')', self.send_operator),
			(5, '7', True, 7, self.send_digit),
			(6, '8', True, 8, self.send_digit),
			(7, '9', True, 9, self.send_digit),
			(8, '\u00F7', True, '/', self.send_operator),
			(9, 'C', False, 'NA', self.clear_all),
			(10, '4', True, 4, self.send_digit),
			(11, '5', True, 5, self.send_digit),
			(12, '6', True, 6, self.send_digit),
			(13, '\u00D7', True, '*', self.send_operator),
			(14, 'CE', False, 'NA', self.clear_entry),
			(15, '1', True, 1, self.send_digit),
			(16, '2', True, 2, self.send_digit),
			(17, '3', True, 3, self.send_digit),
			(18, '-', True, '-', self.send_operator),
			(19, '\u221A', False, 'NA', self.root),
			(20, '\u00B1', False, 'NA', self.plus_minus),
			(21,  '0', True, 0, self.send_digit),
			(22, '.', True, '.', self.send),
			(23, '+', True, '+', self.send_operator),
			(24, '=', False, 'NA', self.evaluate),
		)

		for button in tuple_of_buttons:
			name = 'button_' + str(button[0])
			self.name = Button_With_Value(text=button[1], disabled=False, color=(0, 0, 0, 1),)
			self.buttonGrid.add_widget(self.name)
			self.name.button_value = button[3]
			# self.name.bind(texture_size=self.name.setter('size'))
			# self.name.bind(texture_size=self.name.setter('text_size'))
			self.name.bind(on_press=button[4])
			if button[2]:
				pass
			else:
				pass


class MyApp(App):
	def build(self):
		return CalculatorScreen()


if __name__ == '__main__':
	MyApp().run()
