import pprint

from pyfrc.physics import drivetrains


class PhysicsEngine:

    def __init__(self, physics_controller):
        self.physics_controller = physics_controller
        self.drivetrain = drivetrains.TwoMotorDrivetrain()
        self.initial = True

    def update_sim(self, hal_data, now, tm_diff):
        # print(hal_data)
        if self.initial:
            self.initial = False
            # pprint.pprint(hal_data["CAN"])
            # for key in hal_data["sparkmax-5"].keys():
            #     print(key)
        # Simulate the drivetrain
        left_master_motor = hal_data["CAN"][1]["value"]
        right_master_motor = hal_data["CAN"][3]["value"]

        speed, rotation = self.drivetrain.get_vector(left_master_motor, right_master_motor)
        self.physics_controller.drive(speed, rotation, tm_diff)
