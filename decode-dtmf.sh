#!/bin/bash
##############################################################
#
# Decode DTMF script: reads raw input from RTL-SDR receiver
# prints DTMF charachters to STDOUT
# 2019 Dana Simmons
#
##############################################################

FREQ="146.520M" # Frequency to monitor for incoming tones


rtl_fm -s 22050 -f $FREQ | multimon-ng -t raw -a DTMF -
