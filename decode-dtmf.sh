#!/bin/bash

FREQ="146.520M"


rtl_fm -s 22050 -f $FREQ | multimon-ng -t raw -a DTMF -
