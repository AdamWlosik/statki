from kivy.properties import BooleanProperty, DictProperty, ObjectProperty
from kivy.uix.button import Button


class GameButton(Button):
    coordinate = DictProperty({"x": 0, "y": 0})
    isShip = BooleanProperty(False)
    wasHit = BooleanProperty(False)
    sendMessage = ObjectProperty()

    def setWasHit(self, value=True):
        self.wasHit = value
        self.updateColor()

    def on_release(self):
        super(GameButton, self).on_release()
        self.isShip = not self.isShip
        self.updateColor()
        print(self.coordinate)
        self.sendMessage(self.coordinate)

    def hit(self):
        self.isShip = True
        self.setWasHit()
        print("Hit")

    def miss(self):
        self.isShip = False
        self.setWasHit()
        print("Miss")

    def updateColor(self):
        if self.isShip and self.wasHit:
            self.background_color = (0.9, 0, 0)
        elif self.isShip and not self.wasHit:
            self.background_color = (0, 0.9, 0)
        elif not self.isShip and self.wasHit:
            self.background_color = (0, 0, 0.9)
        elif not self.isShip and not self.wasHit:
            self.background_color = (0.9, 0.9, 0.9)
