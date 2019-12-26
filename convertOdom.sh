
input=$1
start=$2
end=$3
rm -rf ~/log/odom_data

awk '/pose:/ {if (NR >= '$start' && NR <= '$end') printf("%s %s %s\n",$5,$6,$7)}' < $input > ~/log/odom_data
