
cat $1 | grep -Eai "\[move" > move
cat $1 | grep -Eai "\[secu" > secu
cat $1 | grep -Eai "\[map" > map
cat $1 | grep -Eai "\[odom" > odom