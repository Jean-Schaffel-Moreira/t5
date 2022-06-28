#!/bin/bash		
	
usuario=jean;
while :
do
	sensor_data=$(( ( RANDOM % 100 )  + 1 ));
	current_time=$(date +"%D - %H:%M:%S.%3N");

	mosquitto_pub -h localhost -t "sensor/time" -m "$current_time";
	mosquitto_pub -h localhost -t "sensor/data" -m "$sensor_data";

	sleep 1;
done




