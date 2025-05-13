from abc import ABC, abstractmethod

class TextState(ABC):
    @abstractmethod
    def processText(self, text):
       pass

class Text():
    def __init__(self,message):
        self.message = message
        self.state =   NormalText(self.message) # default for program

    def set_state(self,state  :  TextState):
        self.state = state


    def show_message(self):
        self.state.PrintMessage()


class ReverseText(TextState):
    def __init__(self,message):
        self.message = message

    def processText(self):
        self.message  = self.message[::-1]

    def PrintMessage(self):
        self.processText()
        print(self.message )

class NormalText(TextState):
    def __init__(self,message):
        self.message = message


    def processText(self):
        self.message  = self.message

    def PrintMessage(self):
        self.processText()
        print(self.message )



if __name__ == '__main__':

    sentence = input('Enter your sentence: ')
    mode = int(input('Can the sentence be printed in reverse or in normal form?(1-normal or 2-reverse)'))
    if mode == 1:
        message = Text(sentence)
        message.show_message()
    if mode == 2:
        message = Text(sentence)
        message.set_state(ReverseText(message.message))
        message.show_message()























