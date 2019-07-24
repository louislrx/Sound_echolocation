void setup() { 
  Serial.begin(500000); 
  pinMode(A0,INPUT); //Analog ports
  pinMode(A1,INPUT);
}
 
void loop() {
  
  // read a sample
  unsigned long sample1 = analogRead(A0); 
  unsigned long sample2 = analogRead(A1);
  unsigned long outputvalue1 = map(sample1,0,1024,0,255);   
  unsigned long outputvalue2 = map(sample2,0,1024,0,255);


  analogWrite(sample1,outputvalue1); 
  analogWrite(sample2,outputvalue2);


  Serial.print(outputvalue1); //We print the data
  Serial.print(" ; ");
  Serial.println(outputvalue2);
  delay(0);  
}
