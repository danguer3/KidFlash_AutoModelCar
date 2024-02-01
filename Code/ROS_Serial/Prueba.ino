#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/Int8.h>

#define led1 2
#define led2 3
#define led3 4

void SpeedsCallback(const std_msgs::Float32MultiArray& msg)
{
  if(msg.data[0] == 0){
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
  }
  else if(msg.data[0] == 1){
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
  }
  else if(msg.data[0] == 2){
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, LOW);
  }
  else if(msg.data[0] == 3){
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, LOW);
  }
  else if(msg.data[0] == 4){
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, HIGH);
  }
}
std_msgs::Float32MultiArray IRSensors_Array_msg;

ros::Publisher pubIRSensors_Array("/minirobot/hardware/sensors",&IRSensors_Array_msg);    // Hago un publicador llamado pubIRSensors_Array, donde voy a publicar el mensaje IRSensors_Array_msg
ros::NodeHandle n;
ros::Subscriber<std_msgs::Float32MultiArray>subSpeeds("/leds",&SpeedsCallback);

void setup(){
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);

  n.initNode();
  n.advertise(pubIRSensors_Array);
  n.subscribe(subSpeeds);
}

void loop(){
  n.spinOnce();
}
