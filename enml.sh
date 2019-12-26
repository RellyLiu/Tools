input=$1
awk '/matchQuality/ {if ($6 == "FUSE") printf("%s %s %s %s %s %s %s, %s %s \n",$1,$2,$3,$17,$18,$19,$20,$32,$33)} \
                    {if ($6 == "static") printf("%s %s %s %s %s %s %s %s %s \n",$1,$2,$3,$14,$15,$16,$17,$22,$23)} ' < $input > enml