from abc import ABC, abstractmethod

class ElevatorState(ABC):
    @abstractmethod
    def request_up(self, elevator):
        pass

    @abstractmethod
    def request_down(self, elevator):
        pass

    @abstractmethod
    def reach_floor(self, elevator, floor):
        pass


class Elevator:
    def __init__(self, min_floor = -3, max_floor = 25):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = 0
        self.state = StoppedState()

    def set_state(self, state):
        self.state = state

    def request_up(self):
        self.state.request_up(self)

    def request_down(self):
        self.state.request_down(self)

    def reach_floor(self, floor):
        self.current_floor = floor
        self.state.reach_floor(self, floor)

    def Status(self):
            self.state.Status(self.current_floor)

    def move_down(self):
        if self.current_floor > self.min_floor:
            print("در حال حرکت به پایین...")
            self.reach_floor(self.current_floor - 1)
        else:
            print("در پایین‌ترین طبقه هستیم!")
            self.set_state(StoppedState())

    def move_up(self):
        if self.current_floor < self.max_floor:
            print("در حال حرکت به بالا...")
            self.reach_floor(self.current_floor + 1)
        else:
            print("در بالاترین طبقه هستیم!")
            self.set_state(StoppedState())




class StoppedState(ElevatorState):
    def request_up(self, elevator):
        print("درخواست بالا رفتن  دریافت شد.")
        elevator.set_state(GoingUpState())
        elevator.move_up()

    def request_down(self, elevator):
        print("درخواست پایین  رفتن دریافت شد.")
        elevator.set_state(GoingDownState())
        elevator.move_down()

    def Status(self,elevator):
        print(f"اسانسور در طبقه  {self.current_floor} متوقف می باشد..")



    def reach_floor(self, elevator, floor):
        print(f"آسانسور در طبقه {floor} متوقف است.")



class GoingUpState(ElevatorState):
    def request_up(self, elevator):
        print("در حال حاضر در حال حرکت به بالا هستیم.")

    def request_down(self, elevator):
        print("درخواست پایین ذخیره شد (بعد از پایان بالا).")

    def reach_floor(self, elevator, floor):
        print(f"به طبقه {floor} رسیدیم.")
        if floor == elevator.max_floor:
            print("به بالاترین طبقه رسیدیم، توقف.")
            elevator.set_state(StoppedState())

    def Status(self,current_floor):
        print(f"اسانسور بعد از بالا رفتن در طبقه  {current_floor} متوقف می باشد.")



class GoingDownState(ElevatorState):
    def request_up(self, elevator):
        print("درخواست بالا ذخیره شد (بعد از پایان پایین).")

    def request_down(self, elevator):
        print("در حال حاضر در حال حرکت به پایین هستیم.")

    def reach_floor(self, elevator, floor):
        print(f"به طبقه {floor} رسیدیم.")
        if floor == elevator.min_floor:
            print("به پایین‌ترین طبقه رسیدیم، توقف.")
            elevator.set_state(StoppedState())

    def Status(self,current_floor):
        print(f"اسانسور بعد از پایین رفتن در طبقه  {current_floor} متوقف می باشد.")






if __name__ == "__main__":
    elevator = Elevator()

    elevator.request_up()
    elevator.reach_floor(1)
    elevator.Status()

    elevator.request_up()
    elevator.reach_floor(10)
    elevator.Status()

    elevator.request_down()
    elevator.reach_floor(-3)
    elevator.Status()








