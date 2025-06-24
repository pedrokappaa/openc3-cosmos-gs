# Script Runner test script
cmd("GPREDICT_RIGCTLD EXAMPLE")
wait_check("GPREDICT_RIGCTLD STATUS BOOL == 'FALSE'", 5)
