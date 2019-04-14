import math
import enum
import logging

from wpilib.command.subsystem import Subsystem
from wpilib.doublesolenoid import DoubleSolenoid

from ctre.wpi_talonsrx import WPI_TalonSRX
from ctre._impl import FeedbackDevice, ControlMode

from robotmap import RobotMap
from constants import Constants
from commands.joystick_drive import JoystickDrive


class DriveTrain(Subsystem):
    """
    This subsystem controls the drivetrain for the robot.
    """
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.getName())

        # Configure motors
        self.leftMasterTalon = WPI_TalonSRX(RobotMap.LEFT_MASTER_TALON)
        self.leftSlaveTalon = WPI_TalonSRX(RobotMap.LEFT_SLAVE_TALON)
        self.rightMasterTalon = WPI_TalonSRX(RobotMap.RIGHT_MASTER_TALON)
        self.rightSlaveTalon = WPI_TalonSRX(RobotMap.RIGHT_SLAVE_TALON)

        self.leftSlaveTalon.follow(self.leftMasterTalon)
        self.rightSlaveTalon.follow(self.rightMasterTalon)

        self.leftMasterTalon.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Relative, 0,
                                                          Constants.TIMEOUT_MS)
        self.rightMasterTalon.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Relative, 0,
                                                           Constants.TIMEOUT_MS)
        self.leftMasterTalon.setInverted(True)
        self.leftSlaveTalon.setInverted(True)

        self.configureDrivePID()

        # Configure shift solenoid
        self.shiftSolenoid = DoubleSolenoid(RobotMap.SHIFT_IN_SOLENOID, RobotMap.SHIFT_OUT_SOLENOID)

    def configureDrivePID(self):
        # Slot 0 = Distance PID
        # Slot 1 = Velocity PID
        self.leftMasterTalon.config_kF(0, Constants.LEFT_DISTANCE_F, Constants.TIMEOUT_MS)
        self.leftMasterTalon.config_kP(0, Constants.LEFT_DISTANCE_P, Constants.TIMEOUT_MS)
        self.leftMasterTalon.config_kI(0, Constants.LEFT_DISTANCE_I, Constants.TIMEOUT_MS)
        self.leftMasterTalon.config_kD(0, Constants.LEFT_DISTANCE_D, Constants.TIMEOUT_MS)
        
        self.leftMasterTalon.config_kF(1, Constants.LEFT_VELOCITY_F, Constants.TIMEOUT_MS)
        self.leftMasterTalon.config_kP(1, Constants.LEFT_VELOCITY_P, Constants.TIMEOUT_MS)
        self.leftMasterTalon.config_kI(1, Constants.LEFT_VELOCITY_I, Constants.TIMEOUT_MS)
        self.leftMasterTalon.config_kD(1, Constants.LEFT_VELOCITY_D, Constants.TIMEOUT_MS)

        self.rightMasterTalon.config_kF(0, Constants.RIGHT_DISTANCE_F, Constants.TIMEOUT_MS)
        self.rightMasterTalon.config_kP(0, Constants.RIGHT_DISTANCE_P, Constants.TIMEOUT_MS)
        self.rightMasterTalon.config_kI(0, Constants.RIGHT_DISTANCE_I, Constants.TIMEOUT_MS)
        self.rightMasterTalon.config_kD(0, Constants.RIGHT_DISTANCE_D, Constants.TIMEOUT_MS)

        self.rightMasterTalon.config_kF(1, Constants.RIGHT_VELOCITY_F, Constants.TIMEOUT_MS)
        self.rightMasterTalon.config_kP(1, Constants.RIGHT_VELOCITY_P, Constants.TIMEOUT_MS)
        self.rightMasterTalon.config_kI(1, Constants.RIGHT_VELOCITY_I, Constants.TIMEOUT_MS)
        self.rightMasterTalon.config_kD(1, Constants.RIGHT_VELOCITY_D, Constants.TIMEOUT_MS)

        self.leftMasterTalon.configMotionAcceleration(6385)
        self.rightMasterTalon.configMotionAcceleration(6385)

        self.leftMasterTalon.configMotionCruiseVelocity(6385)
        self.rightMasterTalon.configMotionCruiseVelocity(6385)

    def initDefaultCommand(self):
        self.setDefaultCommand(JoystickDrive())

    def zeroEncoders(self):
        self.leftMasterTalon.setSelectedSensorPosition(0)
        self.rightMasterTalon.setSelectedSensorPosition(0)

    def set(self, type, leftMagnitude, rightMagnitude):
        assert (isinstance(type, ControlMode))

        if type == ControlMode.PercentOutput:
            self.leftMasterTalon.set(ControlMode.PercentOutput, leftMagnitude)
            self.rightMasterTalon.set(ControlMode.PercentOutput, rightMagnitude)
        elif type == ControlMode.Velocity:
            self.leftMasterTalon.set(ControlMode.Velocity, leftMagnitude)
            self.rightMasterTalon.set(ControlMode.Velocity, rightMagnitude)
        elif type == ControlMode.MotionMagic:
            self.leftMasterTalon.set(ControlMode.MotionMagic, leftMagnitude)
            self.rightMasterTalon.set(ControlMode.MotionMagic, rightMagnitude)

    def setPIDSlot(self, slot):
        self.leftMasterTalon.selectProfileSlot(slot, 0)
        self.rightMasterTalon.selectProfileSlot(slot, 0)

    def getPositions(self):
        return self.leftMasterTalon.getSelectedSensorPosition(), self.rightMasterTalon.getSelectedSensorPosition()

    def getVelocities(self):
        return self.leftMasterTalon.getSelectedSensorVelocity(), self.rightMasterTalon.getSelectedSensorVelocity()

    def customArcadeDrive(self, xSpeed, zRotation, squareInputs):
        deadband = 0.1
        xSpeed, zRotation = self.limit(xSpeed, zRotation)

        xSpeed, zRotation = self.applyDeadband(deadband, xSpeed, zRotation)

        if squareInputs:
            xSpeed = math.copysign(xSpeed * xSpeed, xSpeed)
            zRotation = math.copysign(zRotation * zRotation, zRotation)

        maxInput = math.copysign(max(abs(xSpeed), abs(zRotation)), xSpeed)

        if xSpeed >= 0:
            if zRotation >= 0:
                leftMotorOutput = maxInput
                rightMotorOutput = xSpeed - zRotation
            else:
                leftMotorOutput = xSpeed + zRotation
                rightMotorOutput = maxInput
        else:
            if zRotation >= 0:
                leftMotorOutput = xSpeed + zRotation
                rightMotorOutput = maxInput
            else:
                leftMotorOutput = maxInput
                rightMotorOutput = xSpeed - zRotation

        # Fine tune control
        if abs(xSpeed) > abs(zRotation):
            self.leftMasterTalon.set(ControlMode.PercentOutput, self.limit(leftMotorOutput) * 0.55)
            self.rightMasterTalon.set(ControlMode.PercentOutput, self.limit(rightMotorOutput) * -0.55)
        else:
            self.leftMasterTalon.set(ControlMode.PercentOutput, self.limit(leftMotorOutput) * 0.55)
            self.rightMasterTalon.set(ControlMode.PercentOutput, self.limit(rightMotorOutput) * -0.55)

    def limit(self, *args):
        return_list = []
        for arg in args:
            if arg > 1.0:
                return_list.append(1.0)
            elif arg < -1.0:
                return_list.append(1.0)
            else:
                return_list.append(arg)

        return return_list[0] if len(return_list) == 1 else return_list

    def applyDeadband(self, deadband, *args):
        return_list = []
        for arg in args:
            if abs(arg) < deadband:
                return_list.append(0.0)
            else:
                return_list.append(arg)

        return return_list[0] if len(return_list) == 1 else return_list
