from wpilib.command.command import Command


class LiftDrive(Command):

    def __init__(self, power):
        super().__init__(name="LiftDrive {}".format(power), subsystem=Command.getRobot().liftElevator)
        self.power = power

    def initialize(self):
        Command.getRobot().liftElevator.liftDrive(self.power)

    def end(self):
        Command.getRobot().liftElevator.liftDrive(0.0)
