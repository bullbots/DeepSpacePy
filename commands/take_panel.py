from wpilib.command.command import Command

from subsystems.intake_output import IntakeOutput


class TakePanel(Command):

    def __init__(self):
        super().__init__(subsystem=Command.getRobot().intakeOutput)

    def initialize(self):
        Command.getRobot().intakeOutput.panelPlace(IntakeOutput.PanelPutOrTake.TAKE)
