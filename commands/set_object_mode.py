from wpilib.command.instantcommand import InstantCommand
from wpilib.command.command import Command


class SetObjectMode(InstantCommand):

    def __init__(self, mode):
        super().__init__(name="SetObjectMode", subsystem=Command.getRobot().intakeOutput)
        self.mode = mode

    def initialize(self):
        if self.mode == Ball:
            Command.getRobot().intakeOutput.place(Take)
            Command.getRobot().intakeOutput.toggle(0)
        elif self.mode == Hatch:
            Command.getRobot().intakeOutput.place(Take)
            Command.getRobot().intakeOutput.toggle(1)
