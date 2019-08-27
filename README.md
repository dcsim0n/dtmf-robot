# DTMF Robot
Direction controlled by STDIN
Designed to read output from multimon-ng [ https://github.com/EliasOenal/multimon-ng]

# Getting started
## Install dependencies
+ Install `multimon-ng` to decode dtmf tones from an RTL-SDR dongle
+ Use `pipenv` to install python dependincies: `pipenv install`

## Connect GPIO Pins:
+ GPIO2: MOTOR_A_IN_1
+ GPIO3: MOTOR_A_IN_2
+ GPIO4: MOTOR_A_ENABLE
+ GROUND: H_BRIDGE_GROUND
+ GPIO17: MOTOR_B_IN_1
+ GPIO27: MOTOR_B_IN_2
+ GPIO22: MOTOR_B_ENABLE

# Start the Beast
1. `pipenv shell` to enter a pipenv virtual enviornment
2. Run `./decodedtmf.sh | python main.py`
3. Send DTMF tones using radio keypad

# Configuration
The control/input frequency of the dtmf decoder can be changed using the `FREQ` variable in `decodedtmf.sh`
