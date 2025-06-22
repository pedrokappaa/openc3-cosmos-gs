# Script Runner test script
cmd("GPREDICT EXAMPLE")
wait_check("GPREDICT STATUS BOOL == 'FALSE'", 5)
