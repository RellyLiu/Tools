
input_file=$1

rm -rf enml_data pose_data
cat $input_file | grep "isinplace" > enml_data

awk '/isinplace/ { printf("%s %s %s\n",$12,$13,$14)}' < enml_data >> pose_data

./draw_dynamic.py ./pose_data
