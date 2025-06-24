# Script Runner test script
cmd("GPREDICT_ROTCTLD EXAMPLE")
wait_check("GPREDICT_ROTCTLD STATUS BOOL == 'FALSE'", 5)
