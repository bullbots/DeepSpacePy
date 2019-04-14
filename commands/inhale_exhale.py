from wpilib.command.instantcommand import InstantCommand
from wpilib.command.command import Command


class InhaleExhale(InstantCommand):

    def __init__(self, key):
        super().__init__(name="InhaleExhale {}".format(key), subsystem=Command.getRobot().intakeOutput)
        self.key = key

    def initialize(self):
        Command.getRobot().intakeOutput.giveOrTakeCargo(self.key)
