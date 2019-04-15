from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from wpilib.command.instantcommand import InstantCommand
from wpilib.command.command import Command

from combo_button import ComboButton
from commands.intake import Intake
from commands.neutral_intake import NeutralIntake
from commands.set_object_mode import SetObjectMode
from commands.low_conditional import LowConditional
from commands.middle_conditional import MiddleConditional
from commands.top_conditional import TopConditional
from commands.two_climb_group import TwoClimbG
from commands.one_climb_group import OneClimbG
from commands.move_elevator import MoveElevator
from commands.high_center import HighCenter

from subsystems.intake_output import IntakeOutput


class OI(object):

    def __init__(self):
        # Create Joysticks
        self.stick = Joystick(0)
        self.gamepad = Joystick(1)

        # Create Buttons
        self.trigger = JoystickButton(self.stick, 1)
        self.button2 = JoystickButton(self.stick, 2)
        self.button3 = JoystickButton(self.stick, 3)
        self.button4 = JoystickButton(self.stick, 4)
        self.button5 = JoystickButton(self.stick, 5)
        self.button6 = JoystickButton(self.stick, 6)
        self.button7 = JoystickButton(self.stick, 7)
        self.button8 = JoystickButton(self.stick, 8)
        self.button9 = JoystickButton(self.stick, 9)
        self.button10 = JoystickButton(self.stick, 10)
        self.button11 = JoystickButton(self.stick, 11)

        self.pad1 = JoystickButton(self.gamepad, 1)
        self.pad2 = JoystickButton(self.gamepad, 2)
        self.pad3 = JoystickButton(self.gamepad, 3)
        self.pad4 = JoystickButton(self.gamepad, 4)
        self.pad5 = JoystickButton(self.gamepad, 5)
        self.pad6 = JoystickButton(self.gamepad, 6)
        self.pad7 = JoystickButton(self.gamepad, 7)
        self.pad8 = JoystickButton(self.gamepad, 8)
        self.pad9 = JoystickButton(self.gamepad, 9)

        self.climb2 = ComboButton(self.pad6, self.button6)
        self.climb3 = ComboButton(self.pad5, self.button6)

        # Test buttons
        self.test = ComboButton(self.pad2, self.button6)

        # Command hookups
        self.trigger.whenPressed(Intake())
        self.trigger.whenReleased(NeutralIntake())

        # self.button2.whileHeld(Align(3.0))

        self.button8.whenPressed(type('', (InstantCommand,),
                                      {'initialize': lambda: Command.getRobot().liftElevator.resetEncoders()}))

        self.pad1.whenPressed(SetObjectMode(IntakeOutput.BallOrHatchMode.HATCH))
        self.pad1.whenReleased(SetObjectMode(IntakeOutput.BallOrHatchMode.BALL))
        Command.getRobot().intakeOutput.mode = IntakeOutput.BallOrHatchMode.HATCH if \
            self.pad1.get() else IntakeOutput.BallOrHatchMode.HATCH

        self.test.whenPressed(TopConditional())
        self.pad3.whenPressed(MiddleConditional())
        self.pad4.whenPressed(LowConditional())

        self.climb2.whenPressed(TwoClimbG())
        self.climb3.whenPressed(OneClimbG())

        self.pad7.whenPressed(MoveElevator(1))
        self.pad8.whenPressed(HighCenter())


    @property
    def driveStick(self):
        return self.stick

    @property
    def gamePad(self):
        return self.gamePad
