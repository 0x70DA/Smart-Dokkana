#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

WiFiClient client;
HTTPClient http;
String serverPath;
int httpResponseCode;
String response;
int msg;

const char *ssid = "supernova.e&m";
const char *pass = "12345supernovae&m";

// Full path to the server
String serverName = "http://192.168.1.151:5000/_node_mcu";

#define echoPin D5 
#define trigPin D6
long duration; 
int distance; 
int dist();
int last;
int i=0;

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed

  // Connect to WiFi
  WiFi.begin(ssid, pass);

  while(WiFi.status() != WL_CONNECTED){
    Serial.println("Connecting....");
    delay(1000);
  }
  Serial.println("Connected to WiFi network: " + WiFi.SSID());
  Serial.print("Local IP address: ");
  Serial.println(WiFi.localIP());
  
}
void loop() {
  
  int distance_now=dist();
  //Serial.println(distance_now);
  if(i==0){last=distance_now;i+=1;}
  if((distance_now-last)>=3||(last-distance_now)>=3){
    delay(3000);

      if((distance_now-last)>=3){
        Serial.println("1");
        msg = 1;
        // Send an HTTP GET request to the server
        // Check WiFi connection status
        if (WiFi.status()== WL_CONNECTED) {
          // Add args to the request
          serverPath = serverName + "?msg=" + msg;
      
          // Send GET request to server and handle the response.
          http.begin(client, serverPath.c_str());
          httpResponseCode = http.GET();
     
          // Free resources
          http.end();
      
        }
        else {
          Serial.println("Disconnected!");
        }
      }
      if((last-distance_now)>=3){
        Serial.println("-1");
        msg = -1;
        // Send an HTTP GET request to the server
        // Check WiFi connection status
        if (WiFi.status()== WL_CONNECTED) {
          // Add args to the request
          serverPath = serverName + "?msg=" + msg;
      
          // Send GET request to server and handle the response.
          http.begin(client, serverPath.c_str());
          httpResponseCode = http.GET();
     
          // Free resources
          http.end();
      
        }
        else {
          Serial.println("Disconnected!");
        }
      }
      last=distance_now;
      }     
  }









int dist(){

  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  int raw=0;
  for (int i=0; i< 20; i++) raw += distance;
  
  return(raw/20);
  

  
}
