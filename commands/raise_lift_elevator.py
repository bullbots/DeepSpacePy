from wpilib.command.commandgroup import Command


class RaiseLiftElevator(Command):

    def __init__(self, lTargetPos, eTargetPos):
        super().__init__(name="RaiseLiftElevator {}:{}".format(lTargetPos, eTargetPos),
                         subsystem=Command.getRobot().liftElevator)
        self.lTargetPos = lTargetPos
        self.eTargetPos = eTargetPos

    def initialize(self):
        Command.getRobot().compressor.stop()
        Command.getRobot().liftElevator.setLiftReference(self.lTargetPos)
        Command.getRobot().liftElevator.setElevatorReference(self.eTargetPos)

    def isFinished(self):
        return False
