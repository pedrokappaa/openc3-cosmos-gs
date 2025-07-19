#! /usr/bin/bash

# Start OpenC3 COSMOS
./openc3.sh run &

# Start rig/rotctld TCP interfaces with Gpredict 
rotctld --port=4533 &
rigctld --port=4532 &
rigctld --port=4531 &

# Start Gpredict
gpredict &

# Start GNUradio flowchart
python3 gnuradio-src/gnuradio_openc3.py

# After closing app, kill all processes
killall rotctld & killall rigctld & killall gpredict
./openc3.sh stop
