from wpilib.buttons.button import Button


class ComboButton(Button):

    def __init__(self, *buttons):
        super().__init__()
        self.buttons = buttons

    def get(self):
        isPressed = True

        for button in self.buttons:
            if not button.get():
                isPressed = False
                break

        return isPressed
