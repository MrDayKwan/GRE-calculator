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
            Rectangle(pos=self.pos, size=self.size, size_hint_y=None)
#
#
class Button_With_Value(Button):
    def on_size(self, button_value='', *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(pos=self.pos, size=self.size, size_hint_y=None)
        # self.parent.ids.main_display.text += self.text
#
# class FunctionButton(Button):
#     def on_size(self, *args):
#         self.canvas.before.clear()
#         with self.canvas.before:
#             Color(1, 1, 1, 1)
#             Rectangle(pos=self.pos, size=self.size, size_hint_y=None)

# class GeneratorScreen(BoxLayout):
#     def __init__(self, **kwargs):
#         def send(instance):
#             self.backstory.text = generator(instance)
#             self.copy.disabled = False
#             self.mid.text = ' '
#
#         def copy_text(instance):
#             Clipboard.copy(self.backstory.text)
#             self.mid.text = 'Current backstory is copied to clipboard.'
#
#         # initial set up of vertical screen setup
#         super(GeneratorScreen, self).__init__(**kwargs)
#         self.orientation = 'vertical'
#
#         # create title label at top of screen
#         self.main_label = Label(text='\n[b]Character Backstory Generator[/b]\n', markup=True)
#         self.main_label.font_size = 30
#         self.main_label.size_hint_y = None
#         self.main_label.bind(texture_size=self.main_label.setter('size'))
#         self.add_widget(self.main_label)
#
#         # create main display for generated backstories
#         self.backstory = ColoredRectangle()
#         self.backstory.text = 'Enter a backstory.'
#         self.backstory.color = (0, 0, 0, 1)
#         ### self.backstory.size = self.backstory
#         self.backstory.text_size = self.backstory.size
#         ### self.backstory.height=self.backstory.texture_size[1]
#         self.add_widget(self.backstory)
#
#         # create buffer area using label
#         self.mid = Label(text=' ', size_hint_y=None)
#         self.add_widget(self.mid)
#         self.mid.bind(texture_size=self.mid.setter('size'))
#
#         # create horizontal box for two side by side buttons
#         self.horizontalBox = BoxLayout(orientation='horizontal', size_hint_y=None)
#         self.add_widget(self.horizontalBox)
#
#         # add button to copy existing text from backstory field
#         self.copy = Button(text='')
#         self.horizontalBox.add_widget(self.copy)
#         self.copy.bind(on_press=copy_text)
#         self.copy.bind(texture_size=self.horizontalBox.setter('size'))
#
#         # add buttom to generate new backstory in field
#         self.generate = Button(text='')
#         self.horizontalBox.add_widget(self.generate)
#         self.generate.bind(on_press=send)
#         self.generate.bind(texture_size=self.horizontalBox.setter('size'))
#
#         # add button to copy existing text from backstory field
#         self.copy = Button(text='')
#         self.horizontalBox.add_widget(self.copy)
#         self.copy.bind(on_press=copy_text)
#         self.copy.bind(texture_size=self.horizontalBox.setter('size'))
#
#         # add buttom to generate new backstory in field
#         self.generate = Button(text='')
#         self.horizontalBox.add_widget(self.generate)
#         self.generate.bind(on_press=send)
#         self.generate.bind(texture_size=self.horizontalBox.setter('size'))
#
#         # add button to copy existing text from backstory field
#         self.copy = Button(text='', disabled=True)
#         self.horizontalBox.add_widget(self.copy)
#         self.copy.bind(on_press=copy_text)
#         self.copy.bind(texture_size=self.horizontalBox.setter('size'))
#
#         # add bottom black buffer zone
#         self.bottom = Label(text=' ', size_hint_y=None)
#         self.add_widget(self.bottom)
#         self.bottom.bind(texture_size=self.bottom.setter('size'))


class CalculatorScreen(GridLayout):
    current_equation = '100'
    main_display_text = '100'

    # def send(self):
    #     global main_display_text
    #     global equation
    #     main_display_text += str(0)
    #     equation = expression
    #     print('grerr')
    #
    # def press(self):
    #     global main_display_text
    #     main_display_text += '0'
    #     print(main_display_text)
    #
    #
    # def evaluate(self):
    #     print('no')
    #     try:
    #         global expression
    #         global equation
    #         total = str(eval(expression))
    #         equation = total
    #         expression = ''
    #     except ZeroDivisionError:
    #         equation = 'Zero division error '
    #         expression = ''
    #     except TypeError:
    #         equation = 'Script error '
    #         expression = ''
    #     except SyntaxError:
    #         equation = 'Syntax error '
    #         expression = ''
    #
    # def mem_recall(self):
    #     global expression
    #     global equation
    #     global memory
    #     expression += str(memory)
    #     equation = expression
    #     print(f'memory {memory}')
    #
    # def mem_clear(self):
    #     global expression
    #     global equation
    #     global memory
    #     memory = ''
    #
    # def mem_add(self):
    #     global expression
    #     global equation
    #     global memory
    #     memory = str(eval(expression + '+' + memory))
    #     expression = ''
    #
    # def plus_minus(self):
    #     global expression
    #     global equation
    #     global memory
    #     expression = str(eval('-1*' + expression))
    #     equation = expression
    #
    # def clear_entry(self):
    #     global expression
    #     global equation
    #     expression = ''
    #     equation = ''
    #
    # def clear_all(self):
    #     global expression
    #     global equation
    #     global memory
    #     expression = ''
    #     memory = '0'
    #     equation = ''
    #
    # def root(self):
    #     global expression
    #     global equation
    #     equation = str(eval(expression + '**(1/2.0)'))
    #     expression = ''
    #
    # def generator(self):
    #     value = ''
    #     for item in range(0, 120):
    #         value += str(random.randint(0, 17))
    #     return value


    def __init__(self, **kwargs):
        global current_equation
        global main_display_text
        # initial set up of vertical screen setup
        super(CalculatorScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.cols = 1


        # create title label at top of screen
        self.main_label = Label(text='\n[b]Work in progress[/b]\n', markup=True)
        self.main_label.size_hint_y = None
        self.main_label.font_size = 30
        self.main_label.bind(texture_size=self.main_label.setter('size'))
        self.add_widget(self.main_label)

        # set hidden Label object with actual expression being evaluated
        self.equation_display = CalculatorDisplay(text=current_equation)
        self.add_widget(self.equation_display)
        self.equation_display.size_hint_y = None
        self.equation_display.color = (1, 0, 0, 1)
        self.equation_display.font_size = 30

        # Add Box Layout for display
        self.box_display = BoxLayout(orientation='horizontal')
        self.add_widget(self.box_display)
        self.cols = 1
        self.box_display.size_hint_y = None

        # Add M label to left side of display
        self.labelM = CalculatorDisplay(text='M')
        self.labelM.color = (0, 0, 0, 1)
        self.labelM.size_hint_y = None
        self.labelM.font_size = 30
        self.box_display.add_widget(self.labelM)

        # create main display for generated expressions
        self.main_display = CalculatorDisplay()
        self.main_display.text = main_display_text
        self.main_display.font_size = 30
        self.main_display.size_hint_y = None
        self.main_display.color = (0, 0, 0, 1)
        self.box_display.add_widget(self.main_display)
        # self.box_display.bind(col_span=5)


        # create horizontal box for two side by side buttons
        self.buttonGrid = GridLayout()
        self.add_widget(self.buttonGrid)
        self.buttonGrid.cols = 5

        def update():
            self.main_display.text = main_display_text
            self.equation_display.text = current_equation

        def send_digit(sending_button):
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
            update()
            print(main_display_text)

        def send_operator(sending_button):
            global main_display_text
            global current_equation
            if main_display_text == '0':
                main_display_text = ''
            if current_equation == '':
                current_equation = '0'
            main_display_text = '0'
            current_equation += sending_button.button_value
            update()

        def send(sending_button):
            global main_display_text
            global current_equation
            if main_display_text == '0':
                main_display_text = ''
            if current_equation == '0':
                current_equation = ''
            main_display_text += sending_button.text
            current_equation += sending_button.text
            update()

        def evaluate(sending_button):
            global main_display_text
            global current_equation
            try:
                total = round(eval(current_equation), 7)
                if total > 10000000:
                    main_display_text = 'GRE Error'
                    current_equation = ''
                else:
                    main_display_text = str(total)
                    current_equation = str(total)
            except ZeroDivisionError:
                main_display_text = 'Zero div Error '
                current_equation = ''
            except TypeError:
                main_display_text = 'type Error '
                current_equation = ''
            except SyntaxError:
                main_display_text = 'syntax Error '
                current_equation = ''
            update()

        def clear_all(sending_button):
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
            update()

        def plus_minus(sending_button):
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
            update()

        def root(self):
            global main_display_text
            global current_equation
            try:
                main_display_text = str(eval(current_equation + '**(1/2.0)'))
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
            update()

        # def mem_recall(self):
        #     expression += str(memory)
        #     equation = expression
        #     print(f'memory {memory}')
        #
        # def mem_clear(self):
        #     global expression
        #     global equation
        #     global memory
        #     memory = ''

        # def mem_add(self):
        #     global expression
        #     global equation
        #     global memory
        #     memory = str(eval(expression + '+' + memory))
        #     expression = ''
        #

# currently does not work
        def clear_entry(self):
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
            update()




        # tuple of (ID, button symbol, BOOLEAN is digit, digit value to send, function command)
        tuple_of_buttons = (
            (0, 'MR', False, 'NA', send), #, self.mem_recall),
            (1, 'MC', False, 'NA', send), #, self.mem_clear()),
            (2, 'M+', False, 'NA', send), #, self.mem_add),
            (3, '(', True, '(', send_operator),
            (4, ')', True, ')', send_operator),
            (5, '7', True, 7, send_digit),
            (6, '8', True, 8, send_digit),
            (7, '9', True, 9, send_digit),
            (8, '\u00F7', True, '/', send_operator),
            (9, 'C', False, 'NA', clear_all),
            (10, '4', True, 4, send_digit),
            (11, '5', True, 5, send_digit),
            (12, '6', True, 6, send_digit),
            (13, '\u00D7', True, '*', send_operator),
            (14, 'CE', False, 'NA', clear_entry),
            (15, '1', True, 1, send_digit),
            (16, '2', True, 2, send_digit),
            (17, '3', True, 3, send_digit),
            (18, '-', True, '-', send_operator),
            (19, '\u221A', False, 'NA', root),
            (20, '\u00B1', False, 'NA', plus_minus),
            (21,  '0', True, 0, send_digit),
            (22, '.', True, '.', send),
            (23, '+', True, '+', send_operator),
            (24, '=', False, 'NA', evaluate),
        )

            
        for button in tuple_of_buttons:
            name = 'button_' + str(button[0])
            self.name = Button_With_Value(text=button[1], disabled=False, color=(1, .5, 0, 1),)
            self.buttonGrid.add_widget(self.name)
            self.name.button_value = button[3]
            self.name.bind(texture_size=self.name.setter('size'))
            self.name.bind(on_press=button[4])
            if button[2]:
                pass
            else:
                pass


        # def send(instance):

        # # add button to copy existing text from backstory field
        #         self.copy = Button(text='')
        #         self.horizontalBox.add_widget(self.copy)
        #         self.copy.bind(on_press=copy_text)
        #         self.copy.bind(texture_size=self.horizontalBox.setter('size'))
        #
        #         # add buttom to generate new backstory in field
        #         self.generate = Button(text='')
        #         self.horizontalBox.add_widget(self.generate)
        #         self.generate.bind(on_press=send)
        #         self.generate.bind(texture_size=self.horizontalBox.setter('size'))


        # self.backstory.text = generator(instance)
        #             self.copy.disabled = False
        #             self.mid.text = ' '
        #
        #         def copy_text(instance):
        #             Clipboard.copy(self.backstory.text)
        #             self.mid.text = 'Current backstory is copied to clipboard.'
        #
        #         # initial set up of vertical screen setup
        #         super(GeneratorScreen, self).__init__(**kwargs)
        #         self.orientation = 'vertical'
        #
        #         # create title label at top of screen
        #         self.main_label = Label(text='\n[b]Character Backstory Generator[/b]\n', markup=True)
        #         self.main_label.font_size = 30
        #         self.main_label.size_hint_y = None
        #         self.main_label.bind(texture_size=self.main_label.setter('size'))
        #         self.add_widget(self.main_label)
        #
        #         # create main display for generated backstories
        #         self.backstory = ColoredRectangle()
        #         self.backstory.text = 'Enter a backstory.'
        #         self.backstory.color = (0, 0, 0, 1)
        #         ### self.backstory.size = self.backstory
        #         self.backstory.text_size = self.backstory.size
        #         ### self.backstory.height=self.backstory.texture_size[1]
        #         self.add_widget(self.backstory)

        # self.button_1 = Button(text='1', color=(1, .5, 0, 1))
        # self.buttonGrid.add_widget(self.button_1)
        # self.button_1.bind(on_press=self.main_display_text.text +=self.button_1.text)

        # # add ALL buttons
        # all_key_icons = ('MR', 'MC', 'M+', '(', ')', 7, 8, 9, '\u00F7', 'C', 4, 5, 6, '\u00D7', 'CE',
        #         1, 2, 3, '-', '\u221A', '\u00B1', 0, '.', '+', '=') # list of labels
        # all_keys = [Button(text=str(all_key_icons[i]), disabled=False, color=(1, .5, 0, 1), ) for i in
        #         range(0, len(all_key_icons))] # list of buttons
        # for digit_key in all_keys:
        #     self.buttonGrid.add_widget(digit_key)
        #     digit_key.bind(texture_size=digit_key.setter('size'))
        #
        # # add button to generate new main_string in field
        # self.extra = Button(text='\nGenerate\n')
        # self.add_widget(self.extra)
        # self.extra.bind(on_press=generate)
        # self.extra.bind(texture_size=self.extra.setter('size'))
        #
        # # for DIGIT buttons, add a command that passes the button value to the screen
        # function_icons = ('MR', 'MC', 'M+', 'C', 'CE', '\u221A', '\u00B1', '=')
        # digit_icons = [button for button in all_keys if button.text not in function_icons]
        # tuple_of_equation_symbols = ('(', ')', 7, 8, 9, '/', 4, 5, 6, '*', 1, 2, 3, '-', 0, '.', '+')
        # digit_symbol_list = [[digit_button, digit_symbol] for digit_button in digit_icons for
        #                          digit_symbol in tuple_of_equation_symbols]
        # print(digit_symbol_list)
        # for [digit_button, digit_symbol] in digit_symbol_list:
        #     digit_button.bind(on_press=lambda x: press(digit_symbol))
        #
        #
        # # For FUNCTION buttons, create lst of lsts such that each sublist is [button, function] to add button commands
        # function_buttons = [button for button in all_keys if button.text in function_icons]
        # tuple_of_function_commands = (mem_recall, mem_clear, mem_add, clear_all, clear_entry, root, plus_minus, evaluate)
        # function_command_list = [[function_button, function_command] for function_button in function_buttons for
        #                          function_command in tuple_of_function_commands]
        #
        # for [function_button, function_command] in function_command_list:
        #     function_button.bind(on_press=function_command)


        # # For FUNCTION buttons, create list of lists such that each sublist is [icon, button, function]
        # function_icons = ('MR', 'MC', 'M+', 'C', 'CE', '\u221A', '\u00B1', '=')
        # function_tup = (mem_recall, mem_clear, mem_add, clear_all, clear_entry, root, plus_minus, evaluate)
        # map(list.__add__, function_icons, all_keys, function_tup)
        #
        # for digit_key in all_keys:
        #     digit_key_function = enumerate(all_keys, 0)
        #     self.buttonGrid.add_widget(digit_key)
        #     self.digit_key.bind()


        # function_tup = (mem_recall, mem_clear, mem_add, clear_all, clear_entry, root, plus_minus, evaluate)
        # function_icons = ('MR', 'MC', 'M+', 'C', 'CE', '\u221A', '\u00B1', '=')

        # digit_keys = ('(', ')', 7, 8, 9, 4, 5, 6, 1, 2, 3, '-', 0, '.', '+', '=')
        # digit_keys = [DigitButton(text=str(digit_key_icons[i]), disabled=True, color=(1, .5, 0, 1)) for i in range(0, len(digit_key_icons))]
        # for digit_key in digit_keys:
        #     self.buttonGrid.text =

        # button_name = 'button_' + str(i) + '_key'
        #     digit = str(i)
        #     self.button_name.bind(on_press=press)

            # self.button_name.bind(digit=str(i))

        # add button to copy existing text from backstory field
        # self.button1 = Button_With_Value(text='1', disabled=False)
        # self.buttonGrid.add_widget(self.button1)
        #
        # self.button1.bind(on_press=press)
        # self.button1.bind(texture_size=self.horizontalBox.setter('size'))


            # callback function tells when button pressed


class MyApp(App):
    def build(self):
        return CalculatorScreen()

def test_press(self):
    print("button pressed")

def press(self):
    global main_display_text
    main_display_text += '0'
    CalculatorScreen.main_display.text = str(main_display_text)
    print(main_display_text)


if __name__ == '__main__':
    MyApp().run()
