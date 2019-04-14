from wpilib.command.command import Command

from ctre._impl import ControlMode


class Move(Command):

    def __init__(self, power):
        super().__init__(name="Move {}".format(power), subsystem=Command.getRobot().drivetrain)
        self.power = power

    def initialize(self):
        Command.getRobot().drivetrain.set(ControlMode.PercentOutput, self.power, self.power)

    def end(self):
        Command.getRobot().drivetrain.set(ControlMode.PercentOutput, 0.0, 0.0)
