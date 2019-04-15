from wpilib.command.command import Command

from subsystems.intake_output import IntakeOutput

from commands.command_logging_decorator import logging_command


@logging_command
class PutPanel(Command):

    def __init__(self):
        super().__init__(subsystem=Command.getRobot().intakeOutput)

    def initialize(self):
        Command.getRobot().intakeOutput.panelPlace(IntakeOutput.PanelPutOrTake.PUT)
