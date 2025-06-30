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
  tx_freq = tlm("GPREDICT_RIGCTLD_TX SAT_FREQ_DPLR_PKT FREQ_DPLR")
  rx_freq = tlm("GPREDICT_RIGCTLD_RX SAT_FREQ_DPLR_PKT FREQ_DPLR")
  
  # Verify if its above the horizon
  if az > 0 and el > 0:
    ON_SIGHT = "TRUE"
  else:
    ON_SIGHT = "FALSE"
  
  # Create trigger interrupts for radio operation
  if on_sight_last == "FALSE" and ON_SIGHT == "TRUE":
    AOS = "TRUE"
  elif on_sight_last == "TRUE" and ON_SIGHT == "FALSE":
    LOS = "TRUE"
  else:
    AOS = "FALSE"
    LOS = "FALSE"
  
  # Save variable for next iteration
  on_sight_last = ON_SIGHT
  
  inject_tlm("GPREDICT_ROTCTLD", "SAT_POS_STATUS", {'AOS': AOS, 'ON_SIGHT': ON_SIGHT, 'LOS': LOS})

  # Delay in seconds
  # wait(1)
  
  