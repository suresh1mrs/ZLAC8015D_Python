
from zlac8015d import ZLAC8015D
import time

motors = ZLAC8015D.Controller(port="/dev/ttyUSB0")

# motors.disable_motor()

# motors.set_accel_time(1000,1000)
# motors.set_decel_time(1000,1000)

# motors.set_mode(3)
# motors.enable_motor()

last_time = time.time()
i = 0
period = 0.0
while True:
	try:
		# motors.set_rpm(cmds[0],cmds[1])
		l_tick, r_tick = motors.get_wheels_tick()
		print("period: {:.4f} l_tick: {:.1f} | r_tick: {:.1f}".format(period,l_tick,r_tick))
		l_curr, r_curr = motors.get_motor_current()
		print("period: {:.4f} l_curr: {:.1f} | r_curr: {:.1f}".format(period,l_curr,r_curr))
		voltage = motors.get_driver_voltage()
		print("period: {:.4f} voltage: {:.1f} ".format(period,voltage))
		l_temp, r_temp = motors.get_motor_temperature()
		print("period: {:.4f} l_temp: {:.1f} | r_temp: {:.1f}".format(period,l_temp,r_temp))
		period = time.time() - last_time
		time.sleep(2)
			

	except KeyboardInterrupt:
		# motors.disable_motor()
		break

	last_time = time.time()