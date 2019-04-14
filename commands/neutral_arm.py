from wpilib.command.commandgroup import CommandGroup

from commands.take_panel import TakePanel
from commands.inhale_exhale import InhaleExhale
from commands.set_intake_mode import SetIntakeMode

from subsystems.intake_output import IntakeOutput


class NeutralArm(CommandGroup):

    def __init__(self):
        super().__init__()
        self.addSequential(TakePanel(), 0.5)
        self.addSequential(InhaleExhale(IntakeOutput.CargeGiveOrTake.NADA))
        self.addSequential(SetIntakeMode(IntakeOutput.IntakeInOutNeutral.NEUTRAL))
