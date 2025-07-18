start = "TRUE"
on_sight_last = "FALSE"
ON_SIGHT = "FALSE"
AOS = "FALSE"
LOS = "FALSE"


while True:

  # Request satellite position
  cmd("GPREDICT_ROTCTLD SAT_POS_AZEL_CMD with ID '-p'")
  
  # Read satellite position response
  az = tlm("GPREDICT_ROTCTLD SAT_POS_AZEL_PKT AZ")
  el = tlm("GPREDICT_ROTCTLD SAT_POS_AZEL_PKT EL")
  
  # Request satellite frequency
  cmd("GPREDICT_RIGCTLD_TX SAT_FREQ_DPLR_CMD with ID '-f'")
  cmd("GPREDICT_RIGCTLD_RX SAT_FREQ_DPLR_CMD with ID '-f'")
  
  # Read satellite frequency response
  freq_tx = tlm("GPREDICT_RIGCTLD_TX SAT_FREQ_DPLR_PKT FREQ_DPLR_EXT")
  freq_rx = tlm("GPREDICT_RIGCTLD_RX SAT_FREQ_DPLR_PKT FREQ_DPLR_EXT")

  # Verify if its above the horizon
  if az > 0 and el > 0:
    ON_SIGHT = "TRUE"
  else:
    ON_SIGHT = "FALSE"
  
  # Trigger recording if script started mid passing
  if start == "TRUE" and ON_SIGHT == "TRUE":
    cmd("GNURADIO START_REC_CMD with ID 'aos'")
  
  # Create trigger interrupts for radio operation
  if on_sight_last == "FALSE" and ON_SIGHT == "TRUE":
    AOS = "TRUE"
    cmd("GNURADIO START_REC_CMD with ID 'aos'")
    
  elif on_sight_last == "TRUE" and ON_SIGHT == "FALSE":
    LOS = "TRUE"
    cmd("GNURADIO STOP_REC_CMD with ID 'los'")
   
  else:
    AOS = "FALSE"
    LOS = "FALSE"
  
  # Save variable for next iteration
  on_sight_last = ON_SIGHT
  start = "FALSE"
  
  # Save simulated track telemetry to show on screen
  inject_tlm("GPREDICT_ROTCTLD", "SAT_POS_STATUS", {"AOS": AOS, "ON_SIGHT": ON_SIGHT, "LOS": LOS})
  
  # Update radio frequencies regarding Doppler effect
  if ON_SIGHT == "TRUE":
    cmd("GNURADIO", "UPDT_FREQ_TX_CMD", {"ID": "freq_tx ", "FREQ": str(int(freq_tx))})
    cmd("GNURADIO", "UPDT_FREQ_RX_CMD", {"ID": "freq_rx ", "FREQ": str(int(freq_rx))})
  
  # Delay in seconds
  wait(1)
  
  